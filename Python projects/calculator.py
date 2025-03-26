num1=int(input("enter your first number:"))
print("1. Add")
print("2. sub")
print("3. multiply")
print("4. divide")
print("5. modulo")

option=int(input("choose an operator :"))
if (option in [1,2,3,4,5]):
    num2=int(input("enter your second number:"))
    
if (option==1):
        result = num1+num2
elif (option==2):
        result = num1-num2
elif (option==3):
        result= num1*num2
elif (option==4):
        result=num1//num2

elif (option==5):
    result=num1%num2
else:
    print("invalid value")

print("the result of the operator is {}".format(result))


    

