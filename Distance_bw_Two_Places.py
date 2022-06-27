                                       #program for distance formulae
print("Enter coordinates for Delhi :")
d1 = int(input())
d2 = int(input())
print("Enter coordinates for Mumbai :")
x1 = int(input())
x2 = int(input())
if(x1<0 or x2<0 or d1<0 or d2<0) :
    print("Please Enter Valid Coordinates")
else :
   total_distance = ((d2-d1)**2 + (x2-x1)**2)**(1/2)
   print("The coordinates for Delhi were ",d1,d2,"\nAnd the coordinates for Mumbai were "
         ,x1,x2,"\nThe distance between them is %.2f" %total_distance)