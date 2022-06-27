def sec_min(a) :
    return a/60
def sec_hour(a) :
    return a/3600
def sec_day(a) :
    return a/(3600*24)
seconds = int(input("Enter the number of seconds:\t"))
res1 = sec_min(seconds)
res2 = sec_hour(seconds)
res3 = sec_day(seconds)
print("The number of minutes are :\t",res1,"\n","The number of hours are :\t ",res2,
      "\n","The number of days are :\t",res3)
