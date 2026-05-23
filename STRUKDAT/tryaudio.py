import streamlit as st
from collections import deque
from gtts import gTTS
import uuid
import os

# ─────────────────────────────────────
# CONFIG
# ─────────────────────────────────────
st.set_page_config(
    page_title="Sistem Boarding KAI",
    page_icon="🚂",
    layout="wide"
)

# ─────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────
if "queue_a" not in st.session_state:
    st.session_state.queue_a = deque()

if "queue_b" not in st.session_state:
    st.session_state.queue_b = deque()

if "counter" not in st.session_state:
    st.session_state.counter = 1

if "last_boarding" not in st.session_state:
    st.session_state.last_boarding = None

# ─────────────────────────────────────
# DATA KERETA
# ─────────────────────────────────────
KERETA = {
    "A": {
        "nama": "Argo Bromo Anggrek",
        "tujuan": "Surabaya Pasar Turi",
        "peron": "Peron 1",
        "berangkat": "08.00",
        "gerbong": [
            "Gerbong 1",
            "Gerbong 2",
            "Gerbong 3",
            "Eksekutif"
        ],
    },

    "B": {
        "nama": "Taksaka",
        "tujuan": "Yogyakarta",
        "peron": "Peron 2",
        "berangkat": "09.30",
        "gerbong": [
            "Gerbong 1",
            "Gerbong 2",
            "Gerbong 3",
            "Bisnis"
        ],
    },
}

KURSI = [
    f"{i}{h}"
    for i in range(1, 11)
    for h in ["A", "B", "C", "D"]
]

# ─────────────────────────────────────
# HELPER
# ─────────────────────────────────────
def buat_kode_tiket():
    return f"KAI-{uuid.uuid4().hex[:6].upper()}"

# ─────────────────────────────────────
# AUDIO FUNCTION
# ─────────────────────────────────────
def play_audio(teks):
    try:
        filename = f"{uuid.uuid4().hex}.mp3"

        tts = gTTS(
            text=teks,
            lang="id"
        )

        tts.save(filename)

        with open(filename, "rb") as f:
            audio_bytes = f.read()

        st.audio(
            audio_bytes,
            format="audio/mp3",
            autoplay=True
        )

        # hapus file setelah dipakai
        os.remove(filename)

    except Exception as e:
        st.error(f"⚠️ Audio gagal diputar: {e}")

# ─────────────────────────────────────
# AUDIO TEMPLATE
# ─────────────────────────────────────
def audio_scan_tiket(p):
    info = KERETA[p["kereta"]]

    teks = (
        f"Tiket valid. "
        f"Atas nama {p['nama']}. "
        f"Kereta {info['nama']} tujuan {info['tujuan']}. "
        f"{p['gerbong']}. "
        f"Kursi {p['kursi']}. "
        f"Silakan menuju {info['peron']}. "
        f"Terima kasih."
    )

    play_audio(teks)

def audio_boarding(p):
    info = KERETA[p["kereta"]]

    teks = (
        f"Perhatian. "
        f"Penumpang atas nama {p['nama']}. "
        f"Kereta {info['nama']} tujuan {info['tujuan']}. "
        f"{p['gerbong']}. "
        f"Kursi {p['kursi']}. "
        f"Silakan segera boarding melalui {info['peron']}. "
        f"Terima kasih."
    )

    play_audio(teks)

# ─────────────────────────────────────
# QUEUE FUNCTION
# ─────────────────────────────────────
def enqueue(nama, kereta, gerbong, kursi):

    penumpang = {
        "nomor": st.session_state.counter,
        "kode": buat_kode_tiket(),
        "nama": nama,
        "kereta": kereta,
        "gerbong": gerbong,
        "kursi": kursi,
        "tujuan": KERETA[kereta]["tujuan"],
    }

    if kereta == "A":
        st.session_state.queue_a.append(penumpang)
    else:
        st.session_state.queue_b.append(penumpang)

    st.session_state.counter += 1

    return penumpang

def dequeue(kereta):

    queue = (
        st.session_state.queue_a
        if kereta == "A"
        else st.session_state.queue_b
    )

    if queue:
        return queue.popleft()

    return None

def peek(kereta):

    queue = (
        st.session_state.queue_a
        if kereta == "A"
        else st.session_state.queue_b
    )

    return queue[0] if queue else None

def is_empty(kereta):

    queue = (
        st.session_state.queue_a
        if kereta == "A"
        else st.session_state.queue_b
    )

    return len(queue) == 0

# ─────────────────────────────────────
# HEADER
# ─────────────────────────────────────
st.title("🚂 Sistem Boarding KAI")
st.caption("Scan tiket → masuk antrian → boarding satu per satu")

st.divider()

# ─────────────────────────────────────
# DEPARTURE BOARD
# ─────────────────────────────────────
st.subheader("📋 Departure Board")

col1, col2 = st.columns(2)

