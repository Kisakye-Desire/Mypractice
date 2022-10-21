#printing integers(They are not put in "")
print(10)
print(2)
print(3)
print(-23)

#Floats-Floating numbers
print(10.2)
print(.3)
print(-0.6)

#Octa decimalBase(use zero then o and the number you want to print(0o5))
print(0o123)

#Hexadecimal Base(use zero then x and the number you wish to print(0x5))
print(0x123)

#Printing complicated numbers like 300,000,000
print(3e8)

print(3e-2)

#Data manipulation

print(8/3)
print(8//3)
print(8/3)
#multiplication
print(2*3)

#printing exponets
print(2**3)
print(2**5)

#Rounding off(print(round(digits to roundoff,then decimal places you want.)))
print(round(2/3,2))

#Name
#Bread
#Unit Cost
#Quantity
#Total Cost

unit_cost=6000
quantity=5

total_cost=quantity*unit_cost
print(total_cost)


#Asking user for input
name=input("What is your name?")
item=input('What item are you taking?')
cost=float(input("What is your unitcost?"))
amount=float(input("What is your quantity?"))

total=amount*cost
print(total)
print('*' * 20)
print("Hello",name,"Here is your bill.")
print('Unit cost',cost)
print('Total cost',total)
print('Thank you for shopping with us.')
print('*' * 20)



#Helps you know the datatype and specify
our_value=int(input("Enter anything"))
print(our_value)
print(type(our_value))

our_value1=float(input("Enter anything"))
print(our_value1)
print(type(our_value1))