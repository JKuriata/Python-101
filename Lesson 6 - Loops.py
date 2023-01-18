#Alrightyo time for the final lesson! Loops! Let's start with something simple, if I asked you to print your favourite drinks it may look something like this:
fav_drinks = ["tea", "hot chocolate", "orange juice"]
print(fav_drinks[0])
print(fav_drinks[1])
print(fav_drinks[2])
print("---------------")
#But what if I asked you to take a census of many peoples favourite drinks? printing them one by one would get tedious quickly. This is where loops come in.
favourite_drinks = ["tea", "hot chocolate", "orange juice"]

for drink in favourite_drinks:
    print(drink)
print("--------------")
#Boom, now you can add as many things to the list and they will all be printed!
#But lets run through that example a little. You should already understand the first line, you are creating a variable list. In the actual for loop you see that we call on "drink" you may be wondering why that works, it's because you are assigning the name there to the index. A lot of the time people will simply put "i" in its place (short for index) but it is preferable to give a name to make your code more readable. 
#You can also use this to print a range, for example:
for number in range(10):
    print(number)
print("--------------")
#or:
for number in range(5, 11):
    print(number)
print("--------------")
#or something a bit different
for number in range(2, 12, 2):
    print(number)
print("--------------")
#As you can hopefully see, the first two numbers still give the range while the third number decides how to count it, so that's counting every other number.

#Activity 1
#Create a list of 4 favourite films
#Use a for loop to show each film in the list
#Create a function called film_check() that checks if the 3rd film in the list is Ghostbusters.
#If it is, it should print “Wooo! Ghostbusters”. If it isn’t, it should print “booo, we want ghostbusters”
#---------------
#region - Answer
fav_flims = ["Amadeus", "Ghostbusters", "Leon the professional", "V for Vendetta"]

if fav_flims[1] == "Ghostbusters":
    print("Woo! Ghostbusters!")
else:
    print("Woo! Actual good movies!")
print("The list:")
for film in fav_flims:
    print(film)
print("--------------")
#endregion
#---------------

#Activity 2
#Look at how we made a loop to count to 10. Could you figure out how to count it backwards?
#---------------
#region - Answer
for number in range(10, 0, -1):
    print(number)
print("--------------")
#endregion
#---------------

#So you've created for loops, it's great for executing a task but what if you had to do that task a set number of times or until a certain criteria was met?
#Lets start with an example:
num = 0

while num < 10:
    num += 1
    print(num)
print("--------------") 
#Once the number reaches 10 it stops counting up!
#Now lets do something similar but with the random library! We want to assign a number we want to find and have random keep generating numbers until we get our number!
import random
rand_num = random.randint(1, 100)
my_num = 27
while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(1, 100)

print(f"You've found {my_num}")

#Activity 1
#Create a for loop that prints “hello world” 13 times. Now, convert this into a while loop that does the same job.
#---------------
#region - Answer
for count in range(13):
    print("Hello World")
print(("--------------"))

print_count = 0
while print_count < 13:
    print("Hello World")
    print_count += 1
print("--------------")
#endregion
#---------------

#Activity 2
#Create a variable, use a loop to generate a random number between 1 and 30 six times. For each random number generated, check if this number of divisible by 7 or not. (hint we've checked if divisible before)
#---------------
#region - Answer
for i in range(6):
    rand_num = random.randint(0,30)
    print(rand_num)
    if rand_num %7 == 0:
        print("Divisible by 7")
print("--------------")
#endregion
#---------------

# Activity 3
# Create a while loop to randomly cycle through a list of card suits until a given card suit is reached
cards = ["Diamonds", "Spades", "Clubs", "Hearts"]
#Decide on one suit you want to draw then have random pick one from your list using the .choice method (new). Then have a while loop print random suits from the list until it finds your suit.
#---------------
#region - Answer
cards = ["Diamonds", "Spades", "Clubs", "Hearts"]
rand_suit = (random.choice(cards))
my_suit = "Diamonds"
while rand_suit != my_suit:
    print(rand_suit)
    rand_suit = (random.choice(cards))
print(f"You've found {my_suit}")
print("--------------")
#endregion
#---------------

# Activity 4
# Create a loop that asks a user to input a number, then displays the multiplication table for that number up to 12.
#Make it loop so the user can input a new number.
#---------------
#region - Answer
printing = True
while printing:
    num = int(input ("Please input your number: "))
    for x in range(12):
        print(f"{num} * {x+1} = {(x+1) * (num)}")
    printing = False
    printing = True
print("--------------")
#endregion
#---------------