from random import randint

def tebak_angka():
	angka_acak = randint(1,10)
	percobaan = 0

	while True:
		percobaan += 1
		angka = int(input("Masukkan angka: "))
		if angka > angka_acak:
			print("angka terlalu besar")
			
		elif angka == angka_acak:
			print("Ya benar angka {}".format(angka))
			print("Percobaan dilakukan {} kali".format(percobaan))
			break
		else:
			print("angka terlalu terlalu kecil")


tebak_angka()


		