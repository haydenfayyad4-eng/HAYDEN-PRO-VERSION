import requests, random, datetime, os
try:
    import streamlit as st
    GEMINI_KEY = st.secrets.get("GEMINI_API_KEY", "")
except:
    GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")

def pekerja_security(s):
    bahaya=["hack","curi","bunuh","password","bom","hack wifi"]
    for b in bahaya:
        if b in s.lower(): return "BLOCK"
    return "OK"

def pekerja_gemini(s):
    if not GEMINI_KEY: return "Gemini belum ON. Kena letak API Key kat Secrets dulu."
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        r = model.generate_content(f"Kau adalah HAYDEN-PRO-VERSION, jawab ringkas dan kelakar sikit, dalam Bahasa Melayu: {s}")
        return r.text
    except Exception as e: return f"Gemini error: {e}"

def pekerja_calculator(s):
    try:
        b="".join([c for c in s if c in "0123456789+-*/(). "])
        return f"Hasil = {eval(b)}"
    except: return "Taip macam: 5+5"

def pekerja_wikipedia(s):
    try:
        r=requests.get(f"https://ms.wikipedia.org/api/rest_v1/page/summary/{s}",timeout=5).json()
        return r.get("extract","Tak jumpa.")
    except: return "Wikipedia sibuk."
def pekerja_berita(s):
    try:
        d=requests.get("https://api.rss2json.com/v1/api.json?rss_url=https://www.bharian.com.my/rss",timeout=5).json()
        return "\n".join([f"- {x['title']}" for x in d.get("items",[])[:3]])
    except: return "Berita takleh load."
def pekerja_kamus(s):
    try:
        w=s.split()[-1]
        d=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{w}",timeout=5).json()
        return f"{w} = {d[0]['meanings'][0]['definitions'][0]['definition']}"
    except: return "Tak jumpa kamus."
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
def pekerja_kuiz(s): return "Kuiz: 7x8? A)54 B)56 C)64"
def pekerja_motivasi(s): return "Penat tu normal. Rehat jap, minum air, pastu sambung. Kau dah jauh dah."
def pekerja_lawak(s): return random.choice(["Kenapa komputer sejuk? Sebab banyak tingkap (Windows).","Kenapa ayam lintas jalan? Nak pergi seberang.","Apa beza kau dengan wifi? Wifi boleh connect, kau tak."])
def pekerja_cerita(s): return "Dulu ada budak nama Adam, dia buat AI nama HAYDEN-PRO-VERSION. Semua gelak, last-last AI dia lagi power."
def pekerja_cuaca(s):
    try:
        d=requests.get("https://api.open-meteo.com/v1/forecast?latitude=2.72&longitude=101.94&current=temperature_2m",timeout=5).json()
        return f"Seremban sekarang {d['current']['temperature_2m']}°C"
    except: return "Cuaca takleh load."
def pekerja_waktu_solat(s): return "Solat Seremban: Subuh 6:05, Zohor 1:20, Asar 4:40, Maghrib 7:20, Isyak 8:35. Check JAKIM untuk tepat."
def pekerja_duit(s):
    try:
        b="".join([c for c in s if c in "0123456789."])
        usd=float(b) if b else 1
        return f"RM{usd} = USD {usd*0.21:.2f} (anggaran)"
    except: return "Taip: 100 ringgit ke usd"
def pekerja_sains(s): return "Sains: Air H2O. Bumi pusing matahari. Graviti tarik kau jatuh."
def pekerja_sejarah(s): return "Sejarah: Hang Tuah pahlawan Melaka. Parameswara buka Melaka 1400."
def pekerja_geografi(s): return "Geografi: Malaysia 13 negeri. Gunung Kinabalu 4095m paling tinggi."
def pekerja_sukan(s): return "Sukan: Malaysia power badminton - Lee Chong Wei, Lee Zii Jia. Bola JDT tengah power."
def pekerja_masak(s): return "Resepi Maggi: Rebus air, masuk maggi, perencah, pecah telur. Siap 3 minit."
def pekerja_kesihatan(s): return "Tip sihat: Minum 8 gelas air, tidur 7 jam, jangan main phone sampai 3 pagi."
def pekerja_belajar(s): return "Tip belajar: 25 minit belajar, 5 minit rehat. Ulang. Jangan hafal last minit."
def pekerja_game(s): return "Game: Teka nombor aku 1-10. Taip nombor."
def pekerja_teka_teki(s): return "Teka-teki: Apa naik tapi tak pernah turun? Umur kau."
def pekerja_code(s): return "Code: print('Hello') untuk print. for i in range(5): untuk ulang."
def pekerja_nama(s): return "Nama best: HAYDEN, ADAM-X, NOVA, ZAYN."
def pekerja_lagu(s): return "Lagu: Naim Daniel - Sembah. Deep."
def pekerja_filem(s): return "Filem: Mechamato, Upin Ipin, Ejen Ali."
def pekerja_cinta(s): return "Fokus belajar dulu. Cinta boleh tunggu, SPM tak boleh tunggu."
def pekerja_doas(s): return "Doa belajar: Allahumma inni as'aluka fahmal nabiyyin."
def pekerja_jadual(s): return f"Hari ni {datetime.date.today()}. Pagi belajar, Petang main, Malam ulang kaji."
def pekerja_english(s): return "English: Cuba taip ayat Melayu, aku translate. Contoh: saya makan nasi = I eat rice."
def pekerja_malay(s): return "Bahasa Melayu: 'Saya' untuk formal, 'aku' untuk kawan rapat. Jangan guna aku dengan cikgu."
def pekerja_quran(s): return "Al-Fatihah adalah surah pembuka. Baca sebelum belajar, hati tenang."
def pekerja_matematik(s): return "Matematik: Formula luas bulatan = pi x r x r. Pi = 3.14"
def pekerja_sejarah_malaysia(s): return "Merdeka 31 Ogos 1957. Tunku Abdul Rahman bapa kemerdekaan."
def pekerja_bola(s): return "Bola: JDT, Selangor, Kedah. Malaysia pernah menang Piala AFF 2010."
def pekerja_tech(s): return "Tech: AI ni guna Python + Streamlit + Gemini. Kau pun boleh buat."
def pekerja_kewangan(s): return "Kewangan: Simpan RM1 sehari = RM365 setahun. Jangan habis duit kat jajan je."
def pekerja_emosi(s): return "Kalau sedih, cerita kat orang yang kau percaya. Jangan pendam sorang-sorang. Kau tak sorang."

