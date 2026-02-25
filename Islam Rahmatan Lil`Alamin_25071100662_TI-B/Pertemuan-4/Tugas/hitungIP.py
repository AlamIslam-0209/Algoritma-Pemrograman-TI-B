def HitungIP():
    try:
        total = 0
        banyak_matkul = int(input("Masukkan jumlah matkul: "))
        for i in range(banyak_matkul):
            total += float(input(f"Masukkan nilai matkul ke-{i+1}: "))

        mean = total / banyak_matkul

        print(f"IP mahasiswa pada semester ini adalah {mean:.2f}")

    except ZeroDivisionError:
        print("Jumlah Mata Kuliah tidak boleh nol !")

    except ValueError:
        print("Input tidak valid!, pastikan hanya masukkan angka")

    except Exception as e:
        print(f"Terdeteksi error tak terduga: {e}")


HitungIP()
