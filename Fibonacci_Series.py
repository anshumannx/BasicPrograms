                                     #program for fibonacci series
num = int(input("Enter required number\n"))
a=0
b=1
count=0
if num<0 :
    print("Please enter a valid number")
elif num==0 :
    print("The number must be greater than 0")
elif num==1 :
    print(b)
else :
    while count<=num :
           print(a)
           sum = a+b
           a=b
           b=sum
           count +=1