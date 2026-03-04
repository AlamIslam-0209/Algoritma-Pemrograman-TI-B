Films = [["Harry Porter", 50000], ["Moana", 40000], ["Intelstellar", 30000], ["The Gamer", 60000], ["Forrest Gump", 65000]]
list_pembelian = []
total = 0
while True:
    for i in range(len(Films)):
        print(f"{i + 1}. {Films[i][0]}: {Films[i][1]}")
        
    pilihan = int(input("Pilih Film: "))
    if pilihan == 0:
        print("Pembelian tiket telah selesai")
        break
    
    jumlah_tiket = int(input(f"Masukkan jumlah tiket {Films[pilihan-1][0]} yang dibeli: "))
    total += Films[pilihan-1][1] * jumlah_tiket
    list_pembelian.append({"nama": Films[pilihan-1][0], "tiket": jumlah_tiket})
    print("\n")
    
print(total)
print(list_pembelian)