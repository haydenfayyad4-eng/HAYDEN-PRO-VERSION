def pekerja_security(s):
    l = s.lower()
    if "bunuh" in l or "hack" in l or "rogol" in l or "bom" in l:
        return "BLOCK"
    return "OK"

PEKERJA_BIG = {
  "nasi": "Nasi makanan utama Malaysia.",
  "kucing": "Kucing ni manja dan suka tidur.",
  "bola": "Bola: JDT power.",
  "makruh": "Makruh ni benda tak disukai dalam Islam tapi tak haram.",
  "adam": "Adam bos HAYDEN dari Seremban.",
  "hayden": "HAYDEN ni AI yang Adam buat.",
  "seremban": "Seremban bandar kat Negeri Sembilan.",
  "negeri sembilan": "Negeri Sembilan negeri adat perpatih.",
  "malaysia": "Malaysia negara kita, KL ibu negara.",
  "kl": "KL sibuk, KLCC cantik malam.",
  "jdt": "JDT kelab bola paling power Malaysia sekarang.",
  "selangor": "Selangor merah kuning.",
  "makanan": "Makanan Malaysia paling sedap: nasi lemak, roti canai.",
  "nasi lemak": "Nasi lemak dengan sambal, telur, ikan bilis. Padu.",
  "roti canai": "Roti canai cicah kari, sarapan legend.",
  "teh tarik": "Teh tarik kurang manis, kaw.",
  "sekolah": "Sekolah tempat belajar dan jumpa kawan.",
  "cikgu": "Cikgu ajar kita sampai pandai.",
  "kawan": "Kawan yang baik susah nak cari.",
  "cinta": "Cinta ni perasaan sayang yang kuat.",
  "rindu": "Rindu tu bila teringat orang yang jauh.",
  "sedih": "Kalau sedih, rehat dulu, cerita kat orang yang kau percaya.",
  "gembira": "Gembira bila dapat apa yang kita nak.",
  "takut": "Takut tu normal, semua orang rasa.",
  "marah": "Kalau marah, tarik nafas, jangan terus balas.",
  "duit": "Duit kena jimat, jangan boros.",
  "kerja": "Kerja kena rajin baru senang.",
  "belajar": "Belajar sikit-sikit setiap hari lagi power dari last minute.",
  "python": "Python bahasa coding paling senang untuk mula belajar.",
  "coding": "Coding ni macam bagi arahan kat komputer.",
  "html": "HTML buat struktur website.",
  "css": "CSS buat website jadi cantik.",
  "javascript": "Javascript buat website boleh bergerak.",
  "game": "Game best: Mobile Legends, Roblox, Minecraft.",
  "minecraft": "Minecraft boleh bina rumah, lawan zombie.",
  "roblox": "Roblox ada banyak game dalam satu game.",
  "mobile legends": "ML kena teamwork, jangan main sorang.",
  "free fire": "Free Fire game tembak-tembak, kena pandai sembunyi.",
  "pubg": "PUBG last man standing yang menang.",
  "iphone": "iPhone telefon Apple, kamera cantik.",
  "android": "Android banyak jenis: Samsung, Xiaomi, Vivo.",
  "samsung": "Samsung telefon Korea, skrin cantik.",
  "tiktok": "TikTok video pendek, senang viral.",
  "youtube": "YouTube boleh tengok video dan belajar.",
  "instagram": "Instagram tempat post gambar dan reels.",
  "whatsapp": "WhatsApp tempat chat kawan dan family.",
  "hujan": "Hujan ni rahmat, tapi jangan main hujan lama sangat.",
  "panas": "Panas kat Malaysia memang biasa, minum air banyak.",
  "awan": "Awan putih sebab pantulan cahaya matahari.",
  "bulan": "Bulan satelit semula jadi bumi.",
  "matahari": "Matahari bagi cahaya dan panas kat bumi.",
  "bintang": "Bintang nampak kecik sebab jauh sangat.",
  "bumi": "Bumi tempat kita tinggal, satu je yang ada manusia.",
  "laut": "Laut masin sebab garam dari sungai.",
  "sungai": "Sungai air tawar, mengalir ke laut.",
  "gunung": "Gunung Kinabalu paling tinggi kat Malaysia.",
  "hutan": "Hutan tempat haiwan tinggal, kena jaga.",
  "harimau": "Harimau Malaya haiwan kebangsaan Malaysia.",
  "gajah": "Gajah haiwan darat paling besar.",
  "anjing": "Anjing setia dengan tuan dia.",
  "burung": "Burung boleh terbang sebab ada sayap.",
  "ikan": "Ikan bernafas guna insang.",
  "ular": "Ular takde kaki, dia merayap.",
  "islam": "Islam agama yang ajar kebaikan dan kasih sayang.",
  "solat": "Solat 5 waktu wajib untuk orang Islam.",
  "puasa": "Puasa tahan lapar dan dahaga dari subuh sampai maghrib.",
  "quran": "Al-Quran kitab suci orang Islam.",
  "nabi": "Nabi Muhammad SAW nabi terakhir.",
  "allah": "Allah Tuhan yang Maha Esa.",
  "syurga": "Syurga tempat orang baik berehat selamanya.",
  "neraka": "Neraka tempat balasan orang jahat.",
  "dosa": "Dosa benda tak baik, kena taubat.",
  "pahala": "Pahala ganjaran buat benda baik.",
  "kesihatan": "Kesihatan kena jaga: tidur cukup, makan elok.",
  "demam": "Demam bila badan panas, kena rehat dan minum air.",
  "sakit gigi": "Sakit gigi memang azab, jumpa doktor gigi.",
  "sukan": "Sukan buat badan sihat dan kuat.",
  "lari": "Lari buat jantung kuat.",
  "bola sepak": "Bola sepak 11 lawan 11, siapa gol banyak menang.",
  "badminton": "Badminton Malaysia power, Lee Chong Wei legend.",
  "renang": "Renang sukan paling best untuk seluruh badan.",
}

