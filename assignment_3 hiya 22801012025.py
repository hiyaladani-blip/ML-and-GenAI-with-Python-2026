# ASSIGNMENT 3

#Create a function to print the first n natural numbers.
def natural_num(n):
    for i in range(1,n+1):
        print(i,end=" ")
natural_num(10)




#Create a function to calculate the sum of the first n natural numbers.
def Sum(n):
    sum=0
    for i in  range(1,n+1):
        sum+=i
    print(f"Sum of the first {n} is {sum}")
n=int(input("Enter the number upto you want sum : "))
Sum(n)




#Create a function to reverse a given number.
def reverse(n):
    while(n>0):
        m=n%10
        print(m,end="")
        n=n//10
n=int(input("Enter the number: "))
reverse(n)


#Create a function to count the digits in a given number.
def count_num(n):
    count=0
    while(n>0):
        count+=1
        n=n//10
    print(count)
n=int(input("Enter the number: "))
count_num(n)



#Create a function to check palindrome number.
def ispalin(n):
    original=n
    reverse=0
    while(n>0):
        m=n%10
        reverse=reverse*10+m
        n=n//10
    if(reverse==original):
      print("Palindrome")
    else:
       print("Not Palindrome")
n=int(input("Enter the number: "))
ispalin(n)




#Create a function to print the Fibonacci series up to n terms.
def fibonacci(n):
    a=0
    b=1
    next=0
    for i in range(n):
        print(a,end=" ")
        next=a+b
        a=b
        b=next
n=int(input("Enter the number upto which fibonacci series is required: "))
fibonacci(n)





#Perform Calculations
def calculator(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        if num2!=0:
            return num1/num2
        else:
            print("Division not possible")
    else:
        print("Invalid operation")
num1=int(input("Enter the number one : "))
num2=int(input("Enter the number two : "))
opr=input("Enter the operation : ")
print(calculator(num1,num2,opr))



#Use select operation.
try:
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    result=num1/num2
    print(result)
except : 
    print("Division not possible")




#Display results
class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
Name=input("Enter the name of the student : ")
marks=int(input("Enter your marks : "))
s1=Student(Name,marks)
print(s1.name)
print(s1.mark)