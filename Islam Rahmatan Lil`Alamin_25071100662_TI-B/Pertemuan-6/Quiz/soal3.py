total_pembelian = int(input("Masukkan total pembelian: "))
bayar = 0
while True:
    bayar = int(input("Masukkan jumlah unag yang dibayarkan: "))
    if bayar >= total_pembelian:
        if bayar == total_pembelian:
            print("uang anda pas")
            break
        print(f"Kembalian uang anda: {bayar - total_pembelian}")
        break
    else:
        print(f"Uang anda masih kurang {total_pembelian - bayar}, silahkan tambah uangnya")
        total_pembelian = total_pembelian - bayar