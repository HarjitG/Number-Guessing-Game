from random import seed        #random library used to create random number generator
from random import randint
count_wins = 0                 # counters initialised to count number of games won and lost
count_lost = 0
a=0                            # Variables a,b will be used to count number of guesses later
b=0
rand=0
un = "_"
sp = " "

#####################  Function asking user if they want to play again or leave
##################### This function is called in next function when the user finishes the game
def play_again():

        y= input('\nWould you like to play again y/n ?') # if function vald input of 'y' to restart game
        if y == 'y':
            play_game() # play_game function will be called if true
        else:
            print("-----------------------------")
            print ("\nGAME OVER")
            print("\nGames lost:" + str(count_lost))
            print("Number of Guesses: ",str(b))
            print("Number of correct guesses:" + str(count_wins))
            print("-----------------------------")

            quit()        # quit function exits the programme after user no longer wants to play

################################## MAIN FUNCTION #############################################

def play_game():

    global rand_          # Here we declare global variables that exist everywhere in the programme
    global count_wins
    global count_lost
    global a
    global b

    rand_=randint(1,10)     # randint function generates random number between two intervals

    for i in range (1,4):  # range(1,4) allows us to process 3 guesses, seen as 1,2 and 3
        while True:
            try:            #ensure valid numerical input using "int" function
                print(un*40)
                number= int(input('Enter a number between 1 and 10: \nYou have entered: '))
                if (number >=1 and number <=10):
                    print(un*40)
                    a=a+1
                    b=a            # a variable counting number of valid guesses user has made
                    break          # break allows us to proceed to next section only after valid output from user
            except ValueError:
                        print('Please enter a whole number')

        if( i ==3 and number != rand_): # case for user has run out of attempts
            print("\nToo many attempts, you've lost, the answer was: " + str(rand_))
            count_lost= count_lost +1    # game has been lost so add 1 to the lost counter
            play_again()    # calls this function which asks user if they want to play again


        elif number < rand_: # checking if users guess is lower than the game number
            print ("\nIncorrect: " + str(3-i) +" attempts remaining\n")
            print("This number is too small") # Telling user their guess is too small


        elif number > rand_: # checking if users guess is higher than game number
            print("This number is too big")
            print ("\nIncorrect: " + str(3-i) +" attempts remaining\n") # number of attempts remaining
            print("-----------------------------")


        elif (number == rand_ and i!=1): # if the user has guessed correctly on 2nd or 3rd attempt
            print ("Congratulations you guessed the correct answer in " + str(i) +" attempts ")
            count_wins = count_wins +1 # user has won game so adding 1 to games won counter
            print("-----------------------------")
            play_again() # calls this function which asks user if they want to play again


        elif (number == rand_ and i==1): # if the user has guessed correctly on their first attempt
            print ("Congratulations you guessed the correct answer in " + str(i) +" attempt ")
            count_wins = count_wins +1
            print("-----------------------------")
            play_again()

play_game()