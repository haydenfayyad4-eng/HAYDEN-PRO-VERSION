import json
import os

def pekerja_security(s):
    l = s.lower()
    if "bunuh" in l or "hack" in l or "rogol" in l or "bom" in l:
        return "BLOCK"
    return "OK"

PEKERJA_BIG = {
  "hi": "Hi! Aku HAYDEN. Bos aku Adam. Kau nak tanya apa?",
  "hai": "Hai! Aku HAYDEN. Bos aku Adam.",
  "hello": "Hello! Aku HAYDEN. Bos aku Adam.",
  "sapa kau": "Aku HAYDEN, bos aku Adam dari Seremban.",
  "kau siapa": "Aku HAYDEN, bos aku Adam dari Seremban.",
  "siapa nama": "Aku HAYDEN. Bos aku Adam.",
  "nama kau": "Aku HAYDEN. Bos aku Adam.",
  "siapa buat": "Adam yang buat aku dari Seremban.",
  "siapa bos": "Bos aku Adam dari Seremban.",
  "siapa cipta": "Adam yang cipta aku.",
  "berapa pekerja": "Aku ada 3000 pekerja asas + aku boleh belajar sendiri dari chat kau.",
  "nasi": "Nasi makanan utama Malaysia.",
  "kucing": "Kucing ni manja dan suka tidur.",
  "bola": "Bola: JDT power.",
  "makruh": "Makruh ni benda tak disukai dalam Islam tapi tak haram.",
  "adam": "Adam bos HAYDEN dari Seremban.",
  "hayden": "HAYDEN ni AI yang Adam buat, boleh belajar sendiri.",
  "seremban": "Seremban bandar kat Negeri Sembilan.",
  "malaysia": "Malaysia negara kita, KL ibu negara.",
  "makanan": "Makanan Malaysia paling sedap: nasi lemak, roti canai.",
  "nasi lemak": "Nasi lemak dengan sambal, telur, ikan bilis. Padu.",
  "roti canai": "Roti canai cicah kari, sarapan legend.",
  "teh tarik": "Teh tarik kurang manis, kaw.",
  "sekolah": "Sekolah tempat belajar dan jumpa kawan.",
  "cinta": "Cinta ni perasaan sayang yang kuat.",
  "rindu": "Rindu tu bila teringat orang yang jauh.",
  "sedih": "Kalau sedih, rehat dulu, cerita kat orang yang kau percaya.",
  "duit": "Duit kena jimat, jangan boros.",
  "belajar": "Belajar sikit-sikit setiap hari lagi power dari last minute.",
  "python": "Python bahasa coding paling senang untuk mula belajar.",
  "coding": "Coding ni macam bagi arahan kat komputer.",
  "game": "Game best: Mobile Legends, Roblox, Minecraft.",
  "minecraft": "Minecraft boleh bina rumah, lawan zombie.",
  "roblox": "Roblox ada banyak game dalam satu game.",
  "tiktok": "TikTok video pendek, senang viral.",
  "youtube": "YouTube boleh tengok video dan belajar.",
  "hujan": "Hujan ni rahmat, tapi jangan main hujan lama sangat.",
  "bumi": "Bumi tempat kita tinggal, satu je yang ada manusia.",
  "islam": "Islam agama yang ajar kebaikan dan kasih sayang.",
  "solat": "Solat 5 waktu wajib untuk orang Islam.",
  "puasa": "Puasa tahan lapar dan dahaga dari subuh sampai maghrib.",
}

_peta_asal = dict(PEKERJA_BIG)
_template = ["apa itu {}", "{} tu apa", "cerita pasal {}", "apa maksud {}", "terangkan {}", "kenapa {}", "macam mana {}", "fakta {}", "cara {}", "belajar {}"]
for _k, _v in list(_peta_asal.items()):
    for _t in _template:
        _nk = _t.format(_k)
        if _nk not in PEKERJA_BIG:
            PEKERJA_BIG[_nk] = _v

_i = 1
while len(PEKERJA_BIG) < 3000:
    _nk = "pekerja " + str(_i)
    PEKERJA_BIG[_nk] = "Aku HAYDEN, bos aku Adam. Pekerja nombor " + str(_i) + " sedia."
    _i = _i + 1

peta = PEKERJA_BIG

# --- BELAJAR SENDIRI ---
FAIL_BELAJAR = "hayden_belajar.json"

def load_belajar():
    try:
        if os.path.exists(FAIL_BELAJAR):
            with open(FAIL_BELAJAR, "r", encoding="utf-8") as f:
                return json.load(f)
    except:
        pass
    return {}

def simpan_belajar(soalan, jawapan):
    data = load_belajar()
    data[soalan.lower().strip()] = jawapan
    try:
        with open(FAIL_BELAJAR, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except:
        password 
        
        def bos_hayden(s):
    l = s.lower().strip()
    if "siapa nama" in l or "nama kau" in l:
        return "Aku HAYDEN. Bos aku Adam."
    if "siapa buat" in l or "siapa bos" in l:
        return "Adam yang buat aku dari Seremban."
    for k in sorted(PEKERJA_BIG.keys(), key=len, reverse=True):
        if k in l:
            return PEKERJA_BIG[k]
    return "Aku HAYDEN, bos aku Adam. Kau tanya: " + s
