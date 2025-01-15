print("1 - Add")
print("2 - Substract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("choose an operation: "))

if(option in [1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = int(input("Enter seccond number: "))
    
    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2

    
else:
    print("Invalid operation entered")
    
print("The result of the operation is {}".format(result))
