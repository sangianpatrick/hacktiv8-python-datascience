#for loop with write file
list_makanan = ["bakso", "sate", "nasi goreng"]

f = open("list_makanan.txt","w")
for makanan in list_makanan:
	# print("Saya pesan {sesuatu}".format(sesuatu=makanan))
	f.write("Saya pesan ")
	f.write(makanan)
	f.write("\n")

f.close()