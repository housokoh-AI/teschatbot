import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI KEAMANAN & API ---
PASSWORD_RAHASIA = "whale123" 
GEMINI_API_KEY = "AIzaSyB7lgc7AA7tJcjoyl3nVBi8VpZyowtx9M8"

# Inisialisasi Otak Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. FUNGSI LOGIN ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    
    if st.session_state["password_correct"]:
        return True

    st.title("🔒 Private Access")
    st.write("Aplikasi ini khusus untuk pengelolaan aset pribadi Rp195 Miliar.")
    
    pwd = st.text_input("Masukkan Password Rahasia:", type="password")
    if st.button("Masuk Sekarang"):
        if pwd == PASSWORD_RAHASIA:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Password salah.")
    return False

# --- 3. TAMPILAN UTAMA ---
if check_password():
    st.title("💼 Wealth Advisor AI - Dashboard")
    
    # Dashboard Angka
    aset_awal = 195000000000 
    bunga = st.slider("Asumsi Return Tahunan (%)", 0.0, 20.0, 5.0)
    total = aset_awal * (1 + (bunga / 100))
    
    st.metric(label="Estimasi Nilai Aset", value=f"Rp {total:,.0f}")

    st.divider()

    # Chatbot Pintar (BAGIAN INI YANG BIKIN PINTAR)
    st.subheader("💬 Konsultasi Strategi Investasi")
    user_input = st.text_input("Tanya AI tentang aset Rp195M kamu:")

    if user_input:
        with st.spinner("Sedang menganalisis..."):
            # Prompt ini memerintahkan Gemini untuk menjawab dengan cerdas
            prompt = f"Anda adalah penasihat keuangan VVIP. Klien memiliki Rp195 Miliar. Jawab dengan sangat detail: {user_input}"
            response = model.generate_content(prompt)
            st.markdown("### 🤖 Rekomendasi Asisten AI:")
            st.info(response.text) # Ini akan menampilkan jawaban asli dari Gemini
