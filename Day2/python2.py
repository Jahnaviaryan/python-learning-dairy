# assignment shortcut
score = 10
score = score + 10
print(score)

# shortcut

score = 5
score += 10
print(score)

#String manipulation

name = "dave"
string = "my name is dave"           #for this example

#f string

name = "dave"
string = f"my name is {name}"
print(string)

name = "avaan is my name"
string = f"my name is {name}"
print(string)                  #change the value in variable name and it updates and gives the name


print(name.title())            # title keeps the starting letter of the words in caps

print(name.capitalize())      # All caps

# checking finding replacing
#checking

message = "I am larning python"  
print("python" in message)            # prints true 

if "python" in message  :           
     print("python is present")       # tried with if condition  
else:
     print("nope")

message = "I am larning python" 
print( message.startswith ("I") )     #True
print(message.endswith ("python"))     #True
print(message.endswith("I"))           #False

if message.startswith("I") and message.endswith("python") :
     print("true,the line is im learning python")
else:                                                                 # just to use and if and checking at once
     print("false,the line has somthing else")




#Finding
messages = " learning python for AI"
print(messages.find("AI"))
print(messages.count("Ai"))                    # Ai is not in the string given python is case sensitive returns 0
print(messages.count("AI"))                    #AI is in the string returns 1 means repeated one time

# Replacing 
new = messages.replace("AI","ML")
print(new)

"""find() - returns index (no storage needed)
replace() - returns new string (stire in variables) """

# student marks grading

score = int(input(" Enter the score: "))
if score >=90 :
     print(" A+  Excellent ,Passd ")
elif score >=80 :
     print(" A  Very Good ,Passed ")
elif score >=70 :
     print(" B+ Good ,Passed ")                         #if and elif
elif score >=60:
     print(" B Cane do better, Passed ")
elif score >=50 :
     print(" C+ Workhard ,Passed " )
elif score >=25 :
     print(" C please improve , Just Passed ")
else:
     print(" Failed ")

"""
Student Grading System

This program:
- Takes student name and marks as input
- Validates marks (must be between 0 and 100)
- Checks if the name contains letter 'a'
- Formats the name by replacing spaces with underscores
- Assigns grade based on marks
- Displays final student report

Concepts used:
- Input handling
- Conditional statements (if-elif-else)
- String operations (lower, replace, split)
- f-strings for formatted output
"""

name = input("Enter the Name of the Student : ")
marks = int(input("Enter the Marks of the Student : "))
if marks > 100 or marks < 0 :
    print( "invalid input ")
else:
    print(len(name))
    if "a" in name:
        name = name.upper()
        print("Conains A")
        clean_name = name.replace(" ","_")
    else:
        clean_name = name
    if marks >=90 :
     grade= " A+  Excellent ,Passd "
    elif marks >=80 :
     grade = " A  Very Good ,Passed "
    elif marks >=70 :
     grade = " B+ Good ,Passed "                         
    elif marks >=60:
     grade = " B Can do better, Passed "
    elif marks >=50 :
     grade = " C+ Workhard ,Passed " 
    elif marks >=25 :
     grade = " C please improve , Just Passed "
    else:
     grade = " Failed "

    if marks >25 :
          print("Pass")
    else:
          print("fail")

    print(f"""--------Student Report------- 
           Name           : {name}
           Formatted name : {clean_name}
           Marks          : {marks}
           Grade          : {grade}""")
        


