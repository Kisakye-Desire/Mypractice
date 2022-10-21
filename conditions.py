
#Equality operator
print(10==10)

#Non-equality operator
print (10 != 5)
print (10 != 10)

#Comparison operators
print(10 <=5)
print(10 <=5)
print(10 < 5)

number1=5
number2=6

if number1 > number2:
    print(True)

else:
     print(False)


#Asking user input
print("*" * 20)
number1=int(input("Enter the first number.."))
number2=int(input("Enter second Number..."))

if number1 > number2:
    print(number1,'is greater than',number2)

else:
     print(number1,'is less than',number2)
print("*" * 20)

#Comparison == and use of else if(elif) the (if,else,elif should all be on one line)
print("*" * 20)
num1=int(input("First number.."))
num2=int(input("Second Number..."))

if num1 == num2:
    print(num1,'is equal to',num2)

elif num1 >num2:
     print(num1,'is greater than',num2)

else:
    print(num1,"is less than",num2)
print("*" * 20)