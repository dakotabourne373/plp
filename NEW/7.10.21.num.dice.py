"""
Function should do three things:
A. take in user input (telling the user the range in which they can guess) (NOTE: obviously make it so if they guess outside the range, it tells them to try again)
B. generate random input
C. tell user whether or not they're input was correct or not
"""
def number_guesser(): 
    input("NUMBER GUESSER!!") 

"""
dice_roll should do three things:
A. ask user how many sides they want on each dice
B. ask user how many dice they want to roll
C. return result of roll(s)
"""
def dice_roll():
    input("DICE ROLLLLLL")

"""
What I did in here is really ugly but it gets the job done, don't take from me!!!
When testing you can use number or n and dice or d
"""
def main():
    while(True):
        route = input("Do you want to Guess the Number or roll some dice? (number/dice)\n")
        if(route == "number" or route == "n"):
            number_guesser()
            break
        elif(route == "dice" or route == "d"):
            dice_roll()
            break
        else:
            print("\n\nIncorrect input, try again\n")

if (__name__ == '__main__'):
    main()