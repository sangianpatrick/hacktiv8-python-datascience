pesanan = []
tambah = 'y'

while tambah == 'y':
	pesan = input("Masukkan pesanan anda: ")
	pesanan.append(pesan)
	tambah = input("Apakah ingin mengulang? (y/n) ").lower() #set to lowercase
print(pesanan)

