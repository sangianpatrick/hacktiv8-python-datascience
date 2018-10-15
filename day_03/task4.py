#function

def sapa(nama):
	print("Hallo {nama}".format(nama=nama))
	print("Ini adalah fungsi sapa() \n")

def ganjilGenap(n):
	if n % 2 == 0:
		print("{n} adalah bilangan genap".format(n=n))
	else:
		print("{n} adalah bilangan ganjil".format(n=n))


ganjilGenap(11)
sapa("patrick")
ganjilGenap(32)
