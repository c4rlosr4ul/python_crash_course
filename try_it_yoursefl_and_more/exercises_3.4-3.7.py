#   3.4 Guest list 

dinner_guest_list = []
dinner_attendees_list = []
dinner_no_show_list = []

message0 = "Hi :D, I'm a Carlos Raúl, nice to meet you. What's your name? > "

guest_prospect = input(message0)

message1 = f"Hello {guest_prospect}, are you invited to my dinner that will be this weekend, do you accept? :D Write 'Yes' to confirm or 'No' to reject. > "

dinner_guest_list.append(guest_prospect)

answer_to_the_invitation = input(message1)

while answer_to_the_invitation != "Yes" or answer_to_the_invitation != "No":
    if answer_to_the_invitation == "Yes":
        
        person_who_accepted_the_invitation = guest_prospect
        dinner_attendees_list.append(person_who_accepted_the_invitation)
        
        message2 = f"Thanks, {person_who_accepted_the_invitation.title()}. I will be happy to receive you at my house this Sunday at 6:00 pm"

        print(message2)
        exit()

    if answer_to_the_invitation == "No":

        person_who_did_not_accepted_the_invitation = guest_prospect
        dinner_no_show_list.append(person_who_accepted_the_invitation)
        
        message3 = f"Well, {person_who_did_not_accepted_the_invitation.title()}. It will be for the next one." 

        print(message3)
        exit()
        
    answer_to_the_invitation= input("Please enter a valid answer :P, Try again... > ")
        








