import streamlit as st

# --- KONFIGURASI KEAMANAN ---
PASSWORD_RAHASIA = "whale123"  # <--- Ganti dengan password pilihanmu sendiri!

def check_password():
    """Mengembalikan True jika password yang dimasukkan benar."""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    # Tampilan Form Login
    st.title("🔒 Akses Terbatas")
    pwd = st.text_input("Masukkan Password Asisten Keuangan:", type="password")
    
    if st.button("Masuk"):
        if pwd == PASSWORD_RAHASIA:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Password Salah!")
    return False

# --- JALANKAN KEAMANAN ---
if check_password():
    # --- SEMUA KODE LAMA KAMU PINDAHKAN KE SINI ---
    st.title("💼 Wealth Advisor AI - Dashboard")
    
    st.subheader("Simulasi Pertumbuhan Aset")
    aset_awal = 195000000000
    bunga_tahunan = st.slider("Asumsi Bunga/Dividen Tahunan (%)", 0.0, 20.0, 5.0)

    hasil_setahun = aset_awal * (1 + (bunga_tahunan / 100))
    profit = hasil_setahun - aset_awal

    st.metric(label="Total Aset Tahun Depan", value=f"Rp {hasil_setahun:,.0f}")
    st.write(f"Potensi keuntungan bersih Anda: **Rp {profit:,.0f}**")

    st.divider()
    st.subheader("Tanya Asisten AI")
    pertanyaan = st.text_input("Contoh: Apakah aman beli saham IPO sekarang?")

    if pertanyaan:
        st.write(f"🤖 **Analisis AI:** Mengingat aset Anda Rp195M, pertanyaan tentang '{pertanyaan}' sangat krusial. Saya menyarankan tetap waspada pada volatilitas pasar.")
