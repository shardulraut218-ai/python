num1 = float(input("Enter a number : "))
num2 = float(input("Enter Another number : "))

operation = input("Operation : ")

if operation == "+" :
    print(num1 + num2)

elif operation == "-" :
    print(num1 - num2)

elif operation == "*" :
    print(num1 * num2)

elif operation == "/" :
    if num2 == 0:
        print("Division cannot be done")
    else:
        print(num1 / num2)


elif operation == "/" :
    print( num1 / num2 ) 

elif operation =="%" :
    print(num1 % num2)   

elif operation =="**" :
    print(num1 ** num2)       
else :
    print("Invalid Operation !!")


          
        
