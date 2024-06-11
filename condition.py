marks=int(input("enter your marks :"))

if marks>=90:
    grade="A"
elif marks<90 and marks>=80:
    grade="B"
elif marks<80 and marks>=70:
    grade="c"
else:
    grade="D"
print(grade)