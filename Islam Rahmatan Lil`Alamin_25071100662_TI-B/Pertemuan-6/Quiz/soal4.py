hari = 2
film = 3

m = [[0 for j in range(film)] for i in range(hari)]

for i in range(hari):
    for j in range(film):
        m[i][j] = int(input("Masukkan jumlah tiket"))
        
print(sum(m[0]) + sum(m[1]))
print((i for i in m[i][0]) + sum(j for j in m[j][1]))