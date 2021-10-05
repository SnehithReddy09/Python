import numpy as np
import random
import time

class tic_tac_toe :
    
    #Initially the board 3*3 is set to '-' 
    board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
    #Player_1 is given the coin 'X' and it will be used during the game.
    player_1='X'
    #Player 2 is given the coin 'O' and it will bw used during the game.
    player_2='O'

    #Function for displaying the entire board after ecah turn.
    def display(self):
        print("\n")
        print("\t     |     |")
        print("\t   {0} |  {1}  | {2} ".format(self.board[0][0],self.board[0][1],self.board[0][2]))
        print("\t_____|_____|_____")
        print("\t   {0} |  {1}  | {2} ".format(self.board[1][0],self.board[1][1],self.board[1][2]))
        print("\t_____|_____|_____")

        print("\t   {0} |  {1}  | {2} ".format(self.board[2][0],self.board[2][1],self.board[2][2]))
        print("\t     |     |")
        print("\n")

    
    #Selected position by Player it set in this function.
    def move(self,turn,position):
        if turn==1:
            self.board[position//3][position%3]=self.player_1
        elif turn==2:
            self.board[position//3][position%3]=self.player_2

 
    # Function to check the validity of the input position.
    def check_validity(self,user_input):
        # checking whether input is within given limit or not
        if user_input<0 or user_input>8:
            return "Invalid input given"
        # checking whether the position is already occupied or not.
        if self.board[user_input//3][user_input%3]=='-':
            return True
        else:
            return False 

    #Function to check if the player has won after he has made his move.
    def check_winner(self):
        horizontal_check=0
        vertical_check=0
        diagonal_check=0
        x=0
        #Checking whether there are similar coins(same player selected positions) in a row
        for i in range(3):
            if ((self.board[i][0]==self.board[i][1]) and (self.board[i][1]==self.board[i][2])) and self.board[i][2]!='-':
                horizontal_check=1
                x=1
        #Checking whether there are similar coins(same player selected positions) in a column
        for i in range(3):
            if ((self.board[0][i]==self.board[1][i]) and (self.board[1][i]==self.board[2][i])) and self.board[2][i]!='-':
                vertical_check=1
               
        #Checking whether there are similar coins(same player selected positions) in a diagonal
        if self.board[1][1]!='-' and self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
            diagonal_check=1 
            x=3
        if self.board[1][1]!='-' and self.board[2][0]==self.board[1][1] and self.board[1][1]==self.board[0][2]:
            diagonal_check=1 
            x=4
        
        #Checking If any of above conditions are satisfied or not
        if horizontal_check==1 or vertical_check==1 or diagonal_check==1:
            return True 
        else:
            return False

 
    #Function to start the game
    def start_game(self):
        #variable 'turn' to know which player is playing at present
        turn=1
        #Variable to keep the count of number of turns 
        turn_count=0
        while(1):
            user_input=int(input("Player {0} enter the position ".format(turn)))
            #Checking validity of input.
            response=self.check_validity(user_input)
            if response==True:
                #If input is valid then that move is been made.
                self.move(turn,user_input)
                #Check whether the player wins after move is made.
                result=self.check_winner()
                #Displaying the board after the move.
                self.display()
                turn_count+=1
                if result==True:
                    #If result is True print which player won and break the loop.
                    print("Won player,",turn)
                    break 
                else:
                    if turn_count==9:
                        #If result is False but turn_count==9 i.e. all the positions are occupied print Draw and break the loop.
                        print("Match Draw!")
                        break
                    else:
                        #If result is False but still all postions are not filled then next round other player have to move.
                        if turn==1:
                            turn=2
                        else:
                            turn=1
            # If response==False then the position selected is already filled
            elif response==False:
                print("Given position which is already occupied")
            else:
                # If the input is out of range (<0 or >9)
                print(response)
    
# Class for user vs Computer whcih inherits all the features of tic_tac_toe class.
class user_vs_computer(tic_tac_toe):

    #Variable to keep the indexex which are not occupied for geenerating a random number by computer.
    indexes_not_occupied=np.arange(9)

    #Generation of random number when it is computer's turn.
    def computer_input_value(self,indexes_not_occupied):
        input_generator=random.choice(indexes_not_occupied)
        return input_generator

    def start_game(self):
        turn=1
        turn_count=0
        while(1):
            #If turn==1 then it is user turn to play the game.
            if turn==1:
                user_input=int(input("Player enter the position "))
                response=self.check_validity(user_input)
            # It's computer turn to play.
            else:
                #generating computer_input
                computer_input=self.computer_input_value(self.indexes_not_occupied)
                user_input=computer_input
                response=True
            if response==True:
                self.move(turn,user_input)
                #Once the position is selected then it is removed from array.
                self.indexes_not_occupied=np.delete(self.indexes_not_occupied,np.where(self.indexes_not_occupied==user_input))
                result=self.check_winner()
                if turn==2:
                    time.sleep(1.5)
                    print("Display after Computer Selection")
                self.display()
                turn_count+=1
                if result==True:
                    if turn==2:
                        print("Computer Won !")
                    else:
                        print("Won player,",turn)
                    break 
                else:
                    if turn_count==9:
                        print("Match Draw!")
                        break
                    else:
                        if turn==1:
                            turn=2
                        else:
                            turn=1
            elif response==False:
                print("Given position which is already occupied")
            else:
                print(response)
        

while(1):
    print("Enter your choice")
    game_type_input=int(input(" 1. User v/s User ||  2. User and Computer "))
    if game_type_input==1:
        obj=tic_tac_toe()
        print("..........................")
        print("Start Playing")
        print()
        obj.start_game()
        break
    elif game_type_input==2:
        obj=user_vs_computer()
        print()
        print("Start Playing")
        print()
        obj.start_game()
        break
    else:
        print("Wrong Input")
        
        
        
'''
OUTPUT

(1) User v/s User

Enter your choice
 1. User v/s User ||  2. User and Computer 1
..........................
Start Playing

Player 1 enter the position 0


             |     |
           X |  -  | - 
        _____|_____|_____
           - |  -  | - 
        _____|_____|_____
           - |  -  | - 
             |     |


Player 2 enter the position 1


             |     |
           X |  O  | - 
        _____|_____|_____
           - |  -  | - 
        _____|_____|_____
           - |  -  | - 
             |     |


Player 1 enter the position 2


             |     |
           X |  O  | X 
        _____|_____|_____
           - |  -  | - 
        _____|_____|_____
           - |  -  | - 
             |     |


Player 2 enter the position 3


             |     |
           X |  O  | X 
        _____|_____|_____
           O |  -  | - 
        _____|_____|_____
           - |  -  | - 
             |     |


Player 1 enter the position 4


             |     |
           X |  O  | X 
        _____|_____|_____
           O |  X  | - 
        _____|_____|_____
           - |  -  | - 
             |     |


Player 2 enter the position 5


             |     |
           X |  O  | X 
        _____|_____|_____
           O |  X  | O 
        _____|_____|_____
           - |  -  | - 
             |     |


Player 1 enter the position 6


             |     |
           X |  O  | X 
        _____|_____|_____
           O |  X  | O 
        _____|_____|_____
           X |  -  | - 
             |     |


Won player, 1


(2) User vs Computer
Enter your choice
 1. User v/s User ||  2. User and Computer 2

Start Playing

Player enter the position 0


             |     |
           X |  -  | - 
        _____|_____|_____
           - |  -  | - 
        _____|_____|_____
           - |  -  | - 
             |     |


Display after Computer Selection


             |     |
           X |  -  | - 
        _____|_____|_____
           - |  -  | O 
        _____|_____|_____
           - |  -  | - 
             |     |


Player enter the position 4


             |     |
           X |  -  | - 
        _____|_____|_____
           - |  X  | O 
        _____|_____|_____
           - |  -  | - 
             |     |


Display after Computer Selection


             |     |
           X |  -  | - 
        _____|_____|_____
           - |  X  | O 
        _____|_____|_____
           - |  -  | O 
             |     |


Player enter the position 2


             |     |
           X |  -  | X 
        _____|_____|_____
           - |  X  | O 
        _____|_____|_____
           - |  -  | O 
             |     |


Display after Computer Selection


             |     |
           X |  -  | X 
        _____|_____|_____
           O |  X  | O 
        _____|_____|_____
           - |  -  | O 
             |     |


Player enter the position 7


             |     |
           X |  -  | X 
        _____|_____|_____
           O |  X  | O 
        _____|_____|_____
           - |  X  | O 
             |     |


Display after Computer Selection


             |     |
           X |  -  | X 
        _____|_____|_____
           O |  X  | O 
        _____|_____|_____
           O |  X  | O 
             |     |


Player enter the position 1


             |     |
           X |  X  | X 
        _____|_____|_____
           O |  X  | O 
        _____|_____|_____
           O |  X  | O 
             |     |


Won player, 1
'''
    
