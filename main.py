import streamlit as st
from pekerja import bos_hayden

st.set_page_config(page_title="HAYDEN-PRO-VERSION", layout="centered")

st.markdown("""
<style>
.stApp { background: #0e1117; }
h1 { font-size: 22px !important; text-align: center; color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 HAYDEN-PRO-VERSION")

if "chat" not in st.session_state:
    st.session_state.chat = [{"role":"assistant","content":"Hai, aku HAYDEN-PRO-VERSION. Aku ada 40 pekerja + Gemini. Tanya la apa-apa."}]

for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.write(m["content"])

soalan = st.chat_input("Tanya HAYDEN...")
if soalan:
    st.session_state.chat.append({"role":"user","content":soalan})
    with st.chat_message("user"):
        st.write(soalan)
    with st.chat_message("assistant"):
        with st.spinner("..."):
            jawapan = bos_hayden(soalan)
            st.write(jawapan)
    st.session_state.chat.append({"role":"assistant","content":jawapan})
