def check(n) :
    if(n%4==0 and n%100==0) :
        if(n%400==0) :
            print("Leap Year")
    else :
        print("Not a leap year")
year = int(input())
check(year)
