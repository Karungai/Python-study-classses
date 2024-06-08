#DATA TYPES 
salamu = "hello guys" #string
#scalar data types
pi = 3.14 #float
phone_number = 254712345678 # integer
isFemale = False #bo0lean
name = "Karungai"

#rules
# cannot name a variable with an integer
#do not use capital letters (creating classes, use snakecase instead. i.e name_name (USE AN UNDERSCORE))
# the names you cannot use to name variables i.e preservered words
print (phone_number)
print (salamu)

#INPUT
input ("Enter a number ") #this gets the users input
#has a return value
age = input ("Enter an age")
print (age)
dob = input("Enter your dob")
#dob = int(input("Enter your dob"))
age = 2024 - dob


#Concatination
#string concatination is when you add two strings
print("hello"+ name) #come out as one words
print ("hello "+name)
print ("age "+dob)
print (type(isFemale))

#METHODS
print (salamu)
print (salamu.upper())
print (salamu.find("e")) #index of the value that exists #always starts with zero # if the value is not found, it comes out with a negative
print ("guys" "salamu")
print (bool("salamu".find("ll")))
print (salamu.replace("guys", "boys"))

#Arithmetic Operators
print (2+3)
print (2**2) #find exponential, use 2*
print (22%3) #finding the remainder #thoat odesnt have a remainder, it comes as 0
print (22/3) #division

#Operator precedence #BODMAS
print (2*3/4)
print ((2*3)/4) #multiplication will happen first

#Comparison operators
print (6>4) #greater than
print (4!=3) #equal to
print (4>=3) #greater than or equal to
print (4<5) #less than
print (10<=5) #less than or equal to
print (10==10) #equal to

#LOGICAL OPERATORS
# and checks for two things: on the left and on the right. (true/false)
print (True and True)
print (False and True)
print (False and False)
print (3>1 and 4<6)
# or if one of the sides, left and right, will give us true
print (3>1 or 4<6)
print (False or True)
print (1==1 or 3>1)
print (1!=1 or 3>1)
#not does the opposite of the command given
print (not 3>1)
print (not 3<1)

#IF statements
#goes with an else
age = 15
if age  <= 18 :
    print ("you're too young")
else :
    print ("you can enter the club but do not drink")

age = 25
if age >= 18 :
    print ("you are of age")
else :
    print ("you can drink")

age = 18
if age  < 18 :
    print ("you're too young")
elif age <21 :
    print ("you can enter the club but do not drink")

age = 450
if age  < 18 :
    print ("you're too young")
elif age <21 :
    print ("you can enter the club but do not drink")
elif age <200 :
    print ("you can enter the club and drink")
else :
    print ("illegal age")

#LOOPS
#While and for
#be keen on the exit condition
#while is a double-edged sword
i = 0
#while
while i < 5 :
    print (i * "*")
    i = i + 1

#for
name = "Carol"
for character in name :
    print (character.capitalize())

#range
for number in range(1, 20):
    print (number)

#FUNCTION
#help avoid competition
def greet ():
    print ("hello my classmates")
greet () #this is how to invoke the function after you have created

#arguments
#first you need to define the parameters
def greet (name):
    print ("hello "+name)
greet ("Karungai")
greet ("Carol")

def greet (name):
    print (f"hello {name}")
greet ("Wacheru")
greet ("Ann")

greeting = greet("Kinuthia")
print (greeting)

def greet (name):
    return f"hello {name}"