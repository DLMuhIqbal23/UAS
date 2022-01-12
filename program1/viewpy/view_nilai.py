from modelpy.daftar_nilai import data, cari

s = data
def cetak_daftar_nilai():
    for item in s:
        print("Nama: ",item['nama'])
        print("NIM: ",item['nim'])
        print("UTS: ",item['uts'])
        print("UAS: ",item['uas'])

def cetak_hasil_pencarian():
    nim = int(input("Nim yang ingin dicari: "))
    cari(nim)
