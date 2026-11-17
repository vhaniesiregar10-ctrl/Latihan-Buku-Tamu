from tools import clear_data, add_entry, list_entries

while True:
    try:
        perintah = input().strip()
    except EOFError:
        break

    if perintah == "EXIT":
        break
    elif perintah == "CLEAR":
        clear_data()
        print("Data dikosongkan.")
    elif perintah.startswith("ADD|"):
        bagian = perintah.split("|", 2)
        if len(bagian) != 3:
            print("Error: format tidak valid.")
            continue
        _, nama, pesan = bagian
        try:
            add_entry(nama, pesan)
            print("Entri ditambahkan.")
        except ValueError as e:
            print(f"Error: {e}")
    elif perintah == "LIST":
        print(list_entries())
    else:
        print("Error: perintah tidak dikenal.")