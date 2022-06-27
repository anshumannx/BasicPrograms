

                                     #program for compound interest
Principal = int(input("Enter Principal amount\t"))
Roi = int(input("Enter the Rate of Interest\t"))
Time = int(input("Enter the Time\t"))
ann = input("Is the interest compounded annually? (Yes/No)\t")
if ann =='Yes' :
    A = Principal*((1+Roi/100)**Time)
    CI = A-Principal
    print("The Compound Interest to be added will be \t",CI)
elif ann =='No' :
    A = Principal * ((1 + (Roi/2)/ 100) ** 2*Time)
    CI = A - Principal
    print("The Compound Interest to be added will be \t", CI)
else :
    print("Please reply with Yes or No")
