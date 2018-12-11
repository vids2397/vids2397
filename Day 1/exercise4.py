n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

if n1 > n2 and n1 > n3:
	print('%d is the biggest number.' % n1)
elif n2 > n1 and n2 > n3:
	print('%d is the biggest number.' % n2)
elif n3 > n2 and n3 > n1:
	print('%d is the biggest number.' % n3)
else:
	print("Any two of the three numbers are the same.")

 
