hour=input("Enter hour: ")
rate_per_hour=input("Enter rate per hour:")
try:
    h=int(hour)
    rph=float(rate_per_hour)
    if h<=40:
        pay=rph*h
    else:
        pay=40*rph+(h-40)*1.5*rph
    print("Pay :",pay)
except:
    print('Error,please enter numeric input')
