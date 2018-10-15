a = input()
jml_huruf = 0
jml_angka = 0

for i in range(len(a)):
    if a[i].isdigit():
        jml_angka += 1
    elif a[i].isalpha():
        jml_huruf +=1
    else:
        pass

print("HURUF: {}".format(jml_huruf))
print("ANGKA: {}".format(jml_angka))



a = int(input())

puluhan_dict = {1:["sepuluh","sebelas","dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"],\
    2:"dua puluh", 3:"tiga puluh", 4:"empat puluh", 5:"lima puluh", 6:"enam puluh", 7:"tujuh puluh", 8:"delapan puluh", 9:"sembilan puluh"}

satuan_dict = {0:""}