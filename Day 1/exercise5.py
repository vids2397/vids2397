n = int(input("Enter a number: "))
i = 2

while i < n:
	r = n % i
	if r == 0:
		print('%d is not a prime number.' % n)
		break
	else:
		i += 1
		continue
if i == n:
	print('%d is a prime number.' % n) 
