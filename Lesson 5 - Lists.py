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
print("-------------")
#But what if you decided, actually you still want to get a second piercing. You can use a method!
bucket_list.append("Get a piercing")
print(bucket_list)
print("-------------")
#What if after watching your friend get a tattoo you decide maybe it's too painful for you?
bucket_list.remove("Get a tattoo")
print(bucket_list)
print("-------------")
#There are a good few methods for lists, some of these are -
    # .remove()
    # .append()
    # .reverse()
    # .sort()
    # .count()
    # .extend()
    # .pop()        (removes last thing on the list)

#Alright, you know the drill, lets put what you've learned to the test!

#Activity 1 
#Create a list of your favourite website (3 of them), and then add another two once you’ve created the list. Then remove the last website.
#------------------------------
#region - Answer 
fav_sites = ["w3schools", "youtube", "facebook"]
fav_sites.append("instagram")
fav_sites.append("ign")
fav_sites.pop()
print(fav_sites)
print("-------------")
#endregion

#Activity 2
#Research the listed methods and make an example using each.