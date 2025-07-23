import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

puanlama_tablolari = {
    "A": {
        "kriterler": [
            "Test başlığı anlaşılır mı?",
            "Öncelik bilgisi girilmiş mi?",
            "Test stepleri var ve doğru ayrıştırılmış mı?",
            "Senaryonun hangi clientta koşulacağı belli mi?",
            "Expected result bulunuyor mu?"
        ],
        "puan": 20
    },
    "B": {
        "kriterler": [
            "Test başlığı anlaşılır mı?",
            "Öncelik bilgisi girilmiş mi?",
            "Test ön koşul eklenmiş mi?",
            "Test stepleri var ve doğru ayrıştırılmış mı?",
            "Senaryonun hangi clientta koşulacağı belli mi?",
            "Expected result bulunuyor mu?"
        ],
        "puan": 17
    },
    "C": {
        "kriterler": [
            "Test başlığı anlaşılır mı?",
            "Öncelik bilgisi girilmiş mi?",
            "Test datası eklenmiş mi?",
            "Test stepleri var ve doğru ayrıştırılmış mı?",
            "Senaryonun hangi clientta koşulacağı belli mi?",
            "Expected result bulunuyor mu?"
        ],
        "puan": 17
    },
    "D": {
        "kriterler": [
            "Test başlığı anlaşılır mı?",
            "Öncelik bilgisi girilmiş mi?",
            "Test datası eklenmiş mi?",
            "Test ön koşul eklenmiş mi?",
            "Test stepleri var ve doğru ayrıştırılmış mı?",
            "Senaryonun hangi clientta koşulacağı belli mi?",
            "Expected result bulunuyor mu?"
        ],
        "puan": 14
    }
}

st.set_page_config(page_title="Test Case Puanlama", layout="wide")
st.title("🧪 Test Case Puanlayıcı")

uploaded_file = st.file_uploader("📷 Bir test case ekran görüntüsü yükleyin", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Görsel", use_column_width=True)

    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    extracted_text = pytesseract.image_to_string(gray, lang="tur")
    st.text_area("📄 OCR ile alınan metin:", extracted_text, height=200)

    tablo_turu = st.selectbox("📊 Hangi tabloya göre değerlendirme yapılacak?", list(puanlama_tablolari.keys()))
    tablo = puanlama_tablolari[tablo_turu]

    st.markdown("### ✅ Kriter Değerlendirme")
    toplam_puan = 0
    for kriter in tablo["kriterler"]:
        mevcut = st.checkbox(kriter, value=True)
        if mevcut:
            toplam_puan += tablo["puan"]

    st.markdown(f"## 🎯 Toplam Puan: {toplam_puan} / {tablo['puan'] * len(tablo['kriterler'])}")
