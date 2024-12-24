print("1 - Add")
print("2 - Substract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("choose an operation: "))

if(option in [1,2,3,4]):
    num1 = int(input("Enter first number: "))
    
else:
    print("Invalid operation entered")