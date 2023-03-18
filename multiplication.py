import random

correct_answers = 0
incorrect_answers = 0
counter = 0

for i in range( 1, 10 ):
    multiplicand, multiplier = random.randint( 1, 12 ), random.randint( 1, 12 )
    product = multiplicand * multiplier 

    user_answer = int( input( "{} x {} = ".format( multiplicand,multiplier ) ) )

    if user_answer == product:
        print( "Correct!" )
        correct_answers += 1
    else:
        print( "Incorrect! {} x {} = {}".format(multiplicand, multiplier, product) )
        incorrect_answers += 1

    counter = i

print( "You got {} out of {}!".format( correct_answers, i ) )
