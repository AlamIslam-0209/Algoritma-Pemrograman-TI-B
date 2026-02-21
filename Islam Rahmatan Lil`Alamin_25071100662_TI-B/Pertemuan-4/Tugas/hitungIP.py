try:
	if 2 == 3:
    print(A)
except IndentationError:
	print("Terjadi TypeError, pastikan Anda menjumlahkan dua angka.")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

teks = input("masukkan teks: ")  # misalnya diisiin "Hello World"
print(teks)        #Output: Hello World
print(type(teks))  #Output: <class 'str'>