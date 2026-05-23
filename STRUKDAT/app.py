import streamlit as st
from collections import deque
from gtts import gTTS
import base64, uuid

st.set_page_config(page_title="🚂 KAI Boarding", layout="centered")

# ── DATA ──
KERETA = {
    "A": {"nama": "Argo Bromo", "tujuan": "Surabaya", "peron": "Peron 1", "jam": "08.00"},
    "B": {"nama": "Taksaka",    "tujuan": "Yogyakarta","peron": "Peron 2", "jam": "09.30"},
}

# ── SESSION STATE ──
for k in ["queue_a","queue_b","counter","last"]:
    if k not in st.session_state:
        st.session_state[k] = deque() if k.startswith("queue") else (1 if k=="counter" else None)

# ── AUDIO ──
def play(teks):
    try:
        f = f"/tmp/{uuid.uuid4().hex}.mp3"
        gTTS(teks, lang="id").save(f)
        b64 = base64.b64encode(open(f,"rb").read()).decode()
        # pakai st.audio agar kompatibel di semua browser
        st.audio(f"data:audio/mp3;base64,{b64}", format="audio/mp3", autoplay=True)
    except:
        st.toast("⚠️ Audio gagal — cek koneksi internet.")

# ── QUEUE OPS ──
def enqueue(nama, kereta, gerbong, kursi):
    p = {"no": st.session_state.counter, "nama": nama,
         "kereta": kereta, "gerbong": gerbong, "kursi": kursi,
         "tujuan": KERETA[kereta]["tujuan"]}
    (st.session_state.queue_a if kereta=="A" else st.session_state.queue_b).append(p)
    st.session_state.counter += 1
    return p

def dequeue(k):
    q = st.session_state.queue_a if k=="A" else st.session_state.queue_b
    return q.popleft() if q else None

def peek(k):
    q = st.session_state.queue_a if k=="A" else st.session_state.queue_b
    return q[0] if q else None

def qlen(k):
    return len(st.session_state.queue_a if k=="A" else st.session_state.queue_b)

# ── UI ──
st.title("🚂 KAI — Sistem Boarding")
st.divider()

# Departure board
c1, c2 = st.columns(2)
for col, k in [(c1,"A"),(c2,"B")]:
    i = KERETA[k]
    col.metric(f"Kereta {k} · {i['nama']}", i['tujuan'], f"🕐 {i['jam']} · {i['peron']} · {qlen(k)} antri")

st.divider()

# Scan tiket (enqueue)
st.subheader("🎫 Scan Tiket")
with st.form("f", clear_on_submit=True):
    nama    = st.text_input("Nama Penumpang")
    c1,c2,c3 = st.columns(3)
    kereta  = c1.selectbox("Kereta", ["A","B"], format_func=lambda x: f"Kereta {x}")
    gerbong = c2.selectbox("Gerbong", ["Gerbong 1","Gerbong 2","Gerbong 3","Eksekutif"])
    kursi   = c3.selectbox("Kursi", [f"{i}{h}" for i in range(1,9) for h in "ABCD"])
    ok      = st.form_submit_button("✅ Scan & Masuk Antrian", use_container_width=True)

if ok:
    if not nama.strip():
        st.error("Nama tidak boleh kosong.")
    else:
        p = enqueue(nama.strip(), kereta, gerbong, kursi)
        info = KERETA[kereta]
        play(f"Tiket valid. Atas nama {p['nama']}, kereta {info['nama']} tujuan {info['tujuan']}, "
             f"{gerbong}, kursi {kursi}. Silakan menuju {info['peron']}.")
        st.success(f"#{p['no']:03d} {p['nama']} → Kereta {kereta} | {gerbong} | Kursi {kursi}")
        st.rerun()

st.divider()

# Gate boarding (dequeue + peek)
st.subheader("🚪 Gate Boarding")
c1, c2 = st.columns(2)
for col, k in [(c1,"A"),(c2,"B")]:
    info = KERETA[k]
    q = st.session_state.queue_a if k=="A" else st.session_state.queue_b
    with col:
        st.write(f"**Gate {k} — {info['peron']}**")
        nx = peek(k)
        st.info(f"👤 Berikutnya: **{nx['nama']}** | {nx['gerbong']} {nx['kursi']}" if nx else "Antrian kosong.")
        if st.button(f"▶ Boarding Kereta {k}", disabled=not nx, use_container_width=True, key=k):
            p = dequeue(k)
            st.session_state.last = p
            play(f"Perhatian. {p['nama']}, kereta {info['nama']} tujuan {info['tujuan']}, "
                 f"{p['gerbong']}, kursi {p['kursi']}, silakan boarding {info['peron']}.")
            st.rerun()
        for i,p in enumerate(q):
            st.write(f"`{i+1}` #{p['no']:03d} {p['nama']} · {p['gerbong']} · {p['kursi']}")

# Last boarding
if st.session_state.last:
    p = st.session_state.last
    st.success(f"🟢 Boarding: **{p['nama']}** | Kereta {p['kereta']} | {p['gerbong']} | {p['kursi']} | {p['tujuan']}")

st.divider()
if st.button("🗑 Reset"):
    for k in ["queue_a","queue_b","last"]:
        st.session_state[k] = deque() if k.startswith("queue") else None
    st.session_state.counter = 1
    st.rerun()

st.caption("🚂 KAI Boarding System · UAS Struktur Data · Farhan · Ummi · Naila · Fathiya")