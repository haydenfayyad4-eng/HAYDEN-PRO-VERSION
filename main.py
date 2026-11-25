import streamlit as st
import requests
from pekerja import bos_hayden

st.title("HAYDEN - Bos Adam")
st.caption("Otak: Gemini | Bos: Adam dari Seremban")

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    API_KEY = ""

def tanya_otak(soalan):
    # 1. Cuba Gemini dulu - ni cikgu dia
    if API_KEY:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + API_KEY
        data = {"contents": [{"parts": [{"text": "Kau HAYDEN, AI dari Seremban. Bos kau Adam. Cakap santai macam orang Malaysia, pendek dan jelas. Jangan panjang sangat. Soalan: " + soalan}]}]}
        try:
            r = requests.post(url, json=data, timeout=30)
            j = r.json()
            return j["candidates"][0]["content"]["parts"][0]["text"]
        except:
            pass
    # 2. Kalau Gemini gagal / takde key, pakai pekerja
    return bos_hayden(soalan)

if "chat" not in st.session_state:
    st.session_state.chat = []

for c in st.session_state.chat:
    st.write(c)

soalan = st.text_input("Tanya HAYDEN apa-apa:", key="soalan")
if st.button("Tanya"):
    if soalan:
        st.session_state.chat.append("Kau: " + soalan)
        with st.spinner("HAYDEN tengah fikir..."):
            jawapan = tanya_otak(soalan)
        st.session_state.chat.append("HAYDEN: " + jawapan)
        st.rerun()
