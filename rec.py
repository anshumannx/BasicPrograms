import sys
n=int(input("Enter a number for factorial\n"))
fact=1
def rec(a) :
    global fact
    if(a<0) :
        print("Does not exist")
    elif(a==0) :
        return 1
    else :
        return (a*rec(a-1))
factorial = rec(n)
print(factorial)


#num = int(input("Enter number for sum\n"))
#sum = 0
#def sum_n(a) :
    #global sum
    #sum = sum + a
    #while(a>0) :
     #sum_n(a-1)
     #return sum
#add = sum_n(num)
#print(add)

#numf = int(input("Enter number for fibonacci series :\n"))
#series = 0
#def fib(a) :
   # global series

    #series = series + (series+1)
    #while (series <=a):
     #fib(a+1)
     #print(series,"\n")
#fib(numf)