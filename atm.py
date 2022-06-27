import random
def bankop() :
 balance = 100000
 operation = input ("What would you like to do today ? \t(deposit/withdraw/inquiry)\t")
 if operation=="deposit" :
      increase = int(input("Please enter the amount you want to deposit : \t"))
      total = balance+increase
      print("Your current balance has been updated to :\t",total)
 elif operation=="withdraw" :
      decrease = int(input("Please enter the amount you want to withdraw :\t"))
      total = balance-decrease
      print("Your current balance has been updated to :\t", total)
 elif operation== "inquiry" :
    print("Your current balance is :\t",balance)
 else :
     print("Invalid Input")
 print("would you like to continue? :\t(yes/no)")
 con = input()
 if con=="yes" :
     bankop()
 elif con =="no":
     print("Have a nice day.")
def inputd() :
 bankno = input("Enter your bank account number :\t")
 if len(bankno)==10 :
    i = random.randint(1000, 9999)
    temp = i
    print("Your otp is :\t", i)
    otp = int(input("Please Enter your 4-digit otp :\t"))
    if otp == temp:
        print("You have successfully entered your account")
        bankop()
    else:
        print("your otp is invalid")
 else:
    print("Entered account number is invalid , would you like to try again ?(yes/no)\t")
    retry = input()
    if retry == "yes" :
     inputd()
    else :
      print("Have a nice day")
inputd()

