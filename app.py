import streamlit as st

# 1. Judul Aplikasi
st.title("💼 Wealth Advisor AI - Dashboard")

# 2. Input Sederhana
st.subheader("Simulasi Pertumbuhan Aset")
aset_awal = 195000000000  # Rp195 Miliar
bunga_tahunan = st.slider("Asumsi Bunga/Dividen Tahunan (%)", 0.0, 20.0, 5.0)

# 3. Logika Perhitungan
hasil_setahun = aset_awal * (1 + (bunga_tahunan / 100))
profit = hasil_setahun - aset_awal

# 4. Tampilan Hasil
st.metric(label="Total Aset Tahun Depan", value=f"Rp {hasil_setahun:,.0f}")
st.write(f"Potensi keuntungan bersih Anda: **Rp {profit:,.0f}**")

# 5. Fitur Chatbot Sederhana (Simulasi)
st.divider()
st.subheader("Tanya Asisten AI")
pertanyaan = st.text_input("Contoh: Apakah aman beli saham IPO sekarang?")

if pertanyaan:
    st.write(f"🤖 **Analisis AI:** Mengingat aset Anda Rp195M, pertanyaan tentang '{pertanyaan}' sangat krusial. Secara umum, saya menyarankan diversifikasi 30% ke Blue Chip dan tetap pegang cash 20% untuk jaga-jaga.")
