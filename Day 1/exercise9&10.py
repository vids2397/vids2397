Maths = {1, 2, 3, 5, 7, 9} 
Physics = { 2, 4, 6, 9}
Chemistry = {1, 3, 5, 9}

ans1 = Maths.intersection(Physics)
ans2 = Maths.intersection(Chemistry)
ans3 = Chemistry.intersection(Physics)
ans4 = Maths.intersection(ans3)
ans5 = (Maths.union(Physics.union(Chemistry))).difference(ans1.union(ans2.union(ans3)))

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
