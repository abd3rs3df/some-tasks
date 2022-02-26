print('''
   welcome to the world game  |
   IF YOU WANT to know the play 
   enter the Capital for esch country |

''')
country = {"iraq":"baghdad", "egypt":"cairo","china":"beiging","jordan":"amman"}

score =0

cpital = input( ' do you want to start (Y/N) : ' )


if cpital.lower() == 'y' :
    for key in country:
        country_user=input(f'what is the capital of {key} : ')
        if country_user == country.get(key):
            print("correct")
            score+=1
        else:
            print("wrong answer")

    print( f"your score is : {score}")
    print('thank you to use world expert ! have a nice day ')
else:
    print("we hope to try the game later")

