#So. We've already learned some Variable stuff but lets make sure you fully understand it!
#Activity 1 
#Write a conditional statement that checks the ages of cinema goers, and display the ticket prices:
#- Child (below age of 18): £8
#- Adult (18+): £10.95
#- Senior (60+): £7.50
#Hint - no function needed, just a conditional.

#----------
#region - Answer
import random
age = random.randint(1,99)
print(f"Your age is {age}")
if age < 18:
    print ("The price will be £8")
elif age < 60:
    print ("The price is £10.95")
else:
    print ("The price is £7.50")

print("-----------------")
#endregion
#----------

#Lesson 2 already covered funtions so this should hopefully not be too difficult. 
#Function recap -
    #Like boxes
    #Can be called by identifiers (name)
    #Breaks down code into smaller chunks
    #REUSABLE :)
    #In-built functions -
        #print()
        #input()

#An example of a simple function:

def grind_beans():      #Declaring new function
    print("Grinding beans for 20 seconds.")

grind_beans()           #Running the function
print("-------------")
#Perameters are the things in the brackets and give you the ability to call on different data inputs. 
#Example from lesson 2:
def cash_withdrawal (cash_amount, acc_number):
    print(f"Withdrawing £{cash_amount} from account {acc_number}")

cash_withdrawal(300, 450230958)

print("-------------")
#Instead of using variables we used perameters, this is generally preferred in programming. 
#It means we can reuse the code much easier.
cash_withdrawal(500, 235056382)
print("-------------")

#Lets use another example from lesson 2 and use perameters instead of variables.

def coffee_order (size, type):
    print(f"So you want a {size} {type}?")
coffee_order("large", "latte")
print("-------------")

#Lets introduce another in-built variable! Return
def add_up(num1, num2):
    return num1 + num2
print(add_up(2,5))
print("-------------")

#Activity 1 
#Here's an example of a function that includes a parameter.
#Parameters are responsible for functions being able to work on different data inputs. Edit the snippet below to include two or more parameters and a running order count updated when the function is called :
#Hint - Remember that Python is whitespace dependant 
order_count = 0
def take_order (topping):
    global order_count
    print (f"Pizza with {topping}")
order_count += 1
take_order ("Pineapple")
print("-------------")

#---------------
#region - Answer
order_count = 0 
def take_order(size, topping):
    global order_count
    print(f"{size} pizza with {topping}")
    order_count += 1

take_order("Large", "pineapple")
take_order("Small", "ham")
take_order("Medium", "double cheese")
print(f"order count: {order_count}")
print("-------------")
#endregion
#---------------

#Activity 2
#Cash machine time. Let’s create one that :
    #Takes an input of pin number and amount
    #Prints dispensing cash if the pin number is correct and there’s enough money to withdraw
    #Displays the new bank balance

#--------------
#region - Answer
pin = input("Please enter your pin : ")
current_balance = random.randint(1, 10000)
if pin == "1234":
    print(f"Current Balance: £{current_balance}")
    withdrawing = input("How much would you like to withdraw? £")
    current_balance -= int(withdrawing)
    print(f"Balance after withdrawal: £{current_balance}")
else:
    print("Check pin")
print("--------------")
#int is to make python recognise withdrawing as an interger not a string.
#endregion
#--------------

#You can also declare the variable with a boolean

coffee_grinding = False

def grind_beans():
    global coffee_grinding
    if coffee_grinding:
        print("Stopping the grind")
        coffee_grinding = False
        print("Grinding is now false")
    else:
        print("Grinding is about to begin")
        coffee_grinding = True
        print("Grinding is now true")
grind_beans()       #The coffee is not grinding
grind_beans()       #The coffee is grinding