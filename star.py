
def arrow(a) :
 for i in range(0,a):

    for k in (0,i) :
        print("    ",end = "")
    for j in range(0, i + 1 ):
         print("*", end="")
    for j in range(0, i + 1):
        print(i+1, end="")
    print("\r")
 for i in range(0,a+9) :
    print("*",end= "")
 print("\n",end="")
 for i in range(a,0,-1):
    for k in (0,i+1) :
        print("    ",end = "")
    for j in range(0, i ):
         print("*", end="")
    print("\r")
n= int(input("Enter the size for arrow :\t"))
arrow(n)
for i in range(n+1 ,0,-1) :
    for j in range(0,i-1) :
        print("*",end="")
    print("")
for i in range(0,n) :
    for j in range(0,i+1) :
        print("*",end="")
    print("")