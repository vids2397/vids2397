#program to compute simple interest

def SI(p,n,r=3.5):
	tmp = p*r*n/100
	return tmp

n1 = int(input("Enter the principle: "))
n2 = int(input("Enter the rate: "))
n3 = int(input("Enter the  time(in yrs): "))

res = SI(n1,n3)
print(res)
