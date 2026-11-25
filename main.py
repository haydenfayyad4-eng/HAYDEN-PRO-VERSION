import streamlit as st
import requests
from google import genai

client = genai.client(api_key=st.secret["GEMINI_API_KEY"])
from pengetahuan import SUMBER_BELAJAR
# lepas tu bagi Hayden baca sumber tu sebelum jawab
import requests, random, datetime

def pekerja_security(s):
    bahaya = ["hack","curi","bunuh","password","bom","hack wifi"]
    for b in bahaya:
        if b in s.lower(): return "BLOCK"
    return "OK"

def pekerja_calculator(s):
    try:
        bersih = "".join([c for c in s if c in "0123456789+-*/(). "])
        return f"Hasil dia = {eval(bersih)}"
    except: return "Cuba taip macam: 5+5"

def pekerja_wikipedia(s):
    try:
        r = requests.get(f"https://ms.wikipedia.org/api/rest_v1/page/summary/{s}", timeout=5).json()
        return r.get("extract","Tak jumpa kat Wikipedia.")
    except: return "Wikipedia sibuk."

def pekerja_berita(s):
    try:
        d = requests.get("https://api.rss2json.com/v1/api.json?rss_url=https://www.bharian.com.my/rss", timeout=5).json()
        return "\n".join([f"- {x['title']}" for x in d.get("items",[])[:3]])
    except: return "Berita takleh load."

def pekerja_kamus(s):
    try:
        w = s.split()[-1]
        d = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{w}", timeout=5).json()
        return f"{w} = {d[0]['meanings'][0]['definitions'][0]['definition']}"
    except: return "Tak jumpa dalam kamus."

def pekerja_hukum(s):
    try:
        from pengetahuan import SUMBER_BELAJAR
        return f"{SUMBER_BELAJAR}\nSoalan: {s}"
    except: return "File pengetahuan.py tak jumpa."

def pekerja_translator(s):
    k={"saya":"I","kamu":"you","makan":"eat","minum":"drink","rumah":"house","sekolah":"school","cinta":"love","kawan":"friend","buku":"book","air":"water"}
    for bm,bi in k.items():
        if bm in s.lower(): return f"{bm} = {bi}"
    return "Perkataan tu aku belum belajar."

def pekerja_kuiz(s): return "Kuiz: 7x8? A)54 B)56 C)64 - Taip jawapan kau."
def pekerja_motivasi(s): return "Penat tu normal. Rehat jap, minum air, pastu sambung. Kau dah jauh dah."
def pekerja_lawak(s):
    l=["Kenapa komputer sejuk? Sebab dia banyak tingkap (Windows).","Kenapa ayam lintas jalan? Nak pergi seberang.","Apa beza kau dengan wifi? Wifi boleh connect, kau tak."] 
    return random.choice(l)
def pekerja_cerita(s): return "Dulu ada budak nama Adam, dia buat AI sendiri nama Hayden. Semua orang gelak, tapi last-last AI dia lagi power dari orang lain."
def pekerja_cuaca(s):
    try:
        d=requests.get("https://api.open-meteo.com/v1/forecast?latitude=2.72&longitude=101.94&current=temperature_2m",timeout=5).json()
        return f"Seremban sekarang {d['current']['temperature_2m']}°C"
    except: return "Cuaca takleh load."
def pekerja_waktu_solat(s): return "Waktu solat Seremban hari ni: Subuh 6:05, Zohor 1:20, Asar 4:40, Maghrib 7:20, Isyak 8:35. Check JAKIM untuk tepat."
def pekerja_duit(s):
    try:
        bersih="".join([c for c in s if c in "0123456789."])
        usd=float(bersih) if bersih else 1
        return f"RM{usd} lebih kurang USD {usd*0.21:.2f} (anggaran)"
    except: return "Taip macam: 100 ringgit ke usd"
