"""
==============================================================
  SISTEM ANTRIAN BOARDING PENUMPANG KERETA API
  Implementasi Struktur Data: QUEUE (FIFO)
  Studi Kasus: Boarding Stasiun Kereta Api
==============================================================
"""

import streamlit as st
import time
import base64
from collections import deque
from gtts import gTTS
import os
import tempfile

# ─────────────────────────────────────────────
#  CORE QUEUE CLASS — Struktur Data Utama
# ─────────────────────────────────────────────

class AntrianBoarding:
    """
    Queue FIFO sederhana untuk sistem boarding kereta.
    Operasi utama: enqueue, dequeue, peek, is_empty, size.
    """

    def __init__(self):
        self._queue: deque = deque()   # deque sebagai backing store O(1)
        self.riwayat: list  = []       # log penumpang yang sudah boarding

    # ---------- ENQUEUE ----------
    def enqueue(self, nama: str, gate: str) -> None:
        """Tambah penumpang ke belakang antrian."""
        penumpang = {"nama": nama.strip().title(), "gate": gate}
        self._queue.append(penumpang)

    # ---------- DEQUEUE ----------
    def dequeue(self) -> dict | None:
        """Ambil & hapus penumpang paling depan (FIFO)."""
        if self.is_empty():
            return None
        penumpang = self._queue.popleft()
        self.riwayat.append(penumpang)
        return penumpang

    # ---------- PEEK / FRONT ----------
    def peek(self) -> dict | None:
        """Lihat penumpang paling depan TANPA menghapus."""
        if self.is_empty():
            return None
        return self._queue[0]

    # ---------- UTILITAS ----------
    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def size(self) -> int:
        return len(self._queue)

    def to_list(self) -> list:
        """Kembalikan antrian sebagai list (untuk tampilan UI)."""
        return list(self._queue)


# ─────────────────────────────────────────────
#  AUDIO ANNOUNCEMENT — gTTS
# ─────────────────────────────────────────────

def buat_audio_pengumuman(nama: str, gate: str) -> str:
    """
    Generate audio pengumuman stasiun menggunakan gTTS.
    Kembalikan path file audio sementara.
    """
    teks = (
        f"Perhatian! Penumpang atas nama {nama}, "
        f"silakan menuju {gate} untuk proses boarding. "
        f"Terima kasih."
    )
    tts = gTTS(text=teks, lang="id", slow=False)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    return tmp.name


def audio_ke_base64(path: str) -> str:
    """Konversi file audio ke base64 untuk autoplay di browser."""
    with open(path, "rb") as f:
        data = f.read()
    os.unlink(path)          # hapus file sementara
    return base64.b64encode(data).decode("utf-8")


