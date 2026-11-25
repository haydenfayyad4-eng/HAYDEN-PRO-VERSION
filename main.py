import streamlit as st
import requests
from google import genai

client = genai.client(api_key=st.secret["GEMINI_API_KEY"])
from pengetahuan import SUMBER_BELAJAR
# lepas tu bagi Hayden baca sumber tu sebelum jawab
