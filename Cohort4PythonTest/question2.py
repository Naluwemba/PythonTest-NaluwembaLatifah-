# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

#Anwers
student_mark = int(input("Enter the mark scored : \t"))

if student_mark>=90:
    print(f" The GRADE is A")
elif student_mark >=80 :
    print(f"The GRADE is B")
elif student_mark >=70 :
    print(f"The GRADE is C")
elif student_mark >=60 :
    print(f"The GRADE is D")
elif student_mark >=40 :
    print(f"The GRADE is F")
else:
    print(f"The GRADE is F")
    
    