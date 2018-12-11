#Program to find the prime umbers between the given range

def prime_no(low,upp):
	res = []
	for i in range(low,upp+1):
		tmp = 2;
		while tmp < i:
			r = i % tmp
			if r == 0:
				break;
			tmp += 1
		if tmp == i:
			res.append(i)
	return res
	
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))

ans = prime_no(n1,n2)
print(ans)
