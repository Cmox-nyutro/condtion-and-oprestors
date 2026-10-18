# for i in range(1,11):
#     for j in range(1,6): 
#         print("$" ,end ="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("$" ,end ="")
#     print()
# for i in range(5,0 ,-1):
#     for j in range(i):
#         print("$" ,end = " ")
#     print( )
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end ="")
#     print()

# for i in range(5 , 0,-1):
#     for j in range(i ,0 ,-1):
#         print(j ,end ="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print("*" ,end ="")
        
#     print()

# for i in range(1,6):
#     for  j in range(1,i+1):
#         print("*" , end ="")
#     print()
    
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*" ,end  = "")
#     print()
# for i in range(1,6):
#     for j in range(1 , i+1):
#         print(j ,end ="")
#     print()
# for i in range(5 , 0 ,-1):
#     for j in range(i, 0 ,-1):
#         print(j,end = "")
#     print()

# python:py is high level machine ,they have easy syntax, they are made by c ,python is  a open source programming language , python have multiple librares(num py,panda,py tourch)  
#var ky hota hey :var is a type of identifiers they are assing value /reprasent a value
#name = "shivam" : name is  a variable and = is opretor, "shivam" is a str value
#data type:-int,float,str,boolen ,tuple,list,complex number
#type()
# a = 6
# b = type(a)
# print(b)
#int :int is a type of data type and they are basically numbers 
#float:a decimal value like 5.5
#boolen:boolen when condtion is true and false
#true/false where use:when conditon is true or false manily while loop
#multile var ek sath:
# a,b,c = 10,20,30 they are assing orderly
#print() use:print is  a type of function they are print any value
#user input
# a = input("Enter your name:")
#input se milne vael data ka default data type:-string
#str to int
# a = "20"
# b = int(a)
# print(b)
# print(type(b))

# a = int(4.0)
# b = 4.0
# print(type(b))
#type casting : type catsing is a basically convetor one data type to another data type  
# ==============================OPRETORS===================================
#py mey arithematic opretors:-
'''
+ ,- ,/ ,*,//,**

'''
#addition of two number
# a = 3
# b =4
# c = a+b
# print(f"c is {c}")
# a = 4
# b = 2
# c = a-b
# print(f"c is {c}")
# a  = 4
# b = 3
# c = a*b
# print(c)
# a  = 4
# b = 3
# c = a/b
# print(c)
# a = 10
# b = 4
# c = a % b
# print(c)
# a  = 4
# b = 3
# c = a//b
# print(c)
# a  = 4
# b = 3
# c = a**b
# print(c)
# a  = 4

# c = a**2
# print(c)
# a  = 4
# c = a**3
# print(c)
#comparison opretor and diff btwn =  and == 
'''
a = b :- equal
a==b:-equal and fix
a>=b:greater then  and equal then b
a<=b:less then b and equal
a>b:greater then b
a<b:less then b
a!=b:not equal
'''
'''
how many opretor in python
7.
1)arithametic:+,-,%,*,%,//,** 
2)assingment:-=,+=,-=,/=
3)bitwise:&,|,^,<<,>>
4)logical:and ,or ,not
5)comparison :=,==,<=,>=,!=
6)membership :in ,notin
7)identity:is,isnot 
'''
# logical:and ,or ,not
# how many types of opretor in pyhton 
# 7types
'''
1. ASSIGNMENT: +=,-=,*=,/=
2. ARITHAMETIC:+,-,*,/ ,// ,** 
3.COMPAISON := ,==,>=,<=,!=
4.BITWISE:&,<<,>>,|
5.MEMBERSHIP:IN ,NOT IN
6.IDENTITY:IS ,ISNOT
7.LOGIACL:AND OR NOT
'''

# ============================================================CONDITION=======================================

# if statment :when condition is  true so code is run "
# a = int(input("Enter the age:"))
# if a>=18:
#     print("your are eligible.....")
# num =int(input("Enter number:"))
# if num>0:
#     print("postive")
# else:
#     print("negative")
    
# num  =int(input("Enter number:"))
# if num%2==0:
#     print("even")
# elif num%2!=0:
#     print("odd")
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))

# if a>b:
#     print("a is greater")
# elif b>a:
#     print("b is greater")
# else:
#     print("both are equal.....")
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# c = int(input("Enter c :"))

# if a>b and a>c:
#     print("a is greater...")
# elif  b>a and b>c:
#     print("b is greater...")

