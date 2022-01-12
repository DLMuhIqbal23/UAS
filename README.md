# UAS

Pertama bikin file program lalu didalam file program buat 2 package dan 1 modul yaitu modelpy dan viewpy, modul main.py, lalu buat modul __init__.py disetiap package, init ini sangat penting dan harus selalu ada disaat kalian membuat package, lalu buat modul daftar_nilai,input_nilai.py,view_nilai.py.<p>
Pertama nyatakan data sebagai list, lalu isi kode fungsi def tambah_data:, def tambah data ini untuk menambahkan data, lalu while True agar terus melooping, lalu masukkan data.append({nama, nim, uts, uas}), lalu inputkan tanya untuk menanyakan apakah mau nambah data lagi atau tidak, lalu if tanya == "t": break agar jika tanya itu t maka loopingnya berhenti.<p> 
Selanjutnya isi kode def ubah(nim): untuk mengubah data, lalu for i in data: untuk data didalam i, lalu u = nim, lalu if u == i['nim']: i['nama'] s/d i['uas'] agar jika u itu sama yang ada didata bagian nim maka mengubah i['nama'] s/d i['uas'].<p>
Selanjutnya def hapus_data(nim): untuk menghapus data, lalu h = nim, lalu h == 1234 s/d if h == 3456: del data [0] s/d del data[2] disini saya dari awal merencanakan mengisi 3 saja maka if h dan del data hanya 3 saja jika mau lebih dari 3 silahkan tinggal bedakan setelah h == dan urutkan del data oh iya kode ini untuk jika h itu sama dengan angka yang kita taruh setelah h == maka program akan secara menghapus data, del data [0] itu maksudnya data yang pertama kali diinput, contoh jika h itu 1234 maka akan menghapus data yang pertama kali diinputkan.<p>
Selanjutnya def cari_data(nim): untuk mencari data, lalu masukkan for i in data: agar i didalam data, lalu c = nim, lalu if c == i['nim']:, lalu print(i['nama']) s/d print(i['uas']), if c itu i['nim'] maka program akan otomatis print(i['nama']) s/d print(i['uas']).<p> 
Selanjutnya ke modul input_nilai.py, lalu nyatakan data sebagai list, lalu def input_data(): untuk menginputkan data diri anda, lalu inputkan data.append ({'nama' s/d ['kelas']}).<p>
Selanjutnya ke module view_nilai, lalu from modelpy.daftar_nilai import data, cari (untuk memanggil kode fungsi cari atau def cari yang ada di package model py -> module daftar_nilai -> def cari), lalu s = data, lalu def cetak_daftar_nilai(): agar menampilkan hasil def tambah_data(), lalu for item in s:, lalu print(item['nama'] s/d item['uas']), lalu def cetak_hasil_pencarian(): untuk menampilkan hasil dari def cari(nim), lalu masukkan nim sebagai integer, lalu panggil def(nim).<p>
Selanjutnya ke modul main.py, lalu from modelpy import daftar_nilai, from viewpy import input_nilai, from viewpy import view_nilai, from dan import itu untuk memanggil fungsi atau def yang ada di package modelpy/viewpy dan module daftar_nilai.py/input_nilai.py/view_nilai.py, lalu bikin output seperti screenshot kode dibawah, lalu while True: untuk melooping, lalu tanya == input("Pilih Menu: ") agar memilih menu yang ada di output, lalu if tanya == "1": maka panggil def input_data, lalu elif tanya == "2": maka panggil def tambah_data, lalu elif tanya == "3": nim sebagai integer lalu panggil def ubah_data(nim), lalu elif tanya == "4":  nim sebagai integer lalu panggil def hapus_data(nim), lalu elif tanya == "5": panggil def cetak_hasil_pencarian(), lalu elif tanya == "6": lalu panggil def cetak_daftar_nilai(), lalu elif tanya == "7": break agar berhenti melooping.<p>
Screenshot Kode:<p>
![Gambar 4](ss/ss4.png)
![Gambar 5](ss/ss5.png)
![Gambar 6](ss/ss6.png)
![Gambar 7](ss/ss7.png)
![Gambar 8](ss/ss8.png)
![Gambar 9](ss/ss9.png)

Screenshot Hasil kode:<p>
![Gambar 1](ss/ss1.png)
![Gambar 2](ss/ss2.png)
![Gambar 3](ss/ss3.png)