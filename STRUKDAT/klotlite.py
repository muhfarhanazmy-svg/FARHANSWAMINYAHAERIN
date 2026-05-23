"""
Sistem Antrian Boarding Kereta Api
Struktur Data: Queue (FIFO) — enqueue, dequeue, peek
"""

import streamlit as st, base64, os, tempfile, io
from collections import deque
from gtts import gTTS

# ── QUEUE ─────────────────────────────────────────────────
class AntrianBoarding:
    def __init__(self):
        self._q: deque = deque()
        self.riwayat: list = []

    def enqueue(self, nama: str, gate: str):
        self._q.append({"nama": nama.strip().title(), "gate": gate})

    def dequeue(self) -> dict | None:
        if not self._q: return None
        p = self._q.popleft()
        self.riwayat.append(p)
        return p

    def peek(self) -> dict | None:
        return self._q[0] if self._q else None

    def to_list(self): return list(self._q)
    def size(self):    return len(self._q)

# ── AUDIO — gaya announcer Stasiun KAI ───────────────────
def buat_audio(nama: str, gate: str) -> bytes | None:
    try:
        teks = (
            f"Perhatian, perhatian. "
            f"Kepada penumpang atas nama {nama}, "
            f"dimohon segera menuju {gate} "
            f"untuk melakukan proses boarding. "
            f"Kami tunggu kehadiran Anda. Terima kasih."
        )
        tts = gTTS(text=teks, lang="id", slow=False)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        return buf.read()
    except:
        return None

# ── INIT ──────────────────────────────────────────────────
if "antrian" not in st.session_state: st.session_state.antrian = AntrianBoarding()
if "notif"   not in st.session_state: st.session_state.notif   = None
if "audio"   not in st.session_state: st.session_state.audio   = None
antrian: AntrianBoarding = st.session_state.antrian

# ── PAGE ──────────────────────────────────────────────────
st.set_page_config(page_title="Antrian Boarding", page_icon="🚆")
st.title("🚆 Antrian Boarding Kereta Api")
st.caption("Struktur Data **Queue (FIFO)** · enqueue · dequeue · peek")

# ── AUDIO PLAYER ──────────────────────────────────────────
if st.session_state.audio:
    st.subheader("🔊 Pengumuman Boarding")
    st.audio(st.session_state.audio, format="audio/mp3", autoplay=True)
    st.session_state.audio = None

# ── NOTIFIKASI ────────────────────────────────────────────
if st.session_state.notif:
    tipe, msg = st.session_state.notif
    getattr(st, tipe)(msg)
    st.session_state.notif = None

# ── METRICS ───────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
c1.metric("🧍 Antrian",  antrian.size())
c2.metric("✅ Boarding", len(antrian.riwayat))
c3.metric("👤 Depan",    antrian.peek()["nama"] if antrian.peek() else "—")

st.divider()

# ── INPUT + TOMBOL ────────────────────────────────────────
col1, col2 = st.columns([3, 1])
nama = col1.text_input("Nama Penumpang", placeholder="Contoh: Budi Santoso")
gate = col2.selectbox("Gate", ["Gate 1", "Gate 2", "Gate 3"])

b1, b2, b3 = st.columns(3)
if b1.button("➕ Enqueue",      use_container_width=True):
    if nama.strip():
        antrian.enqueue(nama, gate)
        st.session_state.notif = ("success", f"**{nama.strip().title()}** masuk antrian → {gate}")
    else:
        st.session_state.notif = ("warning", "Nama tidak boleh kosong!")
    st.rerun()

if b2.button("🎤 Dequeue",      use_container_width=True):
    p = antrian.dequeue()
    if p:
        st.session_state.notif = ("success", f"Memanggil **{p['nama']}** → {p['gate']}")
        st.session_state.audio = buat_audio(p["nama"], p["gate"])
    else:
        st.session_state.notif = ("warning", "Antrian kosong!")
    st.rerun()

if b3.button("👀 Peek / Front", use_container_width=True):
    p = antrian.peek()
    st.session_state.notif = ("info",
        f"Depan: **{p['nama']}** → {p['gate']} *(tidak dihapus)*" if p else "Antrian kosong.")
    st.rerun()

st.divider()

# ── VISUALISASI ANTRIAN ───────────────────────────────────
GATE_EMOJI = {"Gate 1": "🔵", "Gate 2": "🟢", "Gate 3": "🟠"}
st.subheader(f"📋 Antrian Saat Ini ({antrian.size()} orang)")

q_list = antrian.to_list()
if not q_list:
    st.info("Antrian kosong — silakan tambah penumpang.")
else:
    cards = ""
    for i, p in enumerate(q_list):
        is_front = i == 0
        bg     = "#e94560" if is_front else "#16213e"
        border = "#e94560" if is_front else "#2a2a4a"
        badge  = "DEPAN ▶" if is_front else f"#{i+1}"
        cards += f"""
        <div style="background:{bg};border:1.5px solid {border};border-radius:10px;
                    padding:12px 18px;margin-bottom:8px;display:flex;
                    align-items:center;justify-content:space-between;">
            <span>
                <span style="background:#fff3;color:#fff;font-size:.72rem;font-weight:700;
                             padding:2px 8px;border-radius:20px;margin-right:10px;">{badge}</span>
                <span style="color:#fff;font-size:1rem;font-weight:600;">{p['nama']}</span>
            </span>
            <span style="color:#ddd;font-size:.9rem;">{GATE_EMOJI.get(p['gate'],'🔲')} {p['gate']}</span>
        </div>"""
    st.markdown(cards, unsafe_allow_html=True)

# ── RIWAYAT ───────────────────────────────────────────────
if antrian.riwayat:
    st.divider()
    st.subheader("🏁 Riwayat Boarding")
    for i, p in enumerate(reversed(antrian.riwayat[-8:])):
        st.markdown(f"**{i+1}.** {p['nama']} — *{p['gate']}*")