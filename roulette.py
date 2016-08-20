#A roulette game!
#Choose a number between 1 and 12 and earn 12 x your bet if you get it
#Choose a colour between red and black and earn 2 x your bet if you get it
import random 
def roulette():
    your_chips = 10
    while True:
        number_bet = float(input("You have " +str(your_chips)+" chips. Place your next bet on your number: "))
        num_roll = random.randint(1, 12)
        colour_roll = random.randint(0,100)
        
        your_number = float(input("Okay, which number do you choose (1-12)? "))
        colour_bet = float(input("How much would you like to put on a colour? "))
        your_colour = (input("Red or Black? Type in your choice: "))
        if your_number == num_roll:
            your_chips = your_chips + number_bet*12
            print ("Congratulations! You got a "+str(num_roll)+"!")
        elif your_number != num_roll:
            your_chips = your_chips - number_bet
            print ("The number is... "+str(num_roll) +"! Unlucky")
    

        if colour_roll >49 and your_colour[0] == ("R" or "r"):
            your_chips = your_chips + colour_bet
            print ("The colour is...Red, you nailed it.") 
        if colour_roll < 50 and your_colour[0] == ("B" or "b"):
            your_chips = your_chips + colour_bet
            print ("The colour is...Black, you got it.")
        else:
            your_chips = your_chips - colour_bet
            print ("Wrong colour, sorry.")
        if your_chips <= 0.0:
            print ("Game Over!")
            break  
            
