#######################################yarin sabag##########################################################
#פרויקט משחק פייתון, אבן נייר ומספרים, את הפרוייקט הזה עשיתי לבד ללא חברי צוות
import random
import time

user_counter=0
pc_counter=0

def user_win(user_input):
    if win_rules[user_input] == pc_random_pick: # בודק האם המשתמש ניצח
        global  user_counter , pc_counter   
        user_counter+=1
        pc_counter+=0
        print(pc_random_pick)
        print("you got a point added :) , win!")
        print("pc score:",pc_counter,"user score: ",user_counter)
   
def pc_win(pc_random_pick):
    if win_rules[pc_random_pick] == user_input: # האם המחשב ניצח
        global  user_counter , pc_counter 
        user_counter+=0
        pc_counter+=1
        print(pc_random_pick)
        print("you dont got any points :( , lost!")
        print("pc score:",pc_counter,"user score: ",user_counter)
   
def tie(user_input , pc_random_pick):
    if user_input == pc_random_pick : #האם זה תיקו
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
    user_input=input("so what will you want to pick? : ") #המשתמש מכניס את הבחירה שלו
    
    user_input = user_input.strip() #להוריד רווחים עם יש
    
    user_input=user_input.capitalize()#בדיקה שהופכת אות ראשונה לגדולה

    if (user_input!= "Rock") and (user_input!=  "Paper") and (user_input!= "Scissors") : #בדיקה שאין מילה אחרת חוץ מילות המשחק
        print("please write one of the keywords of the game with Capital first letter and without space : Rock, Paper, Scissors")
        break

    words_of_item=["Rock", "Paper", "Scissors"] #מילות מפתח של המשחק
    pc_random_pick=random.choice(words_of_item)#המחשב בחר רנדומלית תו מהרשימה

    for i in range (1,4) : ##טיימר ספירה לאחור עד לחשיפה של התוצאה של המחשב
        print (i)
        time.sleep(1)

    win_rules = {                        #חוקי המשחק במילון
        "Rock":"Scissors",
        "Scissors":"Paper",
        "Paper":"Rock"
    }

    user_win(user_input)     #קריאות לפונקציות
    pc_win(pc_random_pick)
    tie(user_input , pc_random_pick)

######################################################################################################################

if user_counter>pc_counter : # בדיקה של המשחק הסופי האם הוא הפסיד ניצח או תיקו
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
   
          
if pc_counter == 0 and user_counter==0: #אם המשתמש הכניס מילים אחרות מהמילים שהוגדרו בשביל לשחק אז הוא יצא מהלולאה בעזרת ברייק ויעבור לאיפ הזה שידפיס לו יציאה, לפני כן יודפס לו אבל הודעת שגיאה מה בדיוק לכתוב
    print("exit")
     
          
          

























