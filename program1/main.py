from modelpy import daftar_nilai
from viewpy import input_nilai
from viewpy import view_nilai

print("======================")
print("Ulangan Akhir Semester")
print("======================")
print("Pilih menu")
print("1. Masukkan data diri anda")
print("2. Menambahkan data")
print("3. Mengubah data")
print("4. Menghapus data")
print("5. Mencari data")
print("6. Menampilkan data")
print("7. Keluar")
print("======================")
while True:
    tanya = input("Pilih Menu: ")
    if tanya == "1":
        print("======================")
        print("Data Diri Anda")
        print("======================")
        input_nilai.input_data()
        print("======================")
    elif tanya == "2":
        print("======================")
        print("Menambahkan Data")
        print("======================")
        daftar_nilai.tambah_data()
        print("======================")
    elif tanya == "3":
        print("======================")
        print("Mengubah Data")
        print("======================")
        nim = int(input("Nim yang ingin diubah: "))
        print("======================")
        daftar_nilai.ubah_data(nim)
    elif tanya == "4":
        print("======================")
        print("Menghapus Data")
        print("======================")
        nim = int(input("Nim yang ingin dihapus: "))
        daftar_nilai.hapus_data(nim)
        print("======================")
    elif tanya == "5":
        print("======================")
        print("Mencari Data")
        print("======================")
        view_nilai.cetak_hasil_pencarian()
        print("======================")
    elif tanya == "6":
        print("======================")
        print("Menampilkan Data")
        print("======================")
        view_nilai.cetak_daftar_nilai()
        print("======================")
    elif tanya == "7":
        break