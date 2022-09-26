list_of_friend = ['sput', 'blanki', 'carnicero', 'pinguino', 'pikiblinder']

print(list_of_friend)

print(list_of_friend[0])
print(list_of_friend[1])
print(list_of_friend[2])
print(list_of_friend[3])
print(list_of_friend[4])

message0 = f"the organization was conformed by {list_of_friend[0]},  {list_of_friend[1]}, {list_of_friend[2]}, {list_of_friend[3]}, {list_of_friend[4]}, and me (chatarrita:p)."
    #The f"..." is necesaru for insert into parts of list
print(message0)

message1 = f"\tThe organization was conformed by {list_of_friend[0].title()},  {list_of_friend[1].title()}, {list_of_friend[2].title()}, {list_of_friend[3].title()}, {list_of_friend[4].title()}, and me (chatarrita:p)."

print(message1)