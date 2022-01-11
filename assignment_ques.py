#ques1
n1=int(input("enter number 1:"))
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))
print("Average of three numbers : ", n1+n2+n3/3)


#ques2
Gross_income = int(input("Gross Income: "))
Dependent = int(input("Number of Dependents: "))
Standard_deduction = 10000
Dependent_deduction = Dependent * 3000
Taxable_income = Gross_income - Standard_deduction - Dependent_deduction

# Tax is 20% of Taxable_income
Tax = float((20/100) * (Taxable_income))  
print("Income tax : ", Tax)


#ques3
s1=int(input("SID:"))
s2=str(input("Name:"))
s3=str(input("Gender:"))
s4=str(input("Course Name:"))
s5=float(input("CGPA:"))
list=[s1,s2,s3,s4,s5]
print(list)


#ques4
markslist = []
for i in range(5):
    marks=float(input("marks of student:" ))
    markslist.append(marks)
 
# Sorting the marks list
markslist.sort() 
print(markslist)


#ques5
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#(a)
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)

#(b)
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3]="Purple"; color[4]="Purple"
print(color)
