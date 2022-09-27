list_of_friend = ['sput', 'blanki', 'carnicero', 'pinguino', 'pikiblinder']

print(list_of_friend)

print(list_of_friend[-1])
print(list_of_friend[0])
print(list_of_friend[1])

# Elements of the list in a function

message1 = f"\tThe organization was conformed by {list_of_friend[0].title()},  {list_of_friend[1].title()}, {list_of_friend[2].title()}, {list_of_friend[3].title()}, {list_of_friend[4].title()}, and me (chatarrita:p)."

print(message1)

#Modified elements in a list

print(f"André mas conocido como {list_of_friend[0].title()}")
list_of_friend[0] = "André"
print(f"\t{list_of_friend[0].title()} mas conocido como Sput ")

# Adding elements in a list
list_of_friend.append("Chatarra")    #that add in the last position in the list

print(list_of_friend)

list_of_friend.insert(0, "Chatarra") #that add in the first position in the list

print(list_of_friend)

#delete elements in a list

del list_of_friend[6]

print(list_of_friend)

# Remove the last a element in the list but can work with them 

Thomas_Shelby_nick_name = list_of_friend.pop()

print(list_of_friend)

print(f"The nick name of the friend T.Shelvy was {Thomas_Shelby_nick_name}.")

my_nick_name = list_of_friend.pop(0)

print(list_of_friend)

print(f"My nick name was {my_nick_name}.")

# Radom insert

list_of_friend.insert(10, "csmáre")

print(list_of_friend)

#Explicit remove

list_of_friend.remove("csmáre")

print(list_of_friend)
