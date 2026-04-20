# assigning printing 

f = "j"
b = "l"
p = f + " " + b
print(p)
len(p)
print(len)

#len and underline

firstName = "jaanu"
print(len(firstName))
long_dash = "-" * 12
print(long_dash)

#Strings and concat 
b = "l"
f = "j"
p = f + " " + b
print(p)
print(long_dash) 

#if else

age = 120
can_vote = age >= 18
if(age<18):
    print("cant bro minor")
else:
    print ("can")

    # Comparision

age = 120
is_18 = age >= 18
print(is_18)

#modulas

print(10%3)

#even or odd

n = 2
if(n%2==0):
    print("even")
else:
    print("odd")

#G of numbers

a = 1
b= 2
if(a>b):
    print("a is greater")
else:
    print("b is greater")

# G of numbers by user input

c = (input("enter C "))
d = (input("enter D "))
if c>d:
    print("C is OG")
else:
    print("D is OG") 

# and using

age = 12
license = True
canDrive = age >= 18 and license 
print(canDrive) 

# len check 

name = "jahanvi"
print(len(name))
if len(name) <= 5:
    print("short name")
else:
    print("Long name")

#password creationg

password = "dave@31pythON"
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char in "@#$%^&*" for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password) :
    print("strong")
else:
    print("weak")

#input password from user

password = input("Enter password : ")
has_upper = False
has_lower = False
has_special = False
has_digit = False

for char in password :
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif char.islower():
        has_lower = True
    elif char in "!@#$%^&*()":
        has_special = True

if len(password)>=8 and has_upper and has_special and has_digit and has_lower :
    print ( "strong ")  
else:
    print ("weak")   

password = input("Enter password : ")
has_upper = True
has_lower = True
has_special = True
has_digit = True
if len(password)>=8 and has_digit   and  has_lower and has_upper and has_special :
    print("strong")
else:
    print("weak")

