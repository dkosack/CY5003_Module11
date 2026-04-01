""""
Sean Hegarty
CY5003
Spring 2026

These collection of functions are helper functions for a game of battleship.
One function is for checking age, to make sure the player is old enough.
The second one is to check the x axis of a player's guess, and the last one
is to check the y-axis of a player's guess. 
"""

def age_check(age):
    """
    This function checks age of the player with age as a parameter
    Intended for the start of the game
    """
    if not isinstance(age, int):
        # if statement to check is the input is an integer
        raise TypeError("Age must be an integer") # raises error if wrong type
    if age < 7 or age > 100:
        # setting a reasonable range because the game is supposedly rated 8+
        raise ValueError("That age is either too young or too old to play (ages 8-100)")
    # Error from outside reasonable range
def x_axis_check (x_cordinates):
    """ This function checks the x input of a player's guess"""
    if not isinstance(x_cordinates, int):
        # if statement to ensure the input is an integer
        raise TypeError("X coordinate must be an integer")
    #Raises an error if wrong type
    if x_cordinates < 0 or x_cordinates > 10:
        # if statement to ensure the input is reasonable
        raise ValueError("X coordinates have to be greater than 0 and less than 10")
def y_axis_check (y_coordinates):
    """ This function checks the y input of a player's guess"""
    if not isinstance(y_coordinates, str): # if statement ensuring the input is a string
        raise TypeError(" Y coordinates must be a string")
    # Raises an error for wrong type
    if len(y_coordinates) != 1: # if statement ensureing the input is just length 1
        raise ValueError("Please put only one letter")
    # Raises an error if the statement is blank or more than 1 letter
    if y_coordinates.isalpha() is False:
        # Ensuring the input is a letter
        raise ValueError("Y input must be a letter") # Raises and error
    valid_letters = ''.join(chr(i) for i in range(ord('a'), ord('a') + 10))
    # creating a string of valid letters
    if y_coordinates.lower() not in valid_letters: # checking for a valid letter
        raise ValueError("Only letters A-J are valid")
    # Raises an error if the input is outside that range

def main():
    "Main function that uses helper functions and prints assignment message"

    chosen = False # flag for a loop
    while chosen is False: # loop for age check

        player_age = int(input("age?")) # player input
        age_check(player_age) # validates or rejects age
        chosen = True # breaks the loop if no error raised 
    game = True # flag for in game loop
    while game is True: # game loop

        x_guess = int(input("What is your X coordinate guess?")) # gets user input for x-axis guess
        x_axis_check(x_guess) # calls on helper function and validates it or yields an error
        y_guess = str(input("What is your Y axis guess?")) # gets user input for y-axis guess
        y_axis_check(y_guess) # calls on helper function and validates it or yields an error
        proceed = str(input("want to continue?")) # provides option to break the game loop
        if proceed.lower() == "no": # if statement for breaking the loop
            game = False # breaks the loop

    print("This code was programmed by Sean Hegarty on February 5 2026. " +
    "The program validates 3 inputs and uses Pylint static analyser. " +
    "These functions are helper functions for a game of battleship. "+
    "One function is for checking age, to make sure the player is old enough." +
    "The second one is to check the x axis of a player's guess, and the last one " +
    "is to check the y-axis of a player's guess.")


if __name__ == "__main__":
    main()
