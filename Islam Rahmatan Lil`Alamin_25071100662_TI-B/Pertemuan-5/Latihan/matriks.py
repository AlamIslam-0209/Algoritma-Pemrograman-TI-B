A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


C = [[0 for i in range(3)] for j in range(3)]
C_tambah = [[0 for i in range(3)] for j in range(3)]
C_kurang = [[0 for i in range(3)] for j in range(3)]
C_skalar = [[0 for i in range(3)] for j in range(3)]


for baris in range(len(A)):
    for elemen in range(len(A[baris])):
        C_tambah[baris][elemen] = A[baris][elemen] + B[baris][elemen]
    print(C_tambah[baris], end="\n")
    
print()

for baris in range(len(A)):
    for elemen in range(len(A[baris])):
        C_kurang[baris][elemen] = A[baris][elemen] - B[baris][elemen]
    print(C_tambah[baris], end="\n")

print()

for baris in range(len(A)):
    for elemen in range(len(A[baris])):
        C_skalar[baris][elemen] = A[baris][elemen] * 4
    print(C_tambah[baris], end="\n")
print()


#===================================================================#

print("===================================================================")
print("Versi pakai numpy \n")
import numpy as np

A = np.array(A)
B = np.array(B)

C_tambah = A + B
print(C_tambah)

C_kurang = A - B
print(C_kurang)

C_skalar = A * 4
print(C_skalar)

C_dot = np.dot(A, B)
print(C_dot)

A_tranpose = A.T
B_tranpose = B.T