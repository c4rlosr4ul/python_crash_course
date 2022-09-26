file_containing_the_password = open("the_password.txt")
password = file_containing_the_password.read()

your_supous_password = input('Enter the password, rctmáre... ')

while your_supous_password != password:

    if your_supous_password == '69':
        the_phrase = input('OpiO, Cj? ')
        if the_phrase == 'Hugu?':
            print('Access granted for cheroka...')
            exit()

    your_supous_password = input("Incorrect password..., Try again... ")

print('Password correctly entered, access granted...')