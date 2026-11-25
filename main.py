import streamlit as st
from pekerja import bos_hayden

st.set_page_config(page_title="HAYDEN-PRO-VERSION")
st.title("🤖 HAYDEN-PRO-VERSION")
st.write("40 Pekerja + Gemini + Pengetahuan")

soalan = st.text_input("Tanya HAYDEN-PRO-VERSION:")
if st.button("Tanya"):
    if soalan:
        with st.spinner("Bos tengah panggil 40 pekerja..."):
            st.success(bos_hayden(soalan))
    else:
        st.warning("Taip dulu we.")
