marks = int(input("Enter Marks : \n"))
if marks<=100 :
 if 100 <marks<=90 :
     print("A+")
 elif 80<marks<=89 :
     print("A")
 elif 70<marks<=79 :
     print("B+")
 elif 60<marks<=69 :
     print("B")
 elif 50<marks<=59 :
     print("C+")
 elif 40<marks<=49 :
     print("D")
 elif 33<=marks<=39  :
     print("pass")
 else :
     print("Fail")
else :
    print("Please Enter valid marks")