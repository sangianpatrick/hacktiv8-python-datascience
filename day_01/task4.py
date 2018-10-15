#tuple vs list

my_list = [1,2,3]  #list bisa diubah
my_tupel = (1,2,3) #tuple tidak bisa diubah

my_list = my_list + [5,6] #update variable
print(my_list)

#penyisipan insert parameter: loc, item
my_list.insert(0,'patrick')
print(my_list)

#penyisipan belakan (append)
my_list.append('python')
print(my_list)
