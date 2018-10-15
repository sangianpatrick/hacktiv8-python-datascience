angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
	print("{angka} bilangan genap".format(angka = angka))
else:
	print("{angka} bilangan ganjil".format(angka = angka))

if angka > 5:
	print("{angka} lebih dari 5".format(angka = angka))
elif angka == 5:
	print("angka sama dengan 5")
else:
	print("{angka} lebih kecil dari 5".format(angka = angka))
