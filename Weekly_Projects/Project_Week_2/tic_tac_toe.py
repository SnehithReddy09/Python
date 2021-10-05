import numpy as np
import random
import time

class tic_tac_toe :
    board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
    player_1='X'
    player_2='O'

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

    def move(self,turn,position):
        if turn==1:
            self.board[position//3][position%3]=self.player_1
        elif turn==2:
            self.board[position//3][position%3]=self.player_2


    def check_validity(self,user_input):
        if user_input<0 or user_input>8:
            return "Invalid input given"
        if self.board[user_input//3][user_input%3]=='-':
            return True
        else:
            return False 

    def check_winner(self):
        horizontal_check=0
        vertical_check=0
        diagonal_check=0
        x=0
        for i in range(3):
            if ((self.board[i][0]==self.board[i][1]) and (self.board[i][1]==self.board[i][2])) and self.board[i][2]!='-':
                horizontal_check=1
                x=1
        
        for i in range(3):
            if ((self.board[0][i]==self.board[1][i]) and (self.board[1][i]==self.board[2][i])) and self.board[2][i]!='-':
                vertical_check=1
        if self.board[1][1]!='-' and self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
            diagonal_check=1 
            x=3
        if self.board[1][1]!='-' and self.board[2][0]==self.board[1][1] and self.board[1][1]==self.board[0][2]:
            diagonal_check=1 
            x=4
        
        if horizontal_check==1 or vertical_check==1 or diagonal_check==1:
            return True 
        else:
            return False


    def start_game(self):
        turn=1
        turn_count=0
        while(1):
            user_input=int(input("Player {0} enter the position ".format(turn)))
            response=self.check_validity(user_input)
            if response==True:
                self.move(turn,user_input)
                result=self.check_winner()
                self.display()
                turn_count+=1
                if result==True:
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
            
class user_vs_computer(tic_tac_toe):

    indexes_not_occupied=np.arange(9)

    def computer_input_value(self,indexes_not_occupied):
        input_generator=random.choice(indexes_not_occupied)
        return input_generator

    def start_game(self):
        turn=1
        turn_count=0
        while(1):
            if turn==1:
                user_input=int(input("Player enter the position "))
                response=self.check_validity(user_input)
            else:
                computer_input=self.computer_input_value(self.indexes_not_occupied)
                user_input=computer_input
                response=True
            if response==True:
                self.move(turn,user_input)
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
    