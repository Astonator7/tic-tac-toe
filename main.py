import pyttsx3
from IPython.display import clear_output
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
def player_input():
    while True:
        speak("player 1 do you want X or O:")
        player1_marker=input("player 1 do you want X or O:")
        if player1_marker.lower()=="o" or player1_marker.lower()=="x":
            break
        else:
            continue
    if player1_marker.upper()=="X":
        player2_marker="O"
    else:
        player2_marker="X"
    return [player1_marker.upper(),player2_marker]
def place_marker(board, marker, position):
    board[position]=marker
def win_check(board, mark):
    if board[1]==board[2]==board[3]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    elif board[7]==board[8]==board[9]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark:
        return True
    elif board[2]==board[5]==board[8]==mark:
        return True
    elif board[3]==board[6]==board[9]==mark:
        return True
    elif board[3]==board[5]==board[7]==mark:
        return True
    else:
        return False
import random
def choose_first():
    chance=random.randint(1,2)
    if chance==1:
        return 1
    else:
        return 2
def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        return False
def full_board_check(board):
    if (board[1]=='X' or board[1]=='O') and  (board[2]=='X' or board[2]=='O') and (board[3]=='X' or board[3]=='O') and (board[4]=='X' or board[4]=='O') and (board[5]=='X' or board[5]=='O') and  (board[6]=='X' or board[6]=='O') and (board[7]=='X' or board[7]=='O') and (board[8]=='X' or board[8]=='O') and (board[9]=='X' or board[9]=='O'):
        return True
    else:
        return False
def player_choice(board):
    while True:
        speak("where do you want to place your marker")
        placing=int(input("where do u want to place you marker:"))
        if placing in [1,2,3,4,5,6,7,8,9] and space_check(board,placing)==True:
            return placing
        else:
            continue
def replay():
    while True:
        speak("do you want to continue yes or no")
        i=input("do you want to continue (y/n):")
        if i.lower()=='y':
            return True
            break
        elif i.lower()=='n':
            return False
            break
        else:
            continue
speak("hello this is jarvis at you service")
speak('Welcome to Tic Tac Toe!')
while True:
    option=player_input()
    speak("player 1 has chosen {} and player 2 has chosen {}".format(option[0],option[1]))
    first_chance=choose_first()
    game_board=["#"," "," "," "," "," "," "," "," "," "]
    game_on=True
    while game_on:
        if first_chance==1:
            speak("player 1 ")
            o=player_choice(game_board)
            place_marker(game_board,option[0],o)
            display_board(game_board)
            if win_check(game_board,option[0]):
                speak("player 1 has won")
                game_on=False
            else:
                if full_board_check(game_board):
                    speak("it is a tie")
                    break
                else:
                    first_chance=2
        elif first_chance==2:
            speak("player 2")
            q=player_choice(game_board)
            place_marker(game_board,option[1],q)
            display_board(game_board)
            if win_check(game_board,option[1]):
                speak('player 2 has won')
                game_on=False
            else:
                if full_board_check(game_board):
                    speak("it is a tie")
                    break
                else:
                    first_chance=1
    suggestion=replay()
    if suggestion==True:
        continue
    else:
        break
