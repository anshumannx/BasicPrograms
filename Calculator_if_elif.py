                                     #program to create a calculator(if elif)
num_1= int(input("Enter first number\t"))
num_2 = int(input("Enter second number\t"))
a=input("Enter the operation you want to apply\t")
if a=='+' :
    c=num_1+num_2
    print(c)
elif a=='-' :
    c=num_1-num_2
    print(c)
elif a=='*' :
    c= num_1*num_2
    print(c)
elif a=='/' :
    c= num_1/num_2
    print(c)
else :
    print("Invalid Operator")