#ques1
string = "Python is a case sensitive language"

print(len(string))
print(string[::-1])
new_string=string[10:26]
print(new_string)
print(string.replace("a case sensitive","object oriented"))
print(string.index("a"))
print(string.replace(" ",""))
print("\n")

#ques2
name="Shreya"
sid=21104108
dep="electrical engineering"
cgpa=9.8

intro="Hey, {} Here! \n My SID is {} \n I am from {} department and my CGPA is {}."
formatted=intro.format(name,sid,dep,cgpa)
print(formatted)
print("\n")

#ques3
a=56
b=10

print(a&b)
print(a|b)
print(a^b)
print(a<<2,b<<2)
print(a>>2,b>>4)
print("\n")

#ques4
#Program to find the greatest of three numbers
num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
num3=int(input("enter the number 3: "))

#To find the greatest of three numbers 
if (num1>num2) and (num1>num3):
    greatest = num1
elif (num2>num1) and (num2>num3):
    greatest = num2
else:
    greatest = num3

print("the greatest of the three numbers is",greatest)
print("\n")

#ques5 
line=input("Enter the line: ")
if ("name" in line):
   print("Yes")
else:
   print("No")
print("\n")

#ques6
a=float(input("Length of Side1: "))
b=float(input("Length of Side2: "))
c=float(input("Length of Side3: "))
A=int(a)
B=int(b)
C=int(c)
print("Can the triangle be formed?")
if A>=(B+C) or B>=(C+A) or C>=(A+B):
    print("No, Triangle cannot be formed")
else:
    print("Yes, Triangle can be formed")