def autoplay_audio(b64: str) -> None:
    """Inject tag <audio> dengan autoplay ke Streamlit."""
    html = f"""
    <audio autoplay style="display:none">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(html, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  INISIALISASI SESSION STATE
# ─────────────────────────────────────────────

def init_state():
    if "antrian" not in st.session_state:
        st.session_state.antrian = AntrianBoarding()
    if "pesan_info"  not in st.session_state:
        st.session_state.pesan_info  = None   # dict: {tipe, teks}
    if "peek_result" not in st.session_state:
        st.session_state.peek_result = None
    if "audio_b64"   not in st.session_state:
        st.session_state.audio_b64   = None


# ─────────────────────────────────────────────
#  KOMPONEN UI
# ─────────────────────────────────────────────

GATE_OPTIONS = ["Gate 1", "Gate 2", "Gate 3"]
GATE_EMOJI   = {"Gate 1": "🔵", "Gate 2": "🟢", "Gate 3": "🟠"}

def render_header():
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
        border-left: 6px solid #e94560;
    ">
        <h1 style="color:#ffffff; margin:0; font-size:1.9rem; letter-spacing:1px;">
            🚆 Sistem Antrian Boarding
        </h1>
        <p style="color:#a0b4c8; margin:6px 0 0; font-size:0.95rem;">
            Studi Kasus Struktur Data <strong style="color:#e94560">Queue (FIFO)</strong>
            &nbsp;·&nbsp; Stasiun Kereta Api
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_info_box():
    """Tampilkan kotak info / peringatan setelah operasi."""
    msg = st.session_state.pesan_info
    if not msg:
        return
    warna = {"sukses": "#2ecc71", "peringatan": "#f39c12", "info": "#3498db"}
    ikon  = {"sukses": "✅", "peringatan": "⚠️", "info": "ℹ️"}
    t = msg["tipe"]
    st.markdown(f"""
    <div style="
        background: {warna[t]}22;
        border: 1px solid {warna[t]};
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 16px;
        color: {warna[t]};
        font-weight: 600;
    ">
        {ikon[t]} &nbsp; {msg["teks"]}
    </div>
    """, unsafe_allow_html=True)


def render_antrian_visual(antrian_list: list):
    """Visualisasi antrian sebagai kartu bernomor urut."""
    st.markdown("### 📋 Antrian Saat Ini")
    if not antrian_list:
        st.markdown("""
        <div style="
            text-align:center; padding:40px;
            background:#1e1e2e; border-radius:12px;
            color:#666; font-size:1.1rem;
        ">
            🎉 Antrian kosong — semua penumpang sudah boarding!
        </div>
        """, unsafe_allow_html=True)
        return

    cards_html = ""
    for i, p in enumerate(antrian_list):
        is_front = (i == 0)
        bg    = "#e94560" if is_front else "#16213e"
        border= "#e94560" if is_front else "#2a2a4a"
        badge = "DEPAN ▶" if is_front else f"#{i+1}"
        gate_e = GATE_EMOJI.get(p["gate"], "🔲")
        cards_html += f"""
        <div style="
            background:{bg}; border:1.5px solid {border};
            border-radius:10px; padding:12px 18px;
            margin-bottom:8px; display:flex;
            align-items:center; justify-content:space-between;
        ">
            <div>
                <span style="
                    background:{'#fff3' if is_front else '#ffffff18'};
                    color:{'#fff' if is_front else '#8899bb'};
                    font-size:0.72rem; font-weight:700;
                    padding:2px 8px; border-radius:20px;
                    margin-right:10px;
                ">{badge}</span>
                <span style="color:#ffffff; font-size:1rem; font-weight:600;">
                    {p['nama']}
                </span>
            </div>
            <span style="color:{'#fff' if is_front else '#aaa'}; font-size:0.9rem;">
                {gate_e} {p['gate']}
            </span>
        </div>
        """
    st.markdown(cards_html, unsafe_allow_html=True)


def render_riwayat(riwayat: list):
    if not riwayat:
        return
    st.markdown("### 🏁 Riwayat Boarding")
    rows = "".join(
        f"<tr><td style='color:#aaa'>{i+1}</td>"
        f"<td style='color:#eee'>{p['nama']}</td>"
        f"<td style='color:#8bc34a'>{GATE_EMOJI.get(p['gate'],'')} {p['gate']}</td></tr>"
        for i, p in enumerate(reversed(riwayat[-10:]))
    )
    st.markdown(f"""
    <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
        <thead>
            <tr style="color:#e94560;border-bottom:1px solid #333">
                <th style="text-align:left;padding:6px">#</th>
                <th style="text-align:left;padding:6px">Nama</th>
                <th style="text-align:left;padding:6px">Gate</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  PENJELASAN KONSEP QUEUE
# ─────────────────────────────────────────────

def render_konsep():
    with st.expander("📚 Konsep Queue (FIFO) — Klik untuk baca", expanded=False):
        st.markdown("""
**Queue** adalah struktur data linear yang mengikuti prinsip **FIFO** *(First In, First Out)* —
elemen yang pertama masuk adalah yang pertama keluar, persis seperti antrian manusia di dunia nyata.

| Operasi | Keterangan | Kompleksitas |
|---------|-----------|-------------|
| `enqueue(x)` | Tambah elemen `x` ke **belakang** antrian | O(1) |
| `dequeue()` | Hapus & kembalikan elemen **paling depan** | O(1) |
| `peek()` | Lihat elemen depan **tanpa** menghapus | O(1) |
| `is_empty()` | Cek apakah antrian kosong | O(1) |
| `size()` | Jumlah elemen dalam antrian | O(1) |

```
ENQUEUE → [ Budi | Siti | Ahmad ] → DEQUEUE
              ▲ belakang    depan ▲
```

> 🐍 Dalam Python, `collections.deque` digunakan karena operasi `appendleft`/`popleft` adalah **O(1)**,
> lebih efisien dibanding `list` biasa yang membutuhkan O(n) untuk operasi di indeks 0.
        """)


