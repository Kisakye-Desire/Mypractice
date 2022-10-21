
#printing strings(Python strings are not terminated at the end)
from os import sep


print("Hello,Python!")
print("Desire")
print('Denise')

#Escape Characters(\n Newline,\t-Tab Space in words.)
print ("I am Born Again \n I am a child of God")
print ("I am a Ugandan \t I am a child of God")
print ("I am Born Again      I am a child of God")

#printing integers.(They are not put "".)
print(22) 


#Multiple strings./sentences on one line
print("Hello Daniella","Hello Jerry","I am tired")
#Using sep it appears in the middle
print("Hello Daniella","Hello Jerry","I am tired", sep="*")
#End operator which ends the string
print("Hello Daniella","Hello Jerry","I am tired", end="!!")
#Using both 
print("Hello Daniella","Hello Jerry","I am tired", sep="*" , end="!!!\n")

##print("Programming***Essential***in...Python)

print("Programming", "Essential", "in" ,sep="***", end="...")
print("Python")
