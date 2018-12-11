n1 = int(input("Enter the marks of 1st subject: "))
n2 = int(input("Enter the marks of 2nd subject: "))
n3 = int(input("Enter the marks of 3rd subject: "))
n4 = int(input("Enter the marks of 4th subject: "))
n5 = int(input("Enter the marks of 5st subject: "))

avg_marks = (n1 + n2 + n3 + n4 + n5) // 5

if avg_marks > 90:
	print("Grade A")
elif avg_marks > 80:
	print("Grade B")
elif avg_marks > 70:
	print("Grade C")
elif avg_marks > 50:
	print("Grade D")
elif avg_marks > 35:
	print("Grade E")
else:
	print("Grade F")
	
