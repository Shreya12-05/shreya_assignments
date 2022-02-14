#ques1
print("Q-1")
string=input("Give a string:\n")
list1=[]
#splitting the list
list2=string.split()
y=len(list2)
d=dict()
l=dict()

#for one word
if y==1:          
    for i in string:      
        list1.append(i) 
    for j in list1:        
        if j in d:        
            d[j]=d[j]+1    
        else:
            d[j]=1
    print(d)        

#for multiple words
else:
    for i in list2:        
        if i in l:
            l[i]=l[i]+1
        else:
            l[i]=1
    print(l) 
print("\n")

#ques2
print("Q-2")
day=int(input("Enter a day[1-31]: "))

year=int(input("Enter a year[1800-2025]: "))

#leap year or not
if (year%4==0):
    leapyear=True
else:
    leapyear=False

month=int(input("Enter the month[1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    length = 31
elif month == 2:
    if leapyear:
        length = 29
    else:
        length = 28
else:
    length = 30

if day < length:
    day += 1
else:
    day = 31
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(f"The next date is {day}/{month}/{year} ")
print("\n")

#ques3
print("Q-3")

#Creating a list
lst=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input("enter list elements: "))
    lst.append(ele)
print(lst)
#squaring the elements of list
sq_list=[i**2 for i in lst]

#Zipping the lists
l=list(zip(lst,sq_list))
print(l)
print("\n")

#ques4
print("Q-4")
grade_points=float(input("Enter your grade points: "))

if grade_points==10:
    print("Your grade is 'A+' and Outstanding performance")
elif grade_points==9:
    print("Your grade is 'A' and Excellent performance")
elif grade_points==8:
    print("Your grade is 'B+' and Very Good performance")
elif grade_points==7:
    print("Your grade is 'B' and Good performance")
elif grade_points==6:
    print("Your grade is 'C+' and Average performance")
elif grade_points==5:
    print("Your grade is 'C' and Below Average performance")
elif grade_points==4:
    print("Your grade is 'D' and Poor performance")
else:
    print("Error")
print("\n")

#ques5
print("Q-5")
#Program to print the pattern
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=11
for i in range(n):
    if 2*i<n:
        j=a[:n-2*i]

        print(" "*i,j)    
print("\n")

#ques6
print("Q-6")

student_info=dict()
n="y"
listsid=[]

while(n=="y"):
    sid=int(input("Give the sid: "))
    name=input("Enter your name: ")
    student_info[sid]=name
    n=input("y or n: ")             #y means want to add more student and n means no
#(a)
#making a dictionary that store student details
    listsid.append((sid,name))
print("a")
print("The required dictionary:\n",student_info)

#(b)
#to sort our dictionary based to names
print("(b)")
print(student_info)
#now exchange the key value pair and make a new dictionary and a new list
newdict=dict()
list_name=[]
#now we iterate
for (s,n) in student_info.items():
    newdict[n]=s
    list_name.append((n,s))

#now we create a sorted dictionary from our sorted list
sorted_dict=dict(list_name)
print("The sorted dictionary-",sorted_dict)
#now we just need to exchange the key value pair of the sorted_dict
dict_sort_name=dict()
for (s,n) in sorted_dict.items():
    dict_sort_name[n]=s
print("dictionary sorted on the basis of name-\n",dict_sort_name)

#(c)
#sort the dictionary on the basis of sid
#sort the list and convert it into dictionary 
print("(c)")
listsid.sort()
dict_sort_sid=dict(listsid)
print("sorted dictionary based on sid-\n",dict_sort_sid)

#(d)
#search a student's name by sid    
print("(d)")    
entered_sid=int(input("Please enter SID-"))
print("The name of the student with the entered sid is-")    
print(student_info[entered_sid])
print("\n")

#ques7
print("Q-7")
#Program to print a Fibonacci sequence
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

terms = int(input("Enter the number of terms: "))

#To check if the number of terms are positive
if terms<=0:
    print("Enter a positive number")
else:
    print("Fibonacci sequence: ")
for i in range (terms):
    print(f"{fibo(i)}",end=",")

#calculating average
    j=0
for i in range (terms):
    j=j+fibo(i)
average= j/terms
print(end="\n")
print(average)  
print("\n")

#ques8
print("Q-8")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
print(Set1)
print(Set2)
print(Set3)
#part a
print("(A): Set of elements that are in set 1 and set 2 but not in both: ",Set1^Set2)
#part b 
print("(B): Set of elements that are in only one of the three sets: ",Set1^Set2^Set3)
#part c 
print("(C): Set of elements that are exactly two of the sets: ",(Set1&Set2|Set2&Set3|Set1&Set3)-(Set1&Set2&Set3))
#part d
print("(D): Set of all integers in the range 1 to 10 that are not in set 1: ",set(range(1,10))-Set1)
#part e 
print("(E): Set of all integers in the range 1 to 10 that are not in set1, set2 and set3: ",set(range(1,10))-Set1-Set2-Set3)
