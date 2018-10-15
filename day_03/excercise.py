def bilanganPrima(a,b):
	list_bilangan_prima = []
	for no in range(a,b+1):
		count = 0
		if no > 1:
			for x in range(1,no+1):
				if no % x == 0:
					count += 1

		if count == 2:
			list_bilangan_prima.append(no)

	return list_bilangan_prima


a,b = 1,50
print("\nList bilangan prima dari {} - {} adalah : \n".format(a,b))
print(bilanganPrima(a,b))

