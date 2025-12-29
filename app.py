import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI KEAMANAN & API ---
# Silakan ganti password dan API Key di bawah ini
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

    st.set_page_config(page_title="Login - Wealth Advisor", page_icon="🔒")
    st.title("🔒 Private Access")
    st.write("Aplikasi ini khusus untuk pengelolaan aset pribadi Rp195 Miliar.")
    
    pwd = st.text_input("Masukkan Password Rahasia:", type="password")
    if st.button("Masuk Sekarang"):
        if pwd == PASSWORD_RAHASIA:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Password salah. Akses ditolak.")
    return False

# --- 3. TAMPILAN UTAMA (Jika Login Berhasil) ---
if check_password():
    st.set_page_config(page_title="Wealth Advisor AI", page_icon="💼")
    st.title("💼 Wealth Advisor AI - Private Dashboard")
    
    # Bagian Dashboard Angka
    st.subheader("Simulasi Pertumbuhan Aset")
    col1, col2 = st.columns(2)
    
    aset_awal = 195000000000 # Rp195 Miliar
    
    with col1:
        bunga_tahunan = st.slider("Asumsi Return/Dividen Tahunan (%)", 0.0, 20.0, 5.0)
    
    hasil_setahun = aset_awal * (1 + (bunga_tahunan / 100))
    profit = hasil_setahun - aset_awal
    
    with col2:
        st.metric(label="Estimasi Nilai Aset", value=f"Rp {hasil_setahun:,.0f}")
        st.caption(f"Potensi Keuntungan Bersih: Rp {profit:,.0f}")

    st.divider()

    # Bagian Chatbot Pintar
    st.subheader("💬 Konsultasi Strategi Investasi")
    st.write("Tanyakan apa saja kepada AI mengenai pengelolaan aset Anda.")
    
    user_input = st.text_input("Contoh: Berikan rekomendasi alokasi aset untuk dana Rp195 M agar aman dari inflasi.")

    if user_input:
        with st.spinner("Sedang berpikir..."):
            try:
                # Instruksi khusus agar AI sadar dia menangani dana besar
                prompt_lengkap = f"""
                Kamu adalah Penasihat Keuangan Senior (Private Banker) kelas dunia. 
                Klienmu memiliki aset tunai sebesar Rp195 Miliar. 
                Berikan jawaban yang sangat profesional, mendetail, dan berfokus pada pelestarian kekayaan (wealth preservation).
                Pertanyaan Klien: {user_input}
                """
                
                response = model.generate_content(prompt_lengkap)
                st.markdown("### 🤖 Rekomendasi Asisten AI:")
                st.info(response.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}. Pastikan API Key Gemini sudah aktif.")

    # Footer
    st.divider()
    st.caption("Eksklusif dibuat untuk Pengelolaan Aset Pribadi. Powered by Gemini AI.")
