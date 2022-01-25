#ques1
string = "Python is a case sensitive language"

#part(a)
#length of the input string
print(len(string))

#part(b)
#reversing the order of the string
print(string[::-1])

#part(c)
new_string=string[10:26]
print(new_string)

#part(d)
print(string.replace("a case sensitive","object oriented"))

#part(e)
#finding index of "a"
print(string.index("a"))

#part(f)
#removing the white spaces from the string
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

#part(a)
print(a&b)

#part(b)
print(a|b)

#part(c)
print(a^b)

#part(d)
print(a<<2,b<<2)

#part(e)
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
#Checking if word "name" is present in string or not
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

