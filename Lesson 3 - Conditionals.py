#And we're onto conditionals! If/else. If you are reading this, good job! Else... how do you know what I'm saying?
#Say, if there was music playing in a club how would you feel about the music?
#Well I suppose it depends!
music = "other"
if music == "other":
        print("Aw yeee, random murder jams!")
elif music == "no music":
        print("Put on my jams!!")
else:
        print("What even is this?")
print("-----------")
#Other and no music are two conditions, else does not require a condition, it is simply for any other input.
#Take the above example and imagine a user could edit whatever music is input. What would happen if they input "Other"? 
#The code would return, "What even is this?" because the input doesn't match your conditional. Can you fix this using a method?
#---------------
#region - Answer
music = "Other"
if music.lower() == "other":
        print("Aw yeee, random murder jams!")
elif music.lower() == "no music":
        print("Put on my jams!!")
else:
        print("What even is this?")
print("-----------")
#endregion
#---------------
#You may have noticed this by now but Python is whitespace dependant (aka. tabs and spaces matter. Unfortunately)
#Another notable part of this code is that we use a double "==", this is a comparison operator (remember from last lesson? Operators == mathsy things). Lets see some more comparison operator 
    # != == Not equal
    # >= == Greater or equal
    # > == Greater
    # <= == Lesser or equal
    # < -- Lesser

#Activity 1
#Create a variable called age. Write an if statement that logs “Yes I can serve you” if age is greater than 17 and else logs “You aren’t old enough”.
#---------------
#region - Answer
age = 18
if age > 17:
    print("Yes I can serve you")
else:
    print("You aren't old enough.")
#endregion
#---------------
#But you can also have multiple variables!
place = "Manchester"
weather = "Cloudy"

if place == "Manchester" and weather == "Sunny":
    print("OMG the sky is broken!")
elif place == "Manchester" and weather == "Cloudy":
    print("Seems about right.")
else:
    print("Where am I? Who am I? Why do I care so much about the weather?")
print("-----------")
#Another thing you may have noticed is that we DON'T use the double == in the variables. That's because we are assigning value!

#Activity 2
# Take your previous conditional and add a variable called country. Now check if age > 17 and country == “UK”
#---------------
#region - Answer
age = 18
country = "UK"
if age > 17 and country == "UK":
    print("Yes I can serve you")
elif age > 17 and country != "UK":
    print("Please show a recognisable form of ID.")
else:
    print("You aren't old enough.")
print("-----------")
#endregion
#---------------
#Lets walk through another example! 
day = "Saturday"
#in this statement Saturday is true
if day == "Saturday" or day == "Sunday":
#Sunday is false
    print("It's the weekend!")
#It still prints because one of the variable returns true
else:
    print("When's the weekend?")
print("-----------")
#This is called a logical operator. "or" will return true if any one variables returns true; But "and" will only return true if both variables return true.
#So in the weather example we used an "and" logical operator. This meant both variables had to return true for it to return the desired outcome.
#In the example directly above we used if which only required one statement to be true.

#For the next activity you will need to use a modulus symbol "%" this is an operator that returns the remainder of a division. So if you divide 5 by 2, the remainder would be 1. 

#Activity 3
#Create a variable called password.
#Check how many letters are in the password, if there are less than 8 print that the password is too short. Otherwise print the password.
#---------------
#region - Answer
password = "Mango"
print("Password lenght:", len(password))
if len(password) < 8:
    print ("Password is too short.")
else:
    print (password)
print("-----------")
#endregion
#---------------

#Activity 4
#Create a variable called num.
#Check if the variable is divisible by 3 or 5. If it is print “This number is divisible by 3 or 5” to the console. Otherwise log “This number is not divisible by 3 or 5.
#---------------
#region - Answer
num = 24
print (f"Your number is {num}")
if num%3 == 0 or num%5 == 0:
    print ("This number is divisable by either 3 or 5")
if num%3 == 0 and num%5 == 0:
    print ("This number is divisable by 3 and 5")
print("-----------")
#endregion
#---------------

#Activity 5
#Create a variable called num.
# If num is divisible by 3 print “fizz”, if it’s divisible by 7 print “buzz”, if it’s divisible by both 3 and 7 print “fizz buzz”. Otherwise print num.
#---------------
#region - Answer
num = 21
print (f"Your number is {num}")
if num%3 == 0 and num%7 == 0:
    print ("Fizz Buzz")
elif num%3 == 0:
    print ("Fizz")
elif num%7 == 0:
    print ("Buzz")
else:
    print ({num})
print("-----------")
#endregion
#---------------

#Activity 6 (hint in lesson 1)
#Create a variable called word that takes a string.
#Create an if statement that checks if the last letter is the same as the first. If it is return true, otherwise return false.
#---------------
#region - Answer
word = "rover"
if word[0] == word[4]:
    print("The first and final letter are the same")
else:
    print("The first and last letter are not the same")
print("-----------")
#endregion
#---------------

#Activity 7
#Create two variables called num1 and num2.
#Create an if statement that checks if the result of the sum is even. If it is, return a success message.
#---------------
#region - Answer
num1 = 4
num2 = 4

if (num1+num2)%2 == 0:
    print("These numbers are divisable by 2!")
else:
    print("These numbers are not divisible by 2")
print("-----------")
#endregion
#---------------

#Activity 8 (Hard)
#Create a variable called time, a variable called place_of_work and a variable called town_of_home
#Create an if statement that prints where someone is at times of the day. E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at work.
#---------------
#region - Answer
time = 7
place_of_work = ""
place_of_home = ""
if time == 7:
    place_of_work = "I am not at work"
    place_of_home = "I am at home" 
elif time == 8:
    place_of_work = "I am commuting"
    place_of_home = "I am commuting" 
elif time == 9:
    place_of_work = "I am at work"
    place_of_home = "I am not at home"
else:
    print ("I am commuting")
print(place_of_work and place_of_home)
print("-----------")
#Note - If you managed this, I am shooketh. If not, don't worry a lot of this wasn't really covered. 
#Quick run through. Place of work is set to a string in the variable, the string that is printed is then dependant on the time.
#endregion
#---------------

#One last thing
#Truthy and Falsey (Not dwarves from Snow White). Condiotions can be True or False (for some reason referred to in a cute nickname)
print("What is your name?")
name = input()
if name:
#If there is an input in name do this
    print(f"Hello {name}, how are you?")
else:
    "TELL ME YOUR NAME"
#Falsey values are:
    #Empty strings
    #Value of 0
    #Floating point .0
#Everything else is Truthey
#Basically with this code, the user has to make SOME input.

#Aaaaaand that's it! Give yourself a pat on the back, this one was hard!
