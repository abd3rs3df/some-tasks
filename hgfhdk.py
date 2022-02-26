import random
score = 0 #score of user
questions = 0 #number of questions asked
operator = ["+","-","*"]
number1 = random.randint(1,20)
number2 = random.randint(1,20)
print("You have now reached the next level!This is a test of your addition and subtraction")
print("You will now be asked ten random questions")
while questions<10: #while I have asked less than ten questions
    operator = random.choice(operator)
    question = '{} {} {}'.format(number1, operator, number2)
    print("What is " + str(number1) +str(operator) +str(number2), "?")
    answer = input()
    if answer ==(number1,operator,number2):
        print("You are correct")
        score =score+1
    else:
        print("incorrect")
