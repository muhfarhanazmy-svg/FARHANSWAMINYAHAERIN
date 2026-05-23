"""
SISTEM ANTRIAN RESTORAN - MIE GACOAN
Mata Kuliah : Struktur Data
Konsep      : Queue (FIFO - First In First Out)
"""
import streamlit as st
from collections import deque
from gtts import gTTS
import os
import tempfile
import base64

# ─────────────────────────────────────────────
# INISIALISASI SESSION STATE
# Session state digunakan agar data antrian
# tidak hilang saat halaman di-refresh
# ─────────────────────────────────────────────
if "queue" not in st.session_state:
    st.session_state.queue = deque()   # struktur data Queue

# ─────────────────────────────────────────────
# FUNGSI QUEUE
# ─────────────────────────────────────────────
def enqueue(nama: str, pesanan: str):
    """
    ENQUEUE: Menambahkan pelanggan ke belakang antrian.
    Kompleksitas waktu: O(1)
    """
    pelanggan = {"nama": nama, "pesanan": pesanan}
    st.session_state.queue.append(pelanggan)  # append = tambah ke belakang

def dequeue() -> dict | None:
    """
    DEQUEUE: Mengambil pelanggan dari depan antrian.
    Kompleksitas waktu: O(1)
    Returns: dict pelanggan, atau None jika antrian kosong
    """
    if is_empty():
        return None
    return st.session_state.queue.popleft()  # popleft = ambil dari depan

def front() -> dict | None:
    """Melihat pelanggan paling depan tanpa menghapusnya."""
    if is_empty():
        return None
    return st.session_state.queue[0]

def rear() -> dict | None:
    """Melihat pelanggan paling belakang tanpa menghapusnya."""
    if is_empty():
        return None
    return st.session_state.queue[-1]

def is_empty() -> bool:
    """Mengecek apakah antrian kosong."""
    return len(st.session_state.queue) == 0

def size() -> int:
    """Mengembalikan jumlah pelanggan dalam antrian."""
    return len(st.session_state.queue)

# ─────────────────────────────────────────────
# FUNGSI AUDIO (gTTS)
# ─────────────────────────────────────────────

def buat_audio(teks: str) -> str:
    """Membuat audio dari teks menggunakan gTTS dan mengembalikan sebagai base64 string."""
    tts = gTTS(text=teks, lang="id")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        tmp_path = tmp.name

    with open(tmp_path, "rb") as f:
        audio_bytes = f.read()
    os.remove(tmp_path)

    return base64.b64encode(audio_bytes).decode()

def putar_audio(teks: str):
    """Merender audio player HTML di Streamlit."""
    b64 = buat_audio(teks)
    audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TAMPILAN UTAMA
# ─────────────────────────────────────────────

st.set_page_config(page_title="Antrian Mie Gacoan", page_icon="🍜", layout="centered")

st.title("🍜 Sistem Antrian Restoran")
st.subheader("Mie Gacoan — Konsep Queue (FIFO)")


st.divider()

# ─────────────────────────────────────────────
# BAGIAN 1: ENQUEUE
# ─────────────────────────────────────────────
st.subheader("➕ Tambah Pelanggan (Enqueue)")

col1, col2 = st.columns(2)
with col1:
    nama_input = st.text_input("Nama Pelanggan", placeholder="cth: Farhan")
with col2:
    pesanan_input = st.text_input("Pesanan / No. Meja", placeholder="cth: Mie Level 3 / Meja A12")

if st.button("🪑 Masukkan ke Antrian", use_container_width=True):
    if nama_input.strip() and pesanan_input.strip():
        enqueue(nama_input.strip(), pesanan_input.strip())
        st.success(f"✅ **{nama_input}** berhasil masuk antrian. Posisi: #{size()}")
    else:
        st.warning("⚠️ Nama dan pesanan tidak boleh kosong.")

st.divider()

# ─────────────────────────────────────────────
# BAGIAN 2: DEQUEUE
# ─────────────────────────────────────────────
st.subheader("📢 Panggil Pelanggan (Dequeue)")

if st.button("🔔 Panggil Pelanggan Berikutnya", use_container_width=True, type="primary"):
    if is_empty():
        st.error("❌ Antrian kosong! Tidak ada pelanggan yang perlu dipanggil.")
    else:
        pelanggan = dequeue()
        nama    = pelanggan["nama"]
        pesanan = pelanggan["pesanan"]

        teks_audio = f"Atas nama {nama}, pesanan {pesanan} siap diambil. Silakan menuju kasir."

        st.success(f"📣 Memanggil: **{nama}** — {pesanan}")
        st.info(f"🔊 *\"{teks_audio}\"*")

        try:
            putar_audio(teks_audio)
        except Exception as e:
            st.warning(f"Audio tidak dapat diputar: {e}")

st.divider()

# ─────────────────────────────────────────────
# BAGIAN 3: INFO ANTRIAN
# ─────────────────────────────────────────────
st.subheader("📋 Status Antrian")

col_f, col_r, col_s = st.columns(3)

with col_f:
    f = front()
    st.metric("🟢 Depan (Front)", f["nama"] if f else "—")

with col_r:
    r = rear()
    st.metric("🔴 Belakang (Rear)", r["nama"] if r else "—")

with col_s:
    st.metric("👥 Total Antrian", size())

# ─────────────────────────────────────────────
# BAGIAN 4: ISI ANTRIAN
# ─────────────────────────────────────────────
st.subheader("🗂️ Isi Antrian Saat Ini")

if is_empty():
    st.info("Antrian kosong. Silakan tambahkan pelanggan.")
else:
    for i, p in enumerate(st.session_state.queue):
        label = "🟢 DEPAN" if i == 0 else ("🔴 BELAKANG" if i == size() - 1 else f"#{i+1}")
        st.write(f"**{label}** → {p['nama']} | {p['pesanan']}")

st.divider()

# Reset antrian
if st.button("🗑️ Reset Antrian", use_container_width=True):
    st.session_state.queue.clear()
    st.success("Antrian telah direset.")
    st.rerun()