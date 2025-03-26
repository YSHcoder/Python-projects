def calc(a,b,c):
    a=int(input("Enter your number first:"))
    b=(input("+,-,*,/,%"))
    c=int(input("enter your second number:"))
    if b=='+':
        return a+c
    elif b=='-':
        return a-c
    elif b=='*':
        return a*c
    elif b=='/':
        if c==0:
            print("cannot divided by 0")
        elif a==0:
            print("cannot divided by 0")
        else:
           return a//c
    elif b=='%':
        return a%c
total=calc(input,input,input)
print(total)