for col, k in [(col1, "A"), (col2, "B")]:

    info = KERETA[k]

    queue = (
        st.session_state.queue_a
        if k == "A"
        else st.session_state.queue_b
    )

    with col:

        st.markdown(f"### 🚆 Kereta {k}")
        st.write(f"**Nama:** {info['nama']}")
        st.write(f"**Tujuan:** {info['tujuan']}")
        st.write(f"**Peron:** {info['peron']}")
        st.write(f"**Berangkat:** {info['berangkat']}")
        st.write(f"**Jumlah Antrian:** {len(queue)}")

st.divider()

# ─────────────────────────────────────
# FORM SCAN TIKET
# ─────────────────────────────────────
st.subheader("🎫 Scan Tiket")

with st.form("form_scan", clear_on_submit=True):

    nama = st.text_input("Nama Penumpang")

    col_a, col_b, col_c = st.columns(3)

    with col_a:

        kereta = st.selectbox(
            "Kereta",
            ["A", "B"],
            format_func=lambda x:
                f"Kereta {x} — {KERETA[x]['nama']}"
        )

    with col_b:

        gerbong = st.selectbox(
            "Gerbong",
            KERETA[kereta]["gerbong"]
        )

    with col_c:

        kursi = st.selectbox(
            "Kursi",
            KURSI
        )

    scan = st.form_submit_button(
        "🔍 Scan Tiket",
        use_container_width=True
    )

# ─────────────────────────────────────
# HANDLE SCAN
# ─────────────────────────────────────
if scan:

    if not nama.strip():

        st.error("❌ Nama penumpang tidak boleh kosong.")

    else:

        penumpang = enqueue(
            nama.strip(),
            kereta,
            gerbong,
            kursi
        )

        st.success(
            f"✅ Tiket valid!\n\n"
            f"👤 {penumpang['nama']}\n"
            f"🚆 Kereta {penumpang['kereta']}\n"
            f"🪑 {penumpang['gerbong']} | Kursi {penumpang['kursi']}"
        )

        st.code(
            penumpang["kode"],
            language="text"
        )

        # PLAY AUDIO
        audio_scan_tiket(penumpang)

st.divider()

# ─────────────────────────────────────
# GATE BOARDING
# ─────────────────────────────────────
st.subheader("🚪 Gate Boarding")

col_a, col_b = st.columns(2)

for col, k in [(col_a, "A"), (col_b, "B")]:

    info = KERETA[k]

    queue = (
        st.session_state.queue_a
        if k == "A"
        else st.session_state.queue_b
    )

    with col:

        st.markdown(f"### 🚉 Gate {k}")
        st.write(f"**{info['peron']}**")

        berikutnya = peek(k)

        # PEEK
        if berikutnya:

            st.info(
                f"👤 Berikutnya:\n\n"
                f"**{berikutnya['nama']}**\n"
                f"{berikutnya['gerbong']} | "
                f"Kursi {berikutnya['kursi']}"
            )

        else:

            st.warning("Antrian kosong.")

        # BOARDING BUTTON
        if st.button(
            f"▶ Panggil Boarding Kereta {k}",
            disabled=is_empty(k),
            use_container_width=True,
            key=f"btn_{k}"
        ):

            dipanggil = dequeue(k)

            st.session_state.last_boarding = dipanggil

            audio_boarding(dipanggil)

        st.write("### 📄 Daftar Antrian")

        # LIST QUEUE
        if queue:

            for i, p in enumerate(queue, start=1):

                st.write(
                    f"{i}. "
                    f"`{p['kode']}` — "
                    f"{p['nama']} | "
                    f"{p['gerbong']} | "
                    f"Kursi {p['kursi']}"
                )

        else:

            st.write("— kosong —")

st.divider()

# ─────────────────────────────────────
# LAST BOARDING
# ─────────────────────────────────────
if st.session_state.last_boarding:

    p = st.session_state.last_boarding

    info = KERETA[p["kereta"]]

    st.success(
        f"🟢 Baru boarding:\n\n"
        f"👤 {p['nama']}\n"
        f"🚆 Kereta {p['kereta']} — {info['nama']}\n"
        f"🪑 {p['gerbong']} | Kursi {p['kursi']}\n"
        f"🏁 {info['tujuan']}"
    )

# ─────────────────────────────────────
# RESET
# ─────────────────────────────────────
if st.button("🗑 Reset Semua", use_container_width=True):

    st.session_state.queue_a = deque()
    st.session_state.queue_b = deque()
    st.session_state.counter = 1
    st.session_state.last_boarding = None

    st.success("Data berhasil direset.")

    st.rerun()

# ─────────────────────────────────────
# FOOTER
# ─────────────────────────────────────
st.divider()

st.caption(
    "🚂 Sistem Boarding KAI | "
    "UAS Struktur Data | "
    "Farhan · Ummi · Naila · Fathiya"
)