def pekerja_sains(s): return "Sains: Air tu H2O. Bumi pusing matahari, bukan matahari pusing bumi. Graviti yang tarik kau jatuh."
def pekerja_sejarah(s): return "Sejarah: Hang Tuah pahlawan Melaka. Parameswara buka Melaka tahun 1400."
def pekerja_geografi(s): return "Geografi: Malaysia ada 13 negeri. Gunung Kinabalu paling tinggi, 4095m."
def pekerja_sukan(s): return "Sukan: Malaysia power kat badminton - Lee Chong Wei, Lee Zii Jia. Bola pulak JDT tengah power."
def pekerja_masak(s): return "Resepi Maggi: Rebus air, masuk maggi, masuk perencah, pecah telur. Siap 3 minit."
def pekerja_kesihatan(s): return "Tip sihat: Minum 8 gelas air sehari, tidur 7 jam, jangan main phone sampai 3 pagi."
def pekerja_belajar(s): return "Tip belajar: Buat 25 minit belajar, 5 minit rehat. Ulang. Jangan hafal last minit."
def pekerja_game(s): return "Game: Cuba teka nombor aku 1-10. Taip nombor kat bawah."
def pekerja_teka_teki(s): return "Teka-teki: Apa yang naik tapi tak pernah turun? Umur kau."
def pekerja_code(s): return "Code: Kalau nak print kat Python, taip print('Hello'). Kalau nak ulang, guna for i in range(5):"
def pekerja_nama(s): return "Nama best untuk AI kau: HAYDEN, ADAM-X, NOVA, ZAYN. Kau pilih mana?"
def pekerja_lagu(s): return "Lagu: Cuba dengar lagu Naim Daniel - Sembah. Lirik dia deep."
def pekerja_filem(s): return "Filem best: Mechamato, Upin Ipin, Ejen Ali. Semua Malaysia punya."
def pekerja_cinta(s): return "We, fokus belajar dulu. Cinta boleh tunggu, SPM tak boleh tunggu."
def pekerja_doas(s): return "Doa belajar: Allahumma inni as'aluka fahmal nabiyyin. Baca sebelum belajar."
def pekerja_jadual(s): return f"Hari ni {datetime.date.today()}. Buat jadual: Pagi belajar, Petang main, Malam ulang kaji."

def bos_hayden(s):
    if pekerja_security(s)=="BLOCK": return "⛔ Security block. Soalan bahaya."
    l=s.lower()
    if any(x in l for x in ["+","-","*","/","kira","tambah","darab"]): return f"🧮 [Calculator] {pekerja_calculator(s)}"
    if any(x in l for x in ["hukum","solat","puasa","haram","halal","islam"]): return f"🕌 [Hukum] {pekerja_hukum(s)}"
    if "berita" in l or "news" in l: return f"📰 [Berita] {pekerja_berita(s)}"
    if "maksud" in l or "kamus" in l: return f"📖 [Kamus] {pekerja_kamus(s)}"
    if "translate" in l or "english" in l: return f"🌐 [Translator] {pekerja_translator(s)}"
    if "kuiz" in l or "quiz" in l: return f"❓ [Kuiz] {pekerja_kuiz(s)}"
    if any(x in l for x in ["sedih","penat","stress","give up"]): return f"💪 [Motivasi] {pekerja_motivasi(s)}"
    if "lawak" in l or "joke" in l: return f"😂 [Lawak] {pekerja_lawak(s)}"
    if "cerita" in l: return f"📖 [Cerita] {pekerja_cerita(s)}"
    if "cuaca" in l or "panas" in l: return f"🌦️ [Cuaca] {pekerja_cuaca(s)}"
    if "waktu solat" in l or "azan" in l: return f"🕋 [Waktu Solat] {pekerja_waktu_solat(s)}"
    if "ringgit" in l or "usd" in l or "duit" in l: return f"💰 [Duit] {pekerja_duit(s)}"
    if "sains" in l: return f"🔬 [Sains] {pekerja_sains(s)}"
    if "sejarah" in l: return f"🏛️ [Sejarah] {pekerja_sejarah(s)}"
    if "geografi" in l or "negeri" in l: return f"🗺️ [Geografi] {pekerja_geografi(s)}"
    if "sukan" in l or "bola" in l or "badminton" in l: return f"⚽ [Sukan] {pekerja_sukan(s)}"
    if "masak" in l or "resepi" in l or "maggi" in l: return f"🍜 [Masak] {pekerja_masak(s)}"
    if "sihat" in l or "sakit" in l: return f"❤️ [Kesihatan] {pekerja_kesihatan(s)}"
    if "belajar" in l or "study" in l: return f"📚 [Belajar] {pekerja_belajar(s)}"
    if "game" in l or "main" in l: return f"🎮 [Game] {pekerja_game(s)}"
    if "teka" in l: return f"🧩 [Teka-Teki] {pekerja_teka_teki(s)}"
    if "code" in l or "python" in l: return f"💻 [Code] {pekerja_code(s)}"
    if "nama" in l: return f"✨ [Nama] {pekerja_nama(s)}"
    if "lagu" in l: return f"🎵 [Lagu] {pekerja_lagu(s)}"
    if "filem" in l or "movie" in l: return f"🎬 [Filem] {pekerja_filem(s)}"
    if "cinta" in l or "crush" in l: return f"💔 [Cinta] {pekerja_cinta(s)}"
    if "doa" in l: return f"🤲 [Doa] {pekerja_doas(s)}"
    if "jadual" in l or "hari ni" in l: return f"📅 [Jadual] {pekerja_jadual(s)}"
    return f"📚 [Wikipedia] {pekerja_wikipedia(s)}"
