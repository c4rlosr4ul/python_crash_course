from string import punctuation #Para emplear los símbolos reservados en python

#1. Getting Started
#1.1 Basic Python 

print('This is a text ' + str(int(3.1415)))
print('This is a example')
print('Insert a number with decimals')
a = input()
if a == '69.0' :
    print('Your number is ' + str(float(a)))
    print('Hey! OPIO OUO')
else: 
    print('Your number is ' + str(float(a)))
    print(':D XXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    print('GAME1: Complete the word')
    print('Mas ____ lokita...')
    word = input()   
while word !='bien':
    if word != "bien":
        print('Nada mano, completa de nuevo')
        word = input()   
    
print('Ah... sape...')

print('The number of characters of <rcsmáre> is ')
a = '<rcsmáre>'
print(len(a))
print(':D XXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    #I use len() and input 

#1.2 Created the first program of the introduction
comillas = {"'"} 

print('GAME2: I am thinking of a number') 
print('Try to guess the number')
print('Tip: Is a integer number')

number_i_thinking = 123
number_you_think = int(input('I' + str("'") + 'm'+ ' thinking is... :'))

while number_you_think != number_i_thinking:

    if number_you_think > number_i_thinking:
        print('No, it' +str("'") + 's less than that... Keep trying.')
        number_you_think = int(input())
    else:
    #Then number_you_think < number_i_thinking
        print('No, it' +str("'") + 's more than that... Keep trying.')
        number_you_think = int(input())

print('Yes! Sure...')
print('You' + str("'") + 're ' + 'a wizard... :o' )