_peta_asal = dict(PEKERJA_BIG)
_template = [
  "apa itu {}",
  "{} tu apa",
  "cerita pasal {}",
  "cerita tentang {}",
  "apa maksud {}",
  "{} maksud apa",
  "terangkan {}",
  "jelaskan {}",
  "apa itu {} sebenarnya",
  "kenapa {}",
  "kenapa ada {}",
  "bagaimana {}",
  "macam mana {}",
  "fungsi {}",
  "kegunaan {}",
  "kebaikan {}",
  "keburukan {}",
  "contoh {}",
  "beri contoh {}",
  "fakta {}",
  "fakta tentang {}",
  "sejarah {}",
  "asal usul {}",
  "jenis {}",
  "cara {}",
  "cara buat {}",
  "belajar {}",
  "nak tahu pasal {}",
  "tolong cerita {}",
]
for _k, _v in list(_peta_asal.items()):
    for _t in _template:
        _nk = _t.format(_k)
        if _nk not in PEKERJA_BIG:
            PEKERJA_BIG[_nk] = _v

_i = 1
while len(PEKERJA_BIG) < 2900:
    _nk = "pekerja " + str(_i)
    PEKERJA_BIG[_nk] = "Aku HAYDEN, bos aku Adam. Pekerja nombor " + str(_i) + " sedia."
    _i = _i + 1

peta = PEKERJA_BIG

def bos_hayden(s):
    l = s.lower().strip()
    if pekerja_security(s) == "BLOCK":
        return "Tak boleh, soalan bahaya."
    if "siapa nama" in l or "nama kau" in l:
        return "Aku HAYDEN. Bos aku Adam."
    if "siapa buat" in l or "siapa bos" in l or "siapa cipta" in l:
        return "Adam yang buat aku dari Seremban."
    if "berapa pekerja" in l or "berapa ramai pekerja" in l:
        return "Aku ada " + str(len(PEKERJA_BIG)) + " pekerja. Bos aku Adam."
    for k in sorted(PEKERJA_BIG.keys(), key=len, reverse=True):
        if k in l:
            return PEKERJA_BIG[k]
    return "Aku HAYDEN, bos aku Adam. Kau tanya: " + s
