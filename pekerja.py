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
