#######################################yarin sabag##########################################################
#Python Game Project – Rock, Paper, and Scissors
#This project was developed independently by me, without any team members.

import random
import time

user_counter=0
pc_counter=0

def user_win(user_input):
    if win_rules[user_input] == pc_random_pick: # Checks if user won
        global  user_counter , pc_counter   
        user_counter+=1
        pc_counter+=0
        print(pc_random_pick)
        print("you got a point added :) , win!")
        print("pc score:",pc_counter,"user score: ",user_counter)
   
def pc_win(pc_random_pick):
    if win_rules[pc_random_pick] == user_input: # Checks if the pc won
        global  user_counter , pc_counter 
        user_counter+=0
        pc_counter+=1
        print(pc_random_pick)
        print("you dont got any points :( , lost!")
        print("pc score:",pc_counter,"user score: ",user_counter)
   
def tie(user_input , pc_random_pick):
    if user_input == pc_random_pick : #it is a tie?
        global  user_counter , pc_counter 
        user_counter+=1
        pc_counter+=1
        print(pc_random_pick)
        print("its a tie!")
        print("pc score:",pc_counter,"user score: ",user_counter)

print(
 "=========================\n"
  "ROCK PAPER SCISSORS\n"
  "=========================\n"

    "✊"  "✋"  "✌"
 )
######################################################################################################################

while user_counter!=3 and pc_counter !=3:
    print("this is Rock, Paper, Scissors game\nRules:Rock beats Scissors\nScissors beats Paper\nPaper beats Rock\nYou will choose one option, and the computer will choose another\nThe winner is determined by the rules above\nyou will play 3 rounds untill there is a win or a tie")
    user_input=input("so what will you want to pick? : ") #user input
    
    user_input = user_input.strip() #Remove spaces
    
    user_input=user_input.capitalize()#capitalizes the first letter

    if (user_input!= "Rock") and (user_input!=  "Paper") and (user_input!= "Scissors") : #Validates that the input contains only game words
        print("please write one of the keywords of the game with Capital first letter and without space : Rock, Paper, Scissors")
        break

    words_of_item=["Rock", "Paper", "Scissors"] #key words
    pc_random_pick=random.choice(words_of_item)#pc random choice

    for i in range (1,4) : #timer
        print (i)
        time.sleep(1)

    win_rules = {                        #  game ruls
        "Rock":"Scissors",
        "Scissors":"Paper",
        "Paper":"Rock"
    }

    user_win(user_input)     #Call functions
    pc_win(pc_random_pick)
    tie(user_input , pc_random_pick)

######################################################################################################################
# who won? or lost? maybe a tie? - cheak what is the final result of the game
if user_counter>pc_counter : 
    print("==========================================\nfinal result of 3 rounds : big win!!!\n " 
          
        "====================="
        "YOU WIN!!!"
        " ====================="

        )
if pc_counter>user_counter  :
    print("==========================================\nfinal result of 3 rounds : unbelivable lost!!!\n"
          
          
        "====================="
        "YOU LOSE..."
       " ====================="

 
        )   

if pc_counter == user_counter and not pc_counter == 0 and user_counter==0:
    print("==========================================\nfinal result of 3 rounds : its a tie!!! \n"
          
          
        "====================="
        "TIE!"
        " ====================="

        )
   
#If the user enters words other than the ones defined for the game, the loop will end using break, 
# and the program will move to the if statement that prints the exit message. 
# Before that, an error message will be printed explaining exactly what to type.
         
if pc_counter == 0 and user_counter==0: 
    print("exit")
     
          
# thank you!
























