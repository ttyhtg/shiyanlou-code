x=0
while x<=99:
    x = x+1
    if (x%7==0) or (x%10==7) or (x//10==7):
        continue
    else:
        print(x)
