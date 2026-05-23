import streamlit as st
from collections import deque
from gtts import gTTS
import base64
import io

# --- LOGIKA INTI QUEUE (CORE LOGIC) ---
class AntrianBoarding:
    def __init__(self):
        if "queue" not in st.session_state:
            st.session_state.queue = deque()
        if "panggilan_terakhir" not in st.session_state:
            st.session_state.panggilan_terakhir = None

    def enqueue(self, nama):
        st.session_state.queue.append(nama)

    def dequeue(self):
        if not self.is_empty():
            return st.session_state.queue.popleft()
        return None

    def peek(self):
        return st.session_state.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(st.session_state.queue) == 0

    def get_all(self):
        return list(st.session_state.queue)

# --- FUNGSI AUDIO (gTTS) ---
def play_announcement(nama):
    teks = f"Penumpang atas nama {nama}, silakan menuju gate 2. Silakan menuju boarding."
    tts = gTTS(text=teks, lang='id')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    
    # Encode audio ke base64 agar bisa diputar otomatis di Streamlit
    audio_bytes = fp.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# --- STREAMLIT UI ---
def main():
    st.set_page_config(page_title="Sistem Antrian Stasiun", page_icon="🚆")
    system = AntrianBoarding()

    st.title("🚆 Sistem Boarding Penumpang")
    st.subheader("Simulasi Struktur Data Queue (FIFO)")
    st.divider()

    # Sidebar: Input Area
    with st.sidebar:
        st.header("Input Data")
        nama_input = st.text_input("Nama Penumpang")
        if st.button("➕ Tambah Antrian", use_container_width=True):
            if nama_input:
                system.enqueue(nama_input)
                st.success(f"{nama_input} berhasil masuk antrian!")
            else:
                st.warning("Masukkan nama terlebih dahulu.")

    # Main Area: Kontrol
    col1, col2 = st.columns(2)

    with col1:
        st.info("### Panel Kontrol")
        if st.button("🎤 Panggil Penumpang (Dequeue)", type="primary", use_container_width=True):
            panggil = system.dequeue()
            if panggil:
                st.session_state.panggilan_terakhir = panggil
                play_announcement(panggil)
            else:
                st.error("Antrian kosong!")

        if st.button("👀 Lihat Depan (Peek)", use_container_width=True):
            depan = system.peek()
            if depan:
                st.write(f"Penumpang paling depan: **{depan}**")
            else:
                st.write("Tidak ada antrian.")

    with col2:
        st.info("### Status Saat Ini")
        if st.session_state.panggilan_terakhir:
            st.success(f"**Sedang Boarding:** \n\n {st.session_state.panggilan_terakhir}")
        else:
            st.write("Belum ada panggilan.")

    # Visualisasi Antrian
    st.divider()
    st.subheader("📋 Daftar Antrian Real-time")
    antrian_list = system.get_all()

    if antrian_list:
        # Menampilkan antrian dalam bentuk kartu horizontal
        cols = st.columns(len(antrian_list) if len(antrian_list) < 5 else 5)
        for i, nama in enumerate(antrian_list):
            with cols[i % 5]:
                st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 10px;">
                    <small>Urutan {i+1}</small><br>
                    <strong>{nama}</strong>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.write("Antrian kosong. Silakan tambah penumpang.")

if __name__ == "__main__":
    main()