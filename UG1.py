print(f"{'KALKULATOR SEDERHANA':^40}")
print(f"{'-'*40:^40}")

while True:
    print(f"PILIH MENU:")
    print(f"1. Tambah")
    print(f"2. Kurang")
    print(f"3. Kali")
    print(f"4. Bagi")

    input_1 = int(input("Masukan Bilangan Pertama: "))
    input_2 = int(input("Masukan Bilangan Kedua: "))
    pilihan = input("Ingin menggunakan operasi apa (ketik 1/2/3/4): ")

    if pilihan == "1":
        hasil = input_1 + input_2
        print(f"Hasil : {hasil}")
    elif pilihan == "2":
        hasil = input_1 - input_2
        print(f"Hasil : {hasil}")
    elif pilihan == "3":
        hasil = input_1 * input_2
        print(f"Hasil : {hasil}")
    elif pilihan == "4":
        hasil = input_1 / input_2
        print(f"Hasil : {hasil}")

    pilih = input(f"Ingin berhenti ketik 'Q', Ingin lanjut ketik 'L' : ")
    if pilih == "Q":
        break

print(f"\n{'-'*5}{'Kalkulator Sederhana telah berakhir':^40}{'-'*5}")
