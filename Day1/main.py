# Created a greeting 
print("Welcome to the Band Name Generator.")
# ASk users for their city
city = input("What's the name of the city you grew up in?\n")
# Ask users for the name of their fav pet
pet = input("What's your pet's name?\n")
# Now generate a band name using infos of users
print("Your band name could be " + city[:4] + pet)
