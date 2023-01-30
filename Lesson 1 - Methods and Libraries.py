#There are a few built in data types in python, they are:
    #Strings - text
    #Integer - whole numbers
    #Floating points - decimals
    #None - nothing
    #Boolean - true or false
#You can apply various methods to these data types, first we'll focus on strings
#To print your first string enter the below into your terminal
print("Hello World!")
#Congrats, from there you can begin to play around with some methods! 
#Say you wanted to find a specific part of a string, you could use the method below:
print("hello"[1]) #note- the computer counts from 0
#When ran this will print out "e" as that is the first letter (for the computer)
#Let's check out a few other methods:
    #len  (the length of a string)
print(len("Length"))
    #lower()  (making the string lower case)
print("LowEr".lower())
    #strip()  (Removes unnecessary spaces at the start)
print("    Strip".strip())
#The two examples above are dot notation which is simply object.method . It has a dot in it. Programmers are not all that creative
#There are other methods you could play around with such as:
    #upper()  (printing in caps)
print("Upper".upper())
    #capitalize() (note American spelling)
print("capitalize".capitalize())
    #count()  (count the number of times a letter appears in the string)
print("count".count("o"))
    #find()  (find a specific letter in the string)
print("find".find("f"))
    #replace()  (replace a specific thing)
print("replace".replace("place", "mix"))
#As seen above some methods require perimeters (the things in the brackets after the method)
#As you can see, methods are simply a way to manipulate the object (strings in this case)
#----------------------------------------------------
#Next up - Libraries
#You actually already know a library, and have been using it a lot - "print" is a built in library!
#So what about not built-in libraries? 
#Honestly it is incredibly simple, it is like downloading a new font or brush set. It gives you some extra tools to play with. There are many many libraries and you can find them easily online.
#Unlike downloading new brush patterns, importing libraries is far more easy as you will see below
#When you use a library it is generally good practice to place the import at the top of the document.
#I will ignore that last step to not make this document confusing. 
import random
#So lets try to use something from this library!
print(random.random())  #Look a .random() method!
#Try this one out, what does it do?
#It generates a random floating point between 0 - 1!
#Alright so what else can we make it do?
print(random.uniform(1, 10))  #What's the method here?
#Now instead of giving me a number from 0-1 it gives me a number from 1-10
#But how often do we want random decimals?
print(random.randint(1,10))
#This instead generates an integer between 1-10
#And I bet you're thinking, but when would I need a random number?
# BONK! Always! It's how I coded my villain giving a random speech during battle and how I made the damage random!
#Ok but say you knew you only needed certain methods from the random library?
#You can import just them! 
# from random import random, randint, uniform
# print(random())
# print(uniform(1,10))
# print(randint(1,10))
#(You will have to try this in a new .py document as this one already has random imported on line 43)
#Boom you've done lesson 1/6 in the python course!

#Final note - You can mix and match methods. e.g.
print("All around the world"[7].upper())
#This will print the 8th character (remember, computer counts from 0) in upper.
