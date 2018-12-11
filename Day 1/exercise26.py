#program to print the largest number

def largest_no(n1,n2,n3):
	r1 = [n1,n2,n3]
	return max(r1)

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))

ans = largest_no(n1,n2,n3)
print(ans)
