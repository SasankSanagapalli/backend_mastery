marks=int(input('enter marks: '))
if marks>95:
    grade='A'               
elif marks>=80 and marks<=95:
    grade='B'
elif marks>=55 and marks<=79:
    grade='C'
else:
    grade='D'
print('Grade:',grade)