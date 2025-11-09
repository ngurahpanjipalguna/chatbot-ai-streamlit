# 🧠 Chatbot Guru Biologi Berbasis AI

Chatbot ini dirancang sebagai **asisten pembelajaran biologi interaktif** yang menggunakan **Google Gemini AI (LLM)** untuk memahami bahasa alami dan memberikan jawaban yang relevan, edukatif, serta mudah dipahami.  
Dibangun menggunakan **Streamlit** untuk antarmuka web yang sederhana dan interaktif.

---

## 📘 Fitur Utama
- 💬 **Percakapan interaktif** antara siswa dan chatbot guru biologi.  
- 🧬 **Pemahaman konteks biologi:** Chatbot menjawab pertanyaan tentang topik seperti sel, fotosintesis, ekosistem, dan lain-lain.  
- 🎓 **Penyesuaian gaya bahasa:** Menyesuaikan penjelasan sesuai tingkat pelajar (SMP/SMA).  
- 🧩 **Pembuatan kuis otomatis:** Dapat membantu guru membuat pertanyaan latihan.  
- ⚙️ **Ditenagai oleh AI (Gemini API)** untuk menghasilkan jawaban alami dan akurat.

---

## 🧰 Teknologi yang Digunakan
| Komponen | Deskripsi |
|-----------|------------|
| **Python 3.10+** | Bahasa pemrograman utama |
| **Streamlit** | Framework web untuk membuat antarmuka chatbot |
| **Google Generative AI (Gemini API)** | Model AI untuk pemrosesan bahasa alami |
| **python-dotenv** | Untuk memuat API Key dari file `.env` |

---

## 🚀 Instalasi & Menjalankan Proyek

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/chabot-biology.git
cd chabot-biology
```

### 2️⃣ Buat Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instal Dependensi
```bash
pip install -r requirements.txt
```

Contoh isi `requirements.txt`:
```
streamlit
google-generativeai
python-dotenv
```

### 4️⃣ Buat File `.env`
Tambahkan API Key Gemini milikmu:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

> 🔑 Dapatkan API key dari: [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5️⃣ Jalankan Aplikasi
```bash
streamlit run biology_teacher_gemini.py
```

Setelah dijalankan, buka di browser:
```
http://localhost:8501
```

---

## 💡 Cara Menggunakan
1. Jalankan aplikasi Streamlit.  
2. Ketik pertanyaan biologi di kolom input (contoh: *"Apa itu mitosis?"*).  
3. Chatbot akan menjawab layaknya seorang guru biologi yang ramah dan edukatif.  
4. Kamu bisa lanjut bertanya topik lain seperti:
   - “Bagaimana proses fotosintesis?”
   - “Apa perbedaan mitosis dan meiosis?”
   - “Sebutkan fungsi organel sel!”

---

## 🧠 Contoh Kode Utama
```python
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("🧬 Chatbot Guru Biologi")
st.write("Tanyakan apa saja tentang biologi!")

model = genai.GenerativeModel("gemini-1.5-pro")

user_input = st.text_input("Pertanyaan kamu:")
if st.button("Tanya"):
    if user_input:
        prompt = f"Kamu adalah guru biologi yang sabar dan informatif. Jelaskan dengan mudah: {user_input}"
        response = model.generate_content(prompt)
        st.success(response.text)
```

---

## 🧑‍🏫 Peran AI dalam Chatbot Ini
AI berfungsi untuk:
- **Memahami maksud pertanyaan siswa** menggunakan NLP.  
- **Menghasilkan penjelasan ilmiah yang relevan.**  
- **Berinteraksi secara edukatif** layaknya guru sungguhan.  
- **Menyesuaikan gaya bahasa dan kedalaman penjelasan.**

---

## 🧾 Lisensi
Proyek ini bersifat open-source di bawah lisensi MIT.  
Silakan gunakan dan kembangkan sesuai kebutuhan edukasi.

---

## 👨‍💻 Pembuat
**Panji Palguna**  
📧 cerdaskanbangsaindonesia@gmail.com  
🌱 “Mendidik lewat teknologi untuk masa depan yang lebih cerdas.”
