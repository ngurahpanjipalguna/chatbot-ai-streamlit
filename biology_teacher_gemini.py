import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔒 Load API key dari .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Konfigurasi Gemini
genai.configure(api_key=api_key)

# 🔍 Coba pilih model yang tersedia
try:
    model = genai.GenerativeModel("gemini-2.5-pro")  # gunakan model baru kalau tersedia
except Exception:
    model = genai.GenerativeModel("gemini-pro")  # fallback ke model stabil

# 🧬 Konfigurasi halaman
st.set_page_config(page_title="Guru Biologi Virtual (Gemini)", page_icon="🧫")
st.title("🧠 Guru Biologi Virtual - Gemini AI")
st.write("Hai! Saya guru biologi virtualmu. Tanyakan apa saja tentang biologi ya 🌿")

# Simpan riwayat chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input pengguna
user_input = st.chat_input("Tulis pertanyaanmu di sini...")

# Tampilkan chat sebelumnya
for role, content in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(content)

# Proses input baru
if user_input:
    st.session_state.chat_history.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Guru Biologi sedang berpikir... 🧬"):
            response = model.generate_content(
                f"Kamu adalah guru biologi yang sabar dan menjelaskan dengan mudah dipahami siswa. Jawab pertanyaan berikut: {user_input}"
            )
            answer = response.text
            st.markdown(answer)

    st.session_state.chat_history.append(("assistant", answer))
