                              #program for sum of squares of first n natural numbers

a=int(input())
if a<0 :
        print("Enter a valid number , the above input is negative")
elif a==0 :
        print("Enter a valid number , the above input is 0")
else :
        s = (a * (a + 1) * (2 * a + 1) )/6
        print("The sum is :", s)
