# Program Management Kontak
import function

# List of dictionary
daftar_kontak =[]
daftar_kontak.append({
    "nama" : "Kelvin",
    "email" : "kelvinrahmadhani4@gmail.com",
    "telepon" : "085648546347"
})

# Menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah KOntak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Pilih menu :")

    if menu == "0":
       print("Program selesai berjalan, Terimakasih")
       break
    elif menu =="1":
        function.display_kontak(daftar_kontak)
    elif menu =="2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu =="3":
        function.hapus_kontak(daftar_kontak)
    elif menu =="4":
        function.cari_kontak(daftar_kontak)