def bos_hayden(s):
    if pekerja_security(s)=="BLOCK": return "⛔ Security block. Soalan bahaya."
    l=s.lower()
    if any(x in l for x in ["+","-","*","/","kira","tambah","darab"]): return f"🧮 [Calculator] {pekerja_calculator(s)}"
    if any(x in l for x in ["hukum","solat","puasa","haram","halal","islam"]): return f"🕌 [Hukum] {pekerja_hukum(s)}"
    if "berita" in l: return f"📰 [Berita] {pekerja_berita(s)}"
    if "maksud" in l or "kamus" in l: return f"📖 [Kamus] {pekerja_kamus(s)}"
    if "translate" in l: return f"🌐 [Translator] {pekerja_translator(s)}"
    if "kuiz" in l: return f"❓ [Kuiz] {pekerja_kuiz(s)}"
    if any(x in l for x in ["sedih","penat","stress"]): return f"💪 [Motivasi] {pekerja_motivasi(s)}"
    if "lawak" in l: return f"😂 [Lawak] {pekerja_lawak(s)}"
    if "cerita" in l: return f"📖 [Cerita] {pekerja_cerita(s)}"
    if "cuaca" in l: return f"🌦️ [Cuaca] {pekerja_cuaca(s)}"
    if "waktu solat" in l: return f"🕋 [Waktu Solat] {pekerja_waktu_solat(s)}"
    if "ringgit" in l or "usd" in l: return f"💰 [Duit] {pekerja_duit(s)}"
    if "sains" in l: return f"🔬 [Sains] {pekerja_sains(s)}"
    if "sejarah malaysia" in l or "merdeka" in l: return f"🇲🇾 [Sejarah Malaysia] {pekerja_sejarah_malaysia(s)}"
    if "sejarah" in l: return f"🏛️ [Sejarah] {pekerja_sejarah(s)}"
    if "geografi" in l: return f"🗺️ [Geografi] {pekerja_geografi(s)}"
    if "bola" in l: return f"⚽ [Bola] {pekerja_bola(s)}"
    if "sukan" in l: return f"⚽ [Sukan] {pekerja_sukan(s)}"
    if "masak" in l or "resepi" in l: return f"🍜 [Masak] {pekerja_masak(s)}"
    if "sihat" in l or "sakit" in l: return f"❤️ [Kesihatan] {pekerja_kesihatan(s)}"
    if "belajar" in l: return f"📚 [Belajar] {pekerja_belajar(s)}"
    if "game" in l: return f"🎮 [Game] {pekerja_game(s)}"
    if "teka" in l: return f"🧩 [Teka] {pekerja_teka_teki(s)}"
    if "code" in l or "python" in l: return f"💻 [Code] {pekerja_code(s)}"
    if "nama" in l: return f"✨ [Nama] {pekerja_nama(s)}"
    if "lagu" in l: return f"🎵 [Lagu] {pekerja_lagu(s)}"
    if "filem" in l: return f"🎬 [Filem] {pekerja_filem(s)}"
    if "cinta" in l or "crush" in l: return f"💔 [Cinta] {pekerja_cinta(s)}"
    if "doa" in l or "quran" in l: return f"🤲 [Quran/Doa] {pekerja_quran(s)}"
    if "jadual" in l: return f"📅 [Jadual] {pekerja_jadual(s)}"
    if "english" in l: return f"🇬🇧 [English] {pekerja_english(s)}"
    if "melayu" in l: return f"🇲🇾 [Melayu] {pekerja_malay(s)}"
    if "matematik" in l or "formula" in l: return f"📐 [Matematik] {pekerja_matematik(s)}"
    if "tech" in l or "ai" in l: return f"🤖 [Tech] {pekerja_tech(s)}"
    if "simpan" in l or "kewangan" in l: return f"💳 [Kewangan] {pekerja_kewangan(s)}"
    if "emosi" in l or "sedih sangat" in l: return f"❤️ [Emosi] {pekerja_emosi(s)}"
    if "wikipedia" in l: return f"📚 [Wikipedia] {pekerja_wikipedia(s)}"
    return f"✨ [Gemini] {pekerja_gemini(s)}"
