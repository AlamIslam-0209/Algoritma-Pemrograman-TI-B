Films = [["Harry Porter", 50000], ["Moana", 40000], ["Intelstellar", 30000], ["The Gamer", 60000], ["Forrest Gump", 65000]]

for i in range(len(Films)):
    # print(i + 1, Films[i])
    print(f"{i + 1}. {Films[i][0]}: {Films[i][1]}")
    
pilihan = int(input("Pilih Film yang ingin ditonton: "))

if Films[pilihan] in Films:
    print(Films[pilihan-1][0], ":", Films[pilihan-1][1])
else:
    print("Nomor tidak valid")