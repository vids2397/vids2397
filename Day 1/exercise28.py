def swap(a,b):
	a = a + b
	b = a - b
	a = a - b
	print(a)
	print(b)

print("The valus of two numbers before swapping: ")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the first number: "))
print("The valus of two numbers after swapping: ")
swap(n1,n2)
