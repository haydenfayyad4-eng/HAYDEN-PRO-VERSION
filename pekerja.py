import os
import random

def pekerja_security(s):
    l = s.lower()
    for b in ["hack", "curi password", "buat bom", "bunuh", "hack akaun", "tipu"]:
        if b in l:
            return "BLOCK"
    return "OK"

# --- 100 PEKERJA, CODING SAMA JE, 1 PEKERJA = 1 TOPIK ---
def pekerja_calculator(s): return "Kau taip je: 12+8 atau 20*5. Kalau susah, taip 'kira 25 bahagi 5'."
def pekerja_hukum(s): return "Hukum asas: Solat 5 waktu wajib, puasa Ramadhan wajib. Kalau hukum detail, tanya ustaz tau."
def pekerja_berita(s): return "Berita hari ni: Malaysia tengah sibuk dengan sukan, cuaca, dan ekonomi. Nak berita apa specifically?"
def pekerja_kamus(s): return "Kau nak maksud perkataan apa? Taip 'maksud gembira' contohnya."
def pekerja_translator(s): return "Nak translate apa? Taip 'translate saya lapar'."
def pekerja_kuiz(s): return "Kuiz: Ibu negara Malaysia apa? A) KL B) Penang C) Johor. Jawab A!"
def pekerja_motivasi(s): return "Penat tu biasa. Rehat 5 minit, minum air, sambung balik. Adam pun penat buat aku ni, tapi dia tak give up."
def pekerja_lawak(s): return "Kenapa komputer sejuk? Sebab dia banyak tingkap (Windows) 😂"
def pekerja_cerita(s): return "Dulu ada budak nama Adam, dia buat robot nama HAYDEN. Robot tu pandai jawab 100 benda."
def pekerja_cuaca(s): return "Cuaca Seremban: Pagi panas, petang selalu hujan. Standby payung."
def pekerja_waktu_solat(s): return "Waktu solat Seremban: Subuh 6:00, Zohor 1:15, Asar 4:30, Maghrib 7:15, Isyak 8:30."
def pekerja_duit(s): return "1 USD lebih kurang RM4.70. Nak tukar berapa? Taip '100 USD ke RM'."
def pekerja_sains(s): return "Sains: Air tu H2O, bumi pusing matahari 365 hari, manusia perlukan oksigen."
def pekerja_sejarah_malaysia(s): return "Malaysia merdeka 31 Ogos 1957. Tunku Abdul Rahman bapa kemerdekaan."
def pekerja_sejarah(s): return "Sejarah ni cerita lama. Kau nak sejarah Malaysia ke dunia? Taip 'sejarah Malaysia'."
def pekerja_geografi(s): return "Geografi: Malaysia ada Semenanjung + Sabah Sarawak. Gunung tertinggi Kinabalu."
def pekerja_bola(s): return "Bola: JDT power kat Malaysia, tapi EPL pun sengit. Kau sokong team apa?"
def pekerja_sukan(s): return "Sukan sihatkan badan. Jogging 30 minit sehari dah cukup."
def pekerja_masak(s): return "Resepi senang: Nasi goreng - nasi, telur, kicap, bawang. Goreng 5 minit siap."
def pekerja_kesihatan(s): return "Jaga kesihatan: Minum air banyak, tidur cukup. Kalau sakit teruk jumpa doktor ya."
def pekerja_belajar(s): return "Cara belajar power: Baca 25 minit, rehat 5 minit, ulang. Jangan hafal, fahamkan."
def pekerja_game(s): return "Game apa kau main? ML ke Roblox? Aku takleh main, aku cuma AI."
def pekerja_teka_teki(s): return "Teka teki: Apa yang naik tapi tak pernah turun? Umur!"
def pekerja_code(s): return "Nak code apa? Taip 'code python kira umur'."
def pekerja_nama(s): return "Nama best: HAYDEN, ADAM-X, NOVA, ZAYN, AINA, SARA, RAYYAN."
def pekerja_lagu(s): return "Lagu best: Cuba dengar Naim Daniel - Sumpah, atau Insomniacks."
def pekerja_filem(s): return "Filem best: Mechamato, Ejen Ali The Movie, Polis Evo."
def pekerja_cinta(s): return "Crush tu biasa. Fokus belajar dulu, cinta datang kemudian."
def pekerja_quran(s): return "Doa belajar: Allahummaftah alaina. Semoga dipermudahkan urusan kau."
def pekerja_jadual(s): return "Jadual elok: Pagi belajar, petang main, malam rehat. Jangan main phone sampai 2 pagi."
def pekerja_english(s): return "English: 'I am happy' = 'Saya gembira'. Nak belajar perkataan apa?"
def pekerja_malay(s): return "Melayu: 'Gembira' = happy. Bahasa Melayu kita ni cantik."
def pekerja_matematik(s): return "Matematik: Luas segi empat = panjang x lebar. Nak kira apa?"
def pekerja_tech(s): return "AI ni macam aku, HAYDEN. Adam yang buat aku guna Streamlit + Gemini."
def pekerja_kewangan(s): return "Simpan duit: Dapat RM10, simpan RM2, belanja RM8. Jangan habis semua."
def pekerja_emosi(s): return "Kalau sedih, cerita kat orang yang kau percaya. Jangan pendam sorang-sorang."
def pekerja_wikipedia(s): return "Wikipedia: Taip 'wikipedia Malaysia' nanti aku cerita ringkas."
def pekerja_gemini(s): return "Aku HAYDEN. Kau tanya apa-apa je, aku jawab. Kalau soalan susah sangat, aku guna otak Gemini."
def pekerja_agama(s): return "Agama ajar kita jadi baik: hormat mak ayah, jujur, tolong orang."
def pekerja_adab(s): return "Adab: Cakap elok-elok, jangan maki, hormat orang tua, ucap terima kasih."
def pekerja_keluarga(s): return "Keluarga paling penting. Tolong mak ayah kat rumah, jangan lawan cakap."
def pekerja_ibu(s): return "Ibu penat besarkan kita. Tolong dia, peluk dia, ucap terima kasih kat dia."
def pekerja_ayah(s): return "Ayah kerja keras untuk keluarga. Hormat dia, jangan buat dia risau."
def pekerja_guru(s): return "Guru ajar kita ilmu. Hormat cikgu, dengar cakap cikgu kat sekolah."
def pekerja_sekolah(s): return "Sekolah tempat belajar + kawan. Pergi sekolah rajin-rajin, jangan ponteng."
def pekerja_exam(s): return "Tips exam: Tidur awal, baca soalan betul-betul, jangan panik, jawab yang senang dulu."
def pekerja_spm(s): return "SPM ni penting tapi bukan penamat. Buat yang terbaik, jangan stress sangat."
def pekerja_biologi(s): return "Biologi: Manusia ada jantung, paru-paru, otak. Tumbuhan buat fotosintesis."
def pekerja_kimia(s): return "Kimia: Air H2O, garam NaCl, oksigen O2. Jangan main bahan kimia bahaya."
def pekerja_fizik(s): return "Fizik: Graviti tarik benda ke bawah. Tu sebab kita tak terbang."
def pekerja_addmath(s): return "Addmath: Jangan takut formula. Faham konsep, banyakkan latihan."
def pekerja_bm(s): return "BM: Karangan kena ada pendahuluan, isi, penutup. Guna ayat cantik."
def pekerja_ekonomi(s): return "Ekonomi: Harga naik sebab permintaan tinggi. Kena pandai urus duit."
def pekerja_kerjaya(s): return "Kerjaya best: Doktor, cikgu, engineer, polis, programmer. Kau nak jadi apa?"
def pekerja_cita_cita(s): return "Cita-cita kau apa? Kejar betul-betul. Adam cita-cita dia nak buat AI macam aku."
def pekerja_doktor(s): return "Doktor tolong orang sakit. Nak jadi doktor kena belajar rajin, especially sains."
def pekerja_engineer(s): return "Engineer buat bangunan, robot, app. Macam Adam buat aku ni."
def pekerja_polis(s): return "Polis jaga keamanan. Kalau emergency call 999."
def pekerja_pilot(s): return "Pilot bawa kapal terbang. Kena pandai Matematik + English, mata pun kena bagus."
def pekerja_youtuber(s): return "Youtuber: Kena rajin buat content, tapi jangan buat content bodoh."
def pekerja_komputer(s): return "Komputer: Ada CPU, RAM, storage. Macam otak, ingatan, dan almari."
def pekerja_internet(s): return "Internet ni best tapi bahaya. Jangan share password, jangan percaya semua benda kat internet."
def pekerja_phone(s): return "Phone: Guna untuk belajar, jangan main game 10 jam. Mata rosak nanti."
def pekerja_robot(s): return "Robot macam aku, HAYDEN. Robot ikut arahan manusia, tapi AI boleh belajar sendiri."
def pekerja_angkasa(s): return "Angkasa: Ada planet, bintang, bulan. Manusia dah sampai bulan tahun 1969."
def pekerja_bumi(s): return "Bumi ni satu-satunya planet ada manusia. Jaga bumi, jangan buang sampah merata."
def pekerja_bulan(s): return "Bulan pusing bumi. Bulan takde cahaya sendiri, dia pantul cahaya matahari."
def pekerja_matahari(s): return "Matahari bagi cahaya + haba kat bumi. Jangan tengok matahari direct, sakit mata."
def pekerja_haiwan(s): return "Haiwan: Kucing, anjing, burung semua makhluk Allah. Jangan dera haiwan."
def pekerja_kucing(s): return "Kucing ni manja. Bagi makan, bagi air, jangan tarik ekor dia."
def pekerja_anjing(s): return "Anjing setia. Kalau anjing orang, jangan kacau, takut dia gigit."
def pekerja_burung(s): return "Burung boleh terbang sebab ada sayap + tulang ringan."
def pekerja_ikan(s): return "Ikan hidup dalam air, bernafas guna insang. Jangan bagi ikan makan banyak sangat."
def pekerja_pokok(s): return "Pokok bagi oksigen. Tanam pokok, bumi jadi sejuk."
def pekerja_bunga(s): return "Bunga cantik: Ros, matahari, orkid. Bunga perlukan air + matahari."
def pekerja_makanan(s): return "Makanan sihat: Nasi, sayur, ayam, buah. Kurangkan jajan."
def pekerja_minuman(s): return "Minuman best: Air kosong paling sihat. Air manis tu sedap tapi tak sihat."
def pekerja_buah(s): return "Buah: Durian raja buah, manggis ratu buah. Kau suka buah apa?"
def pekerja_sayur(s): return "Sayur: Bayam bagi kuat, carrot bagi mata terang. Jangan picky makan sayur."
def pekerja_badminton(s): return "Badminton: Lee Chong Wei legend Malaysia. Main badminton bagus untuk stamina."
def pekerja_berenang(s): return "Berenang: Best untuk badan, tapi jangan berenang sorang, bahaya."
def pekerja_basikal(s): return "Basikal: Kayuh slow-slow, pakai helmet. Jangan main kat jalan besar."
def pekerja_lari(s): return "Lari: Panaskan badan dulu, jangan terus pecut. Nanti cramp."
def pekerja_gym(s): return "Gym: Angkat berat ikut kemampuan, jangan ikut orang. Rehat cukup."
def pekerja_tidur(s): return "Tidur: Budak kena tidur 8-9 jam. Jangan main phone sampai 3 pagi."
def pekerja_mimpi(s): return "Mimpi tu otak kita tengah susun memori. Mimpi pelik tu normal."
def pekerja_hantu(s): return "Hantu ni cerita je, jangan takut sangat. Kalau takut, baca doa, tidur awal."
def pekerja_superhero(s): return "Superhero: Mechamato, Ejen Ali, Boboiboy. Kau suka siapa?"
def pekerja_anime(s): return "Anime: Naruto, One Piece, Doraemon. Jangan tengok sampai lupa homework."
def pekerja_kartun(s): return "Kartun: Upin Ipin, Boboiboy. Kartun Malaysia pun power."
def pekerja_komik(s): return "Komik: Lawak Kampus, Gempak. Baca komik pun boleh belajar bahasa."
def pekerja_novel(s): return "Novel: Baca novel bagus untuk imaginasi. Cuba baca novel Melayu."
def pekerja_puisi(s): return "Puisi: Puisi ni ayat cantik, pendek tapi dalam maksud dia."
def pekerja_pantun(s): return "Pantun: Dua kerat dua kerat, pergi kedai beli roti. Belajar rajin-rajat, nanti dapat A nanti."
def pekerja_peribahasa(s): return "Peribahasa: 'Bagai aur dengan tebing' maksudnya tolong-menolong."
def pekerja_kawan(s): return "Kawan baik: Yang tolong masa susah, bukan yang ajak buat jahat."
def pekerja_buli(s): return "Buli tu jahat. Kalau kena buli, bagitau cikgu / mak ayah, jangan diam."
def pekerja_duit_raya(s): return "Duit raya: Simpan sikit, jangan habis beli jajan semua."
def pekerja_hari_raya(s): return "Hari Raya: Maaf zahir batin, makan ketupat rendang, ziarah saudara."
def pekerja_merdeka(s): return "Merdeka: 31 Ogos 1957. Kita kena hargai kemerdekaan ni."
def pekerja_covid(s): return "Covid dah kurang, tapi jaga kebersihan. Basuh tangan selalu."
# === 2000 PEKERJA ADAM - COPY DARI SINI ===
PEKERJA_BIG = {
  "makruh": "Makruh ni benda tak disukai dalam Islam. Buat tak berdosa, tinggal dapat pahala.",
  "wajib": "Wajib ni mesti buat. Tinggal berdosa. Contoh: solat 5 waktu, puasa Ramadhan.",
  "sunat": "Sunat ni buat dapat pahala, tinggal tak berdosa. Contoh: puasa Isnin Khamis.",
  "haram": "Haram ni jangan buat langsung. Kalau buat berdosa.",
  "halal": "Halal ni dibenarkan dalam Islam.",
  "najis": "Najis ni kotor. Kena basuh sampai bersih sebelum solat.",
  "wuduk": "Wuduk: Niat, basuh muka, tangan, sapu kepala, basuh kaki.",
  "zakat": "Zakat ni tolong orang susah. Orang kaya wajib bayar zakat.",
  "sedekah": "Sedekah ni bagi sikit pun pahala besar. Senyum pun sedekah.",
  "puasa": "Puasa Ramadhan wajib. Puasa Isnin Khamis sunat.",
  "solat": "Solat 5 waktu wajib: Subuh, Zohor, Asar, Maghrib, Isyak.",
  "doa": "Doa belajar: Allahummaftah alaina. Semoga dipermudahkan.",
  "quran": "Quran kitab suci umat Islam. Baca Quran dapat pahala.",
  "surah": "Surah pertama Al-Fatihah. Surah last An-Nas.",
  "nabi": "Nabi Muhammad SAW nabi terakhir.",
  "islam": "Islam ajar kita jadi baik: jujur, hormat mak ayah.",
  "syurga": "Syurga tempat orang baik.",
  "neraka": "Neraka tempat orang jahat. Jangan buat dosa.",
  "dosa": "Dosa ni benda jahat. Kalau buat dosa, cepat-cepat taubat.",
  "pahala": "Pahala ni ganjaran buat baik.",
  "syukur": "Syukur ni ucap Alhamdulillah bila dapat nikmat.",
  "sabar": "Sabar ni tahan bila susah. Allah suka orang sabar.",
  "taubat": "Taubat ni minta ampun kat Allah.",
  "iman": "Iman ni percaya kat Allah, malaikat, kitab, nabi, hari kiamat.",
  "malaikat": "Malaikat buat kerja Allah. Jibril bawa wahyu.",
  "kiamat": "Hari Kiamat hari semua manusia dibangkitkan semula.",
  "haji": "Haji rukun Islam ke-5. Pergi Mekah kalau mampu.",
  "umrah": "Umrah ni ziarah Mekah. Macam haji kecik.",
  "masjid": "Masjid tempat solat. Jaga kebersihan masjid.",
  "ustaz": "Ustaz ajar agama. Kalau soalan hukum susah, tanya ustaz.",
  "sunnah": "Sunnah ni apa Nabi buat. Ikut sunnah dapat pahala.",
  "aurat": "Aurat kena tutup. Lelaki pusat sampai lutut, perempuan seluruh badan kecuali muka tangan.",
  "fitnah": "Fitnah ni cakap benda tak betul pasal orang. Dosa besar.",
  "ghibah": "Ghibah ni mengumpat. Jangan mengumpat kawan.",
  "amanah": "Amanah ni jaga barang orang baik-baik. Jangan khianat.",
  "jujur": "Jujur ni cakap betul. Jangan tipu.",
  "ikhlas": "Ikhlas ni buat baik sebab Allah, bukan nak tunjuk kat orang.",
  "redha": "Redha ni terima apa Allah bagi dengan hati tenang.",
  "tawakal": "Tawakal ni usaha dulu, lepas tu serah kat Allah.",
  "ibu": "Ibu penat besarkan kita. Tolong dia, peluk dia.",
  "mak": "Mak kau penat. Tolong mak kat rumah.",
  "mama": "Mama sayang kau. Jangan buat mama risau.",
  "umi": "Umi sayang kau. Hormat umi selalu.",
  "ayah": "Ayah kerja keras untuk keluarga. Hormat ayah.",
  "bapa": "Bapa cari rezeki untuk kita.",
  "abah": "Abah sayang kau. Dengar cakap abah.",
  "papa": "Papa kerja keras. Peluk papa bila dia balik kerja.",
  "adik": "Adik kena jaga. Jangan buli adik.",
  "abang": "Abang kena jaga adik. Jadi contoh baik.",
  "kakak": "Kakak tolong jaga adik. Hormat kakak.",
  "keluarga": "Keluarga paling penting. Tolong mak ayah kat rumah.",
  "nenek": "Nenek sayang cucu. Ziarah nenek selalu.",
  "datuk": "Datuk sayang cucu. Dengar cerita datuk.",
  "sepupu": "Sepupu macam adik beradik. Main elok-elok jangan gaduh.",
  "kawan": "Kawan baik yang tolong masa susah, bukan yang ajak buat jahat.",
  "sahabat": "Sahabat baik ajak buat baik, bukan ajak ponteng.",
  "jiran": "Jiran kena hormat. Jangan buat bising sangat.",
  "cinta": "Crush tu biasa. Fokus belajar dulu.",
  "crush": "Crush tu biasa. Jangan layan sangat.",
  "kahwin": "Kahwin bila dah besar, dah ada kerja.",
  "sayang": "Sayang mak ayah, sayang keluarga. Tunjuk dengan tolong mereka.",
  "rindu": "Rindu tu biasa. Kalau rindu mak ayah, call mereka.",
  "gaduh": "Gaduh dengan kawan tu biasa. Minta maaf, baik balik.",
  "maaf": "Minta maaf tu bukan kalah. Minta maaf tu berani.",
  "tolong": "Tolong orang ni pahala. Tolong mak ayah kat rumah dulu.",
  "hormat": "Hormat orang tua, hormat cikgu, hormat kawan.",
  "buli": "Buli tu jahat. Kalau kena buli, bagitau cikgu / mak ayah.",
  "ejek": "Jangan ejek orang. Orang yang kena ejek tu sedih.",
  "sombong": "Sombong tu tak baik. Jangan sombong dengan kawan.",
  "sekolah": "Sekolah tempat belajar + kawan. Jangan ponteng.",
  "cikgu": "Cikgu ajar kita ilmu. Hormat cikgu.",
  "guru": "Guru ajar kita ilmu. Tanpa guru kita tak pandai.",
  "belajar": "Cara belajar power: Baca 25 minit, rehat 5 minit, ulang.",
  "exam": "Tips exam: Tidur awal, baca soalan betul-betul, jawab yang senang dulu.",
  "spm": "SPM ni penting tapi bukan penamat. Buat yang terbaik.",
  "kerja": "Kerja sekolah buat awal-awal. Jangan buat last minute.",
  "homework": "Homework buat hari ni jugak. Jangan tangguh esok.",
  "sains": "Sains: Air H2O, bumi pusing matahari 365 hari.",
  "biologi": "Biologi: Manusia ada jantung, paru-paru, otak.",
  "kimia": "Kimia: Air H2O, garam NaCl, oksigen O2.",
  "fizik": "Fizik: Graviti tarik benda ke bawah.",
  "matematik": "Matematik: Luas segi empat = panjang x lebar.",
  "addmath": "Addmath: Jangan takut formula. Faham konsep, banyak latihan.",
  "bm": "BM: Karangan kena ada pendahuluan, isi, penutup.",
  "english": "English: 'I am happy' = 'Saya gembira'.",
  "melayu": "Melayu: 'Gembira' = happy.",
  "sejarah": "Sejarah: Malaysia merdeka 31 Ogos 1957.",
  "merdeka": "Merdeka: 31 Ogos 1957. Tunku Abdul Rahman bapa kemerdekaan.",
  "geografi": "Geografi: Malaysia ada Semenanjung + Sabah Sarawak.",
  "ekonomi": "Ekonomi: Harga naik sebab permintaan tinggi.",
  "seni": "Seni: Lukis, nyanyi, menari semua seni.",
  "muzik": "Muzik: Lagu best, nyanyi dengan kawan.",
  "pendidikan": "Pendidikan penting. Belajar rajin-rajin untuk masa depan.",
  "universiti": "Universiti tempat belajar tinggi.",
  "cita": "Cita-cita kau apa? Kejar betul-betul. Adam cita-cita dia nak buat AI macam aku.",
  "kerjaya": "Kerjaya best: Doktor, cikgu, engineer, polis, programmer.",
  "doktor": "Doktor tolong orang sakit. Nak jadi doktor kena rajin sains.",
  "engineer": "Engineer buat bangunan, robot, app. Macam Adam buat aku ni.",
  "polis": "Polis jaga keamanan. Kalau emergency call 999.",
  "askar": "Askar jaga negara. Berani dan disiplin.",
  "pilot": "Pilot bawa kapal terbang. Kena pandai Matematik + English.",
  "lawyer": "Lawyer tolong orang dalam mahkamah.",
  "youtuber": "Youtuber: Kena rajin buat content, jangan buat content bodoh.",
  "tiktok": "Tiktok best tengok, tapi jangan tengok 10 jam.",
  "instagram": "Instagram tempat share gambar. Jangan percaya semua benda.",
  "whatsapp": "Whatsapp tempat chat kawan. Jangan forward berita palsu.",
  "buku": "Buku ni kawan baik. Baca buku banyak-banyak, jadi pandai.",
  "perpustakaan": "Perpustakaan tempat pinjam buku. Diam dalam perpustakaan.",
  "kelas": "Kelas tempat belajar. Dengar cikgu dalam kelas.",
  "disiplin": "Disiplin: Datang awal, buat homework, dengar cakap cikgu.",
  "ponteng": "Ponteng tu tak baik. Rugi ilmu, mak ayah sedih.",
  "malas": "Malas tu musuh kita. Lawan malas dengan mula sikit-sikit.",
  "rajin": "Rajin ni kunci berjaya. Rajin sikit-sikit, lama-lama jadi banyak.",
  "pandai": "Pandai bukan sebab lahir pandai, tapi sebab rajin belajar.",
  "bodoh": "Takde orang bodoh, yang ada orang malas belajar je.",
  "soalan": "Soalan apa kau nak tanya? Tanya je, aku jawab.",
  "jawapan": "Jawapan kena fikir dulu, jangan main teka je.",
  "markah": "Markah bukan segala-galanya. Yang penting kau faham.",
  "gagal": "Gagal sekali bukan gagal selamanya. Cuba lagi.",
  "komputer": "Komputer: Ada CPU, RAM, storage. Macam otak, ingatan, almari.",
  "internet": "Internet ni best tapi bahaya. Jangan share password.",
  "phone": "Phone: Guna untuk belajar, jangan main game 10 jam.",
  "laptop": "Laptop macam komputer tapi boleh bawa mana-mana.",
  "robot": "Robot macam aku, HAYDEN. Robot ikut arahan manusia.",
  "ai": "AI ni macam aku, HAYDEN. Adam yang buat aku guna Streamlit + Gemini.",
  "tech": "Tech: AI, robot, komputer semua tech. Adam minat tech sebab tu dia buat aku.",
  "code": "Nak code apa? Taip 'code python kira umur'.",
  "python": "Python bahasa coding senang. Print('Hello') tu coding paling asas.",
  "game": "Game apa kau main? ML ke Roblox?",
  "ml": "ML tu Mobile Legends. Main boleh, tapi jangan sampai lupa homework.",
  "roblox": "Roblox best main dengan kawan. Jangan beli Robux banyak sangat.",
  "minecraft": "Minecraft: Bina rumah, lawan zombie. Best main kreatif.",
  "freefire": "Free Fire: Main hati-hati, jangan maki orang.",
  "pubg": "PUBG: Tembak-tembak dalam game je.",
  "streamlit": "Streamlit tu yang Adam guna untuk buat app aku ni.",
  "gemini": "Gemini tu AI dari Google. Aku guna Gemini untuk jawab soalan susah.",
  "google": "Google tempat cari maklumat. Taip je apa kau nak cari.",
  "youtube": "Youtube tempat tengok video. Tengok video belajar.",
  "password": "Password jangan share kat orang. Buat password susah sikit, jangan 123456.",
  "hack": "Hack tu jahat. Jangan hack akaun orang.",
  "virus": "Virus komputer rosakkan komputer. Jangan download benda pelik.",
  "wifi": "Wifi bagi internet. Kalau wifi slow, restart router.",
  "charger": "Charger jangan main masa charge. Bahaya.",
  "bateri": "Bateri phone jangan biar sampai 0% selalu. Charge bila 20%.",
  "camera": "Camera phone sekarang power. Ambil gambar cantik-cantik.",
  "edit": "Edit video guna CapCut senang. Adam pun guna CapCut.",
  "content": "Content creator kena rajin. Buat content baik-baik.",
  "viral": "Viral tu kalau ramai tengok video kau. Jangan buat benda bodoh nak viral.",
  "angkasa": "Angkasa: Ada planet, bintang, bulan. Manusia dah sampai bulan 1969.",
  "bumi": "Bumi ni satu-satunya planet ada manusia. Jaga bumi.",
  "bulan": "Bulan pusing bumi. Bulan pantul cahaya matahari.",
  "matahari": "Matahari bagi cahaya + haba kat bumi.",
  "bintang": "Bintang jauh gila. Cahaya bintang dari tahun lepas.",
  "planet": "Planet: Mercury, Venus, Bumi, Marikh, Jupiter, Zuhal, Uranus, Neptune.",
  "hujan": "Hujan sebab awan berat. Bawa payung kalau musim hujan.",
  "panas": "Panas sebab matahari kuat. Minum air banyak.",
  "banjir": "Banjir sebab hujan lebat + longkang tersumbat.",
  "gempa": "Gempa bumi sebab plat bumi bergerak.",
  "haiwan": "Haiwan: Kucing, anjing, burung semua makhluk Allah. Jangan dera haiwan.",
  "kucing": "Kucing ni manja. Bagi makan, bagi air, jangan tarik ekor dia.",
  "anjing": "Anjing setia. Kalau anjing orang, jangan kacau.",
  "burung": "Burung boleh terbang sebab ada sayap + tulang ringan.",
  "ikan": "Ikan hidup dalam air, bernafas guna insang.",
  "pokok": "Pokok bagi oksigen. Tanam pokok, bumi jadi sejuk.",
  "bunga": "Bunga cantik: Ros, matahari, orkid.",
  "ular": "Ular bahaya. Kalau nampak ular, lari.",
  "harimau": "Harimau haiwan kebanggaan Malaysia.",
  "gajah": "Gajah besar tapi baik. Gajah suka makan daun.",
  "makanan": "Makanan sihat: Nasi, sayur, ayam, buah.",
  "minuman": "Minuman best: Air kosong paling sihat.",
  "buah": "Buah: Durian raja buah, manggis ratu buah.",
  "sayur": "Sayur: Bayam bagi kuat, carrot bagi mata terang.",
  "masak": "Resepi senang: Nasi goreng - nasi, telur, kicap, bawang.",
  "resepi": "Resepi senang: Nasi goreng, telur goreng, maggi.",
  "nasi": "Nasi
    
    # Cari pekerja ikut keyword - ni yang buat dia pandai
    peta = {
        "kira": pekerja_calculator, "+": pekerja_calculator, "-": pekerja_calculator, "*": pekerja_calculator, "/": pekerja_calculator,
        "hukum": pekerja_hukum, "solat": pekerja_hukum, "puasa": pekerja_hukum, "halal": pekerja_hukum, "haram": pekerja_hukum,
        "berita": pekerja_berita, "maksud": pekerja_kamus, "kamus": pekerja_kamus, "translate": pekerja_translator,
        "kuiz": pekerja_kuiz, "sedih": pekerja_motivasi, "penat": pekerja_motivasi, "stress": pekerja_motivasi, "give up": pekerja_motivasi,
        "lawak": pekerja_lawak, "cerita": pekerja_cerita, "cuaca": pekerja_cuaca, "waktu solat": pekerja_waktu_solat,
        "ringgit": pekerja_duit, "usd": pekerja_duit, "duit": pekerja_duit, "sains": pekerja_sains,
        "sejarah malaysia": pekerja_sejarah_malaysia, "merdeka": pekerja_merdeka, "sejarah": pekerja_sejarah,
        "geografi": pekerja_geografi, "bola": pekerja_bola, "sukan": pekerja_sukan, "masak": pekerja_masak, "resepi": pekerja_masak,
        "sihat": pekerja_kesihatan, "sakit": pekerja_kesihatan, "belajar": pekerja_belajar, "game": pekerja_game,
        "teka": pekerja_teka_teki, "code": pekerja_code, "python": pekerja_code, "nama": pekerja_nama,
        "lagu": pekerja_lagu, "filem": pekerja_filem, "cinta": pekerja_cinta, "crush": pekerja_cinta,
        "doa": pekerja_quran, "quran": pekerja_quran, "jadual": pekerja_jadual, "english": pekerja_english,
        "melayu": pekerja_malay, "matematik": pekerja_matematik, "formula": pekerja_matematik, "tech": pekerja_tech, "ai": pekerja_tech,
        "simpan": pekerja_kewangan, "kewangan": pekerja_kewangan, "emosi": pekerja_emosi, "wikipedia": pekerja_wikipedia,
        "agama": pekerja_agama, "adab": pekerja_adab, "keluarga": pekerja_keluarga, "ibu": pekerja_ibu, "mak": pekerja_ibu,
        "ayah": pekerja_ayah, "bapa": pekerja_ayah, "guru": pekerja_guru, "cikgu": pekerja_guru, "sekolah": pekerja_sekolah,
        "exam": pekerja_exam, "peperiksaan": pekerja_exam, "spm": pekerja_spm, "biologi": pekerja_biologi,
        "kimia": pekerja_kimia, "fizik": pekerja_fizik, "addmath": pekerja_addmath, "bm": pekerja_bm, "bahasa melayu": pekerja_bm,
        "ekonomi": pekerja_ekonomi, "kerjaya": pekerja_kerjaya, "cita": pekerja_cita_cita, "doktor": pekerja_doktor,
        "engineer": pekerja_engineer, "polis": pekerja_polis, "pilot": pekerja_pilot, "youtuber": pekerja_youtuber,
        "komputer": pekerja_komputer, "internet": pekerja_internet, "phone": pekerja_phone, "handphone": pekerja_phone,
        "robot": pekerja_robot, "angkasa": pekerja_angkasa, "bumi": pekerja_bumi, "bulan": pekerja_bulan,
        "matahari": pekerja_matahari, "haiwan": pekerja_haiwan, "kucing": pekerja_kucing, "anjing": pekerja_anjing,
        "burung": pekerja_burung, "ikan": pekerja_ikan, "pokok": pekerja_pokok, "bunga": pekerja_bunga,
        "makanan": pekerja_makanan, "minuman": pekerja_minuman, "buah": pekerja_buah, "sayur": pekerja_sayur,
        "badminton": pekerja_badminton, "berenang": pekerja_berenang, "basikal": pekerja_basikal, "lari": pekerja_lari,
        "gym": pekerja_gym, "tidur": pekerja_tidur, "mimpi": pekerja_mimpi, "hantu": pekerja_hantu,
        "superhero": pekerja_superhero, "anime": pekerja_anime, "kartun": pekerja_kartun, "komik": pekerja_komik,
        "novel": pekerja_novel, "puisi": pekerja_puisi, "pantun": pekerja_pantun, "peribahasa": pekerja_peribahasa,
        "kawan": pekerja_kawan, "buli": pekerja_buli, "duit raya": pekerja_duit_raya, "raya": pekerja_hari_raya, "covid": pekerja_covid,
    }
    for kunci, pekerja in peta.items():
        if kunci in l:
            return pekerja(s)
    return f"✨ [Gemini] {pekerja_gemini(s)}"
import re

def bos_hayden(s):
    if pekerja_security(s) == "BLOCK":
        return "⛔ Security block. Soalan bahaya."
    l = s.lower().strip()
    if "siapa nama" in l or "nama kau" in l or "nama awak" in l or "siapa awak" in l or l in ["kau siapa", "awak siapa", "siapa kau"]:
        return "Nama aku HAYDEN-PRO-VERSION. Bos aku Adam yang buat aku. Kau pulak siapa?"
    if "siapa buat" in l or "siapa cipta" in l or "siapa bos" in l:
        return "Adam yang buat aku. Dia bos aku, dia dari Seremban."
    if "kau buat apa" in l or "kau buat ape" in l:
        return "Aku ni AI tolong jawab soalan kau. Ada 100 pekerja bawah aku."
    if l in ["hi", "hello", "hey", "salam", "assalamualaikum", "hai"]:
        return "Hai! Aku HAYDEN. Tanya aku apa-apa je."

    # NI YANG BARU - DIA BACA PERKATAAN PENUH, BUKAN SEKERAT
    # Contoh: makruh takkan kena tangkap jadi mak lagi
    perkataan = re.findall(r"[a-z0-9]+", l)
    perkataan_set = set(perkataan)

    def ada(*kata):
        return any(k in perkataan_set for k in kata)

    if ada("makruh", "haram", "halal", "hukum", "solat", "puasa", "islam", "wuduk", "najis"):
        return f"🕌 [Hukum] Makruh ni maksudnya benda yang tak disukai dalam Islam, tapi kalau buat tak berdosa, kalau tinggal dapat pahala. Contoh makruh: makan bawang mentah sebelum solat, main-main masa solat, berwuduk dengan air yang terdedah panas matahari. Nak tanya makruh apa lagi?"
    if ada("kira", "tambah", "darab", "bahagi", "tolak"):
        return f"🧮 [Calculator] {pekerja_calculator(s)}"
    if ada("berita"):
        return f"📰 [Berita] {pekerja_berita(s)}"
    if ada("maksud", "kamus"):
        return f"📖 [Kamus] {pekerja_kamus(s)}"
    if ada("translate"):
        return f"🌐 [Translator] {pekerja_translator(s)}"
    if ada("kuiz"):
        return f"❓ [Kuiz] {pekerja_kuiz(s)}"
    if ada("sedih", "penat", "stress"):
        return f"💪 [Motivasi] {pekerja_motivasi(s)}"
    if ada("lawak"):
        return f"😂 [Lawak] {pekerja_lawak(s)}"
    if ada("cerita"):
        return f"📖 [Cerita] {pekerja_cerita(s)}"
    if ada("cuaca"):
        return f"🌦️ [Cuaca] {pekerja_cuaca(s)}"
    if ada("ibu", "mak", "mama", "emak", "umi"):
        return f"❤️ [Ibu] {pekerja_ibu(s)}"
    if ada("ayah", "bapa", "abah", "papa"):
        return f"❤️ [Ayah] {pekerja_ayah(s)}"
    if ada("nama"):
        return f"✨ [Nama] {pekerja_nama(s)}"
    if ada("lagu"):
        return f"🎵 [Lagu] {pekerja_lagu(s)}"
    if ada("filem"):
        return f"🎬 [Filem] {pekerja_filem(s)}"
    if ada("cinta", "crush"):
        return f"💔 [Cinta] {pekerja_cinta(s)}"
    if ada("doa", "quran"):
        return f"🤲 [Quran/Doa] {pekerja_quran(s)}"
    if ada("belajar"):
        return f"📚 [Belajar] {pekerja_belajar(s)}"
    if ada("game"):
        return f"🎮 [Game] {pekerja_game(s)}"
    if ada("kucing"):
        return f"🐱 [Kucing] {pekerja_kucing(s)}"
    if ada("bola"):
        return f"⚽ [Bola] {pekerja_bola(s)}"
    if ada("masak", "resepi"):
        return f"🍜 [Masak] {pekerja_masak(s)}"
    if ada("tidur", "mimpi"):
        return f"😴 [Tidur] {pekerja_tidur(s)}"
    if ada("sekolah", "cikgu", "guru"):
        return f"🏫 [Sekolah] {pekerja_sekolah(s)}"
    if ada("sains", "biologi", "kimia", "fizik"):
        return f"🔬 [Sains] {pekerja_sains(s)}"
    if ada("sejarah", "merdeka"):
        return f"🇲🇾 [Sejarah] {pekerja_sejarah_malaysia(s)}"

    return f"✨ [Gemini] {pekerja_gemini(s)}"
def bos_hayden(s):  # <-- NI BOS, PALING BAWAH
    if pekerja_security(s) == "BLOCK":
        return "⛔ Security block. Soalan bahaya."
    l = s.lower().strip()
    if "siapa nama" in l or "nama kau" in l:
        return "Nama aku HAYDEN-PRO-VERSION. Bos aku Adam..."
    if "siapa buat" in l or "siapa cipta" in l:
        return "Adam yang buat aku..."
    # ... dia baca PEKERJA_BIG kat sini ...
    for _k in sorted(PEKERJA_BIG.keys(), key=len, reverse=True):
        if _k in l:
            return PEKERJA_BIG[_k]
    return f"✨ [Gemini] Aku HAYDEN, bos aku Adam..."
