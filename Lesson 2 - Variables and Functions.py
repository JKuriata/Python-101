#This lesson will focus on variables and functions. Variables are labels we can put on things, we can store those labels in functions.
# To explain with a similie, funtions are like boxes. You store things inside the boxes to take out later. Say you have a box called electronics. Inside you have stored HDMI cables, chargers, random ethernet cables and a wi-fi extender. You then decide you want to set up a new entertainment centre. Instead of having to find each thing individually you can simply find the box. That's what functions are. 
#An example of a variable would be:
greeting = "hello"
#While a function would be:
def greeting():
    print("Hello!")
#Now that we have defined greeting as "Hello" we do not need to print("hello"), instead we can call the function we made.
greeting()
print("-----------")
#Another thing functions can do is take new data which is the equivelant of you stuffing another cable into the "electronics" box. 
#So when would you like to use a variable? When you need to reuse code. A good example of this is a cash machine. 
def cash_withdrawl (cash_amount, acc_number):
    print(f"Withdrawing £{cash_amount} from account {acc_number}")

cash_amount = 300 
acc_number = 50443497

cash_withdrawl (cash_amount, acc_number)
print("-----------")
#So now instead of having to tell it to print the whole script you can adjust just the cash amount and account number. 
cash_amount = 250 
acc_number = 58934893

cash_withdrawl (cash_amount, acc_number)
print("-----------")
#As you can see now it prints the new amount and number.
#Let's do another example with different formatting just in case:
def say_something(something):
    print(f"{something}")

say_something("Hello")
say_something("Goodbye")
print("-----------")
#Try to make your own function taking an order in a coffee shop. Take the size and type of drink. (Look to the cash withdrawl for an example)
#---------------
#region - Answer
def coffee_order (size, type):
    print(f"So you want a {size} {type}?")
size = "large"
type = "chai tea"
print("-----------")
#endregion
#---------------

coffee_order(size, type)
#You can use either format to print out what you want as shown below:
def cash_withdrawal (cash_amount, acc_number):
    print(f"Withdrawing: {cash_amount} from {acc_number}")

w_amount = 100
account_num = 124573242

cash_withdrawal (cash_amount, acc_number)
cash_withdrawal (400, 480137495)
cash_withdrawal (582, 743829573)
print("-----------")
#You may have noticed that inside of the functions I have used the letter f before the string. This is an alternative to using .format() a method which allows the connection with the inputs. Using the shorthand f is far more accepred now.
#Of course functions aren't limited to strings:
def add_up(num1, num2):
    return num1 + num2

print(add_up(7,3))
print(add_up(2,5))
print("-----------")
#A few additional notes -
    #Mathsy symbols are called operators
    #If you wish to use quote marks inside a string you can use \ to ignore the next letter. This is called character escaping and can also be used for \t for tab and \n for new line (poss. \r\n)
    #To comment out/in text in the terminal yous can use ctrl and foreward slash.
    #You can also select a lot of lines and tab them out or tab them in with shift tab.
    #You may have noticed already but in python we use snake case which is the underscore instead of spaces

#Activity 1:
    #Create a program that stores someone’s name, age and favourite colour that prints these in a complete sentence.
    #Try this yourself before looking at the answer below!
    #If your answer isn't exactly the same but works, it's correct :)
#---------------
#region - Answer
def print_details(name, age,fav_col):
    print(f"{name}\'s {age} years old and their favourite colour is {fav_col}")
print_details("Jude", "18(+8yrs exp)", "Blue/Yellow")
print("-----------")
#endregion
#---------------

#Activity 2:
    # Create a program that stores what you ate/will eat today for breakfast, lunch and dinner, print these.
    # Update each of these variables to what you will eat tomorrow, print these.
#---------------
#region - Answer
def nom_noms():
    print(f"Breakfast = {breakfast}")
    print(f"Lunch = {lunch}")
    print(f"Dinner = {dinner}")
breakfast = "Porridge"
lunch = "Egg bread sandwich"
dinner = "Full on Christmas dinner"
nom_noms()
print("------")
breakfast = "Full English"
lunch = "Bacon sandwich"
dinner = "Roast chicken"
nom_noms()
print("-----------")
#endregion
#---------------

#Activity 3:
    #Create a program that calculate the number of days you've been alive, and print this out. 
    #This requires researching a new library so don't worry if you can't figure it out.
#---------------
#region - Answer
from datetime import date
d0 = date (1996, 10, 27)
d1 = date (2022, 12, 5)
delta = d1 - d0
print(delta.days)
print("-----------")
#endregion
#---------------