# ─────────────────────────────────────────────
#  MAIN APP
# ─────────────────────────────────────────────

def main():
    st.set_page_config(
        page_title="Antrian Boarding Kereta",
        page_icon="🚆",
        layout="centered",
    )

    # CSS global — dark railway theme
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .stApp { background: #0d0d1a; }
    .block-container { padding-top: 1.5rem; max-width: 820px; }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 700;
        font-size: 0.95rem;
        padding: 10px 0;
        transition: all 0.2s ease;
        border: none;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px #0007; }

    div[data-testid="stTextInput"] input {
        background: #1a1a2e;
        color: #eee;
        border: 1.5px solid #2a2a4a;
        border-radius: 10px;
    }
    div[data-testid="stSelectbox"] > div {
        background: #1a1a2e;
        border-radius: 10px;
    }
    .stExpander { background: #13131f; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

    init_state()
    antrian: AntrianBoarding = st.session_state.antrian

    # ── Autoplay audio jika ada ──
    if st.session_state.audio_b64:
        autoplay_audio(st.session_state.audio_b64)
        st.session_state.audio_b64 = None

    render_header()

    # ── Statistik singkat ──
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("🧍 Dalam Antrian",  antrian.size())
    col_s2.metric("✅ Sudah Boarding", len(antrian.riwayat))
    front = antrian.peek()
    col_s3.metric("👤 Penumpang Depan", front["nama"] if front else "—")

    st.divider()

    # ── Panel Kontrol ──
    st.markdown("### ⚙️ Panel Kontrol")
    c1, c2 = st.columns([3, 2])
    with c1:
        nama_input = st.text_input("Nama Penumpang", placeholder="Contoh: Budi Santoso", label_visibility="visible")
    with c2:
        gate_pilih = st.selectbox("Pilih Gate", GATE_OPTIONS)

    b1, b2, b3 = st.columns(3)

    # ── ENQUEUE ──
    with b1:
        if st.button("➕ Tambah Antrian", use_container_width=True):
            if not nama_input.strip():
                st.session_state.pesan_info = {"tipe": "peringatan", "teks": "Nama penumpang tidak boleh kosong!"}
            else:
                antrian.enqueue(nama_input, gate_pilih)
                st.session_state.pesan_info = {
                    "tipe": "sukses",
                    "teks": f"{nama_input.strip().title()} berhasil ditambahkan ke antrian ({gate_pilih})."
                }
            st.session_state.peek_result = None
            st.rerun()

    # ── DEQUEUE ──
    with b2:
        if st.button("🎤 Panggil Penumpang", use_container_width=True):
            hasil = antrian.dequeue()
            if hasil is None:
                st.session_state.pesan_info = {"tipe": "peringatan", "teks": "Antrian sedang kosong!"}
            else:
                st.session_state.pesan_info = {
                    "tipe": "sukses",
                    "teks": f"✈️ {hasil['nama']} dipanggil → {hasil['gate']} | Proses audio pengumuman..."
                }
                try:
                    path_audio = buat_audio_pengumuman(hasil["nama"], hasil["gate"])
                    st.session_state.audio_b64 = audio_ke_base64(path_audio)
                except Exception:
                    pass   # audio gagal → tetap lanjut tanpa audio
            st.session_state.peek_result = None
            st.rerun()

    # ── PEEK ──
    with b3:
        if st.button("👀 Lihat Depan (Peek)", use_container_width=True):
            hasil_peek = antrian.peek()
            if hasil_peek is None:
                st.session_state.pesan_info = {"tipe": "info", "teks": "Antrian kosong, tidak ada penumpang di depan."}
            else:
                st.session_state.pesan_info = {
                    "tipe": "info",
                    "teks": f"Penumpang paling depan: {hasil_peek['nama']} → {hasil_peek['gate']} (tidak dihapus dari antrian)"
                }
            st.session_state.peek_result = hasil_peek
            st.rerun()

    st.divider()
    render_info_box()

    # ── Visualisasi Antrian ──
    render_antrian_visual(antrian.to_list())

    st.divider()
    render_riwayat(antrian.riwayat)
    render_konsep()


if __name__ == "__main__":
    main()