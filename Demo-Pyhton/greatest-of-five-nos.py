# Program to find the greates of five numbers 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number:"))
d = int(input("Ente the forth number: "))
e = int(input("Enter the fifth number: "))
if a>b and a>c and a>d and a>e:
    print("The greates number is: ",a)
elif b>a and b>c and b>d and b>e:
    print("The greatest number is: ",b)
elif c>a and c>b and c>d and c>e:
    print("The greatest number is: ",c)
elif d>a and d>b and d>c and d>e:
    print("The greatest number is:" ,d)
else: 
    print("The greatest number is: ",e)