# elif c>a and c>b:
#     print(" c is greater...")
# else:
#     print("some numbers are equal...")
# a = int(input("Enter number:"))
# if a==0:
#     print("yes num is zero")
# else:
#     print("they are not zero..")

# stu = float(input("Enter marks:"))
# if stu>=33 and stu>=80: 
#     print("yes! student is pass with A grade")
    
    
# else:
#     print("student is fail...")
# age = int(input("Enter the age:"))
# if age>=18:
#     print("yes it is adult....")
# else:
#     print("no it is minor....")
# a = int(input("Enter a :"))
# if a%5 ==0:
#     print("yes !it's divisible by 5...")
# # else:
# #     print("no it is not divisible..")
# a = int(input("Enter a :"))
# if a%10 ==0:
#     print("yes! it is divisble by 10.....")
# else:
#     print("no it is not divisible...")
#if:-if mean when condition is true 
# else :-else is opposite to if when if is true so else is false
# elif :-when we check multiple conditon and we want only single output
# student  = float(input("Enter marks:"))
# if student>=90:
#     print("GRADE = A")
# elif student>=75:
#     print("GRADE = B")
# elif student >=60:
#     print("GRADE = C")
# elif student>=40:
#     print("GRADE = D")
# elif student>=33:
#     print("GRADE = E ")
# else:
#     print("student is fail....")
# a = int(input("Enter a :"))

# if a%4 ==0:
#     print("leap year...")
# elif a%400 ==0:
#     print("yes leap year....")
# elif a%100 ==0:
#     print("it is not a leap year....")
# else:
#     print("not leap year..")
# ========================================STRING=========================
'''
#string is a collection of mulitple single character is like a name shivam 
#str len find
'''
# a = "shivam "
# b = len(a)
# print(b)
# a = "SHIVAM"
# b = a.lower()
# print(b)
# a = "shivam"
# b = a[0:1]
# print(b)
# a = "shiavm "
# b = a[-2:-1]
# print(b)
# a = "shiavm rawat"
# b =("avm" in a )
# print(b)
# a = "shiavm rawat"
# b = a.find("m")
# print(b)
# a = "shivam"
# b = "rawat"
# c = "okey"
# d = (a +" "+b + " " +c)
# print(d)
# a = "shivam rawat"
# b = a[6]
# print(b)
# b = input("enter:")
# consonants = 0
# vowels = 0
# for ch in b:
#     if ch in "aeiou AEIOU":
        
#         vowels +=1
#     else:
#         consonants+=1
        
# print(f"vowels:{vowels}")
# print(f"consonants:{consonants}")
# a = input("Enter name:")
# rev =" "
# for i in range(len(a)-1 ,-1,-1):
#     rev +=a[i]
# print(rev)

# a = input("Enter your name:")
# print(f"hello {a}")
#=======================LOOPS===============
# what is loop :any condtion is reapted when task is not complited
# for loop :for loop is a basically a types of loop who define range
# while loop when condition is true loop is contioues but condtion is false itertion will be close
# 1 to 10 print num
# for i in range(1,11):
    # print(i)
# 10 to 1
# for i in range(10 ,0,-1):
    # print(i )
# for i in range(1,101):
#     if i%2==0:
#         print(f"it is even bcz it is {i}")
#     elif  i%2!=0:
#         print(f"it is odd bcz it is {i}")
# 1 se 10 tak num sum find kro
# count = 0

# for i in range(1,11):
#     count =count+i
#     print(count )
# print only even number 1 to 100
# for i in range(1,101):
#     if i%2==0:
        
#         print(i)
# print a table 
# a = int(input("Enter digit:"))
# for i in range(1 ,11):
#     print(f"{a}*{i} ={a*i}")
# n = int(input("Enter the number:"))
# count =0
# for i in range(1,11):
#     if i**2>0:
#         count = count+i
        
#     print(count)
# for i in range(1,11):
#     print(i**2)
# for i in range(1,11):    
#         print(i**3)
# n = int(input("Enter num:"))
# count =0
# while n>0:
#     count+=1
#     n = n//10
# print(count)
# sum =0
# while n>0:
#     dig = n%10
#     sum += dig
#     n = n//10
# print(sum)

n = int(input("Enter num:"))
count =0
while n>0:
    t= n%10
    count = count*10+t
    n = n//10
print(count)