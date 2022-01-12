data = []

def tambah_data():
    while True:   
        data.append({
            'nama': input("Nama: "),
            'nim': int(input("NIM: ")),
            'uts': int(input("UTS: ")),
            'uas': int(input("UAS: "))
        })
        tanya = input("Tambah data?(y/t): ")
        if tanya == "t":
          break

def ubah_data(nim):
    for i in data:
        u = nim
        if u == i['nim']:
            i['nama'] = input("Ubah nama: ")
            i['uts'] = input("Ubah uts: ")
            i['uas'] = input("Ubah uas: ")
            
def hapus_data(nim):
    h = nim
    if h == 1234:
        del data[0]
        print("Data telah terhapus")
    elif h == 2345:
        del data[1]
        print("Data telah terhapus")
    elif h == 3456:
        del data[2]
        print("Data telah terhapus")

def cari_data(nim):
    for i in data:
        c = nim
        if c == i['nim']:
            print("Nama: ",i['nama'])
            print("NIM: ", i['nim'])
            print("UTS: ", i['uts'])
            print("UAS: ",i['uas'])

        