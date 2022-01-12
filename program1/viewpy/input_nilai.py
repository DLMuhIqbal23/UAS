data = []
def input_data():
    print("Masukkan Data Diri Anda")
    data.append({
            'Nama' : input("Nama Anda: "),
            'Nim' : int(input("NIM Anda: ")),
            'Kelas' : input("Kelas Anda: "),      
        })
