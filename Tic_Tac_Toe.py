#! /usr/bin/python3
import random

try:
    player = input("A. Play against friend\nB. Play against computer\nselect " +
    "one, A or B : ").lower()

    # Used 0-2 instead of 1-3 so that it's easier to understand
    # This is what it will display as the body of the game
    #Moved this outside the function game_screen to make the lists 
                #editable while the program runs
    border = ['0', '1', '2' ]
    blankA=[" " , " " , " "]
    blankB=[" " , " " , " "]
    blankC=[" " , " " , " "]


    def game_screen():
        print(f"\n     {border}\n")
        print(f"A.   {blankA}")
        print(f"B.   {blankB}")
        print(f"C.   {blankC}\n\n")

    game_screen()


    #Extracting row and column from the user's input
    if player == 'a':
        letter = input("What letter (X/O) : ").title()
    elif player == 'b':
        letter = 'X'
       


    #Just creating a function to return the required row ex: BlankA for 'A',
                      # BlankB for 'B' etc
    def row_finder():
        if row=='A':
            return blankA
        elif row=='B':
            return blankB
        elif row=='C':
            return blankC


    #Checking if each combination of indexes is either Xs or Os
               #(if they line up to form the winning criteria)
    def winning_criteria():
        if [blankA[0],blankA[1],blankA[2]] == ['X','X','X']:
            return True
        elif [blankA[0],blankA[1],blankA[2]] == ['O','O','O']:
            return True
        elif [blankB[0],blankB[1],blankB[2]] == ['X','X','X']:
            return True
        elif [blankB[0],blankB[1],blankB[2]] == ['O','O','O']:
            return True
        elif [blankC[0],blankC[1],blankC[2]] == ['X','X','X']:
            return True
        elif [blankC[0],blankC[1],blankC[2]] == ['O','O','O']:
            return True
        elif [blankA[0],blankB[1],blankC[2]] == ['X','X','X']:
            return True
        elif [blankA[0],blankB[1],blankC[2]] == ['O','O','O']:
            return True
        elif [blankC[0],blankB[1],blankA[2]] == ['X','X','X']:
            return True
        elif [blankC[0],blankB[1],blankA[2]] == ['O','O','O']:
            return True
        elif [blankA[0],blankB[0],blankC[0]] == ['X','X','X']:
            return True
        elif [blankA[0],blankB[0],blankC[0]] == ['O','O','O']:
            return True
        elif [blankA[1],blankB[1],blankC[1]] == ['X','X','X']:
            return True
        elif [blankA[1],blankB[1],blankC[1]] == ['O','O','O']:
            return True
        elif [blankA[2],blankB[2],blankC[2]] == ['X','X','X']:
            return True
        elif [blankA[2],blankB[2],blankC[2]] == ['O','O','O']:
            return True
        return False


    available = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C0', 'C1', 'C2', ]



    # Checking if all the available moves are done that is,
          # if there are no more playable moves left
    # asking for the position to place X
    # Inserting the Xs and Os to their places
    # Changing the variable 'letter' to O or X depending on the 
                           #move of the next player
    if player == 'a':
        while winning_criteria() == False :
            if available == []:
                break
            if letter=='X' :
                position = input("Where to put X (Alphabet followed by the " +
                "number : a1, b2 or c0 ...) : ").title()
                if position in available:
                    available.remove(position)
                    row = position[0]
                    column = int(position[1])
                    row_finder().__setitem__(column, letter)
                    game_screen()
                    letter='O'
                else:
                    print("already entered or wrong input")
                    continue
            elif letter=='O' :
                position = input("Where to put O (Alphabet followed by the " +
                "number : a1, b2 or c0 ...) : ").title()
                if position in available:
                    available.remove(position)
                    row = position[0]
                    column = int(position[1])
                    row_finder().__setitem__(column, letter)
                    game_screen()
                    letter = 'X'
                else:
                    print("already entered or wrong input")
                    continue

        # checking the last item in variable-letter and deciding 
                    #if its a win or not
        if winning_criteria() == True:
            if letter=='X':
                game_screen()
                print('O Wins!')
            elif letter=='O':
                game_screen()
                print('X Wins!')
        else:
            game_screen()
            print('Draw!')




    # Checking if all the available moves are done that is,
        # if there are no more playable moves left
    #asking for the position to place X
    # Inserting the Xs to their places
    # Changing the variable 'letter' to O for computer to run its turn
    #removing the player's choice from the list-available
    elif player == 'b':
        while winning_criteria() == False :
            if available == []:
                break
            if letter == 'X':
                position = input("Where to put (Alphabet followed by " +
                "the number : a1, b2 or c0 ...) : ").title()
                if position in available:
                    row = position[0]
                    column = int(position[1])
                    row_finder().__setitem__(column, letter)
                    letter = 'O'
                    available.remove(position)
                else:
                    print("already entered or wrong input")
                    continue
                
            #taking a random position from the available-list of choices
            #removing the random choice so its not chosen again
            elif letter == 'O':
                computer_choice = random.choice(available)
                available.remove(computer_choice)
                row = computer_choice[0]
                column = int(computer_choice[1])
                row_finder().__setitem__(column,letter)
                game_screen()
                letter = 'X'




        #checking the last item in variable-letter and deciding 
               #if its a win or not
        if winning_criteria() == True:   
            if letter=='X':
                game_screen()
                print('You Lost!')
            elif letter=='O':
                game_screen()
                print('You Won!')
        else:
            game_screen()
            print('Draw!')



except:
    print("Game Crashed! You happy now? input correct values next time")
