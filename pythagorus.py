import math
def check (a,b,c) :
     res = c-math.sqrt(a**2+b**2)
     if res==0 :
        print("The triangle is pythagorean")
     else :
        print("The triangle is not pythagorean")
l=int(input("Enter length\t"))
b=int(input("Enter breadth\t"))
h=int(input("Enter hypotenuse\t"))
check(l,b,h)