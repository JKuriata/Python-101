#Eyyy onto lists! Lists let you store data, much like pen and paper but with a few more fiddly things. Lets start with creating a bucket list - 
#Let's say this is your list -
    # - Finish python lessons
    # - Get a driving licence 
    # - Get a second piercing
    # - Thank programming teacher with expensive gift
#Just a random example! Let's make it into a python list
bucket_list = [
    "Finish Python lessons",
    "Get driving licence",
    "Get second piercing",
    "Thank programming teacher with expensive gift"
]
print(bucket_list)
print("-------------")
#You should notice a few things about making a list:
    #We use square brackets
    #After each item on the list, we use a comma
#Using that, make a list of your current top 3 favourite songs!
#---------------
#region - Answer
fav_songs = [
    "Father Finlee - Spence Hood, Justin Ray Stringer",
    "Blood upon the Snow - Hozier, Bear McCreary",
    "Woe to the People of Order - Cami-cat"
]
print(fav_songs)
print("-------------")
#endregion
#---------------
#What if I wanted to call only one thing from a list though?
print(bucket_list[3]) #remember, computer counts from 0
print("-------------")
#Much like variables, lists can be updated.
bucket_list[2] = "Get a tattoo"
print(bucket_list)