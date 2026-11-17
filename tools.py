DATA_FILE = "guestbook.txt"


def clear_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("")


def load_entries():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            baris = f.read().splitlines()
    except FileNotFoundError:
        return []

    hasil = []
    for b in baris:
        if not b.strip():
            continue
        bagian = b.split("|", 1)
        if len(bagian) == 2:
            hasil.append((bagian[0], bagian[1]))
    return hasil


def save_entries(entries):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for nama, pesan in entries:
            f.write(f"{nama}|{pesan}\n")


def add_entry(nama, pesan):
    nama = nama.strip()
    pesan = pesan.strip()
    if nama == "" or pesan == "":
        raise ValueError("nama/pesan tidak boleh kosong")

    entries = load_entries()
    entries.append((nama, pesan))
    save_entries(entries)


def list_entries():
    entries = load_entries()
    lines = ["=== Buku Tamu ==="]
    if len(entries) == 0:
        lines.append("(kosong)")
    else:
        for i, (nama, pesan) in enumerate(entries, start=1):
            lines.append(f"{i}. {nama}: {pesan}")
    lines.append(f"Jumlah : {len(entries)}")
    return "\n".join(lines)