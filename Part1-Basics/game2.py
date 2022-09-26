print('GAME2: I am thinking of a number') 
print('Try to guess the number')
print('Tip: Is a integer number')

number_i_thinking = 123
number_you_think = int(input('\tI' + str("'") + 'm'+ ' thinking is... : '))

while number_you_think != number_i_thinking:

    if number_you_think > number_i_thinking:
        number_you_think = int(input('\tNo, it' +str("'") + 's less than that... Keep trying: '))
    else:
    #Then number_you_think < number_i_thinking
        number_you_think = int(input('\tNo, it' +str("'") + 's more than that... Keep trying: '))

print('Yes! Sure...')
print('You' + str("'") + 're ' + 'a wizard... :o' )
print('Game over, congratulations...')