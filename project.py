import time

rounds= 0 
ComputerScore = 0 
PlayerScore = 0 
draws = 0

def play_game():

    UserName = user_name()

    global ComputerScore,PlayerScore,rounds,draws
    while True:
        
        compChoose=computer_choose()
        userChoose=user_choose()
       

        result = ''
        rounds +=1
       
        if userChoose == compChoose:
            result ='draw'
            draws+=1

        elif userChoose == 'rock'  and compChoose == 'scissor': 
            result = 'you win'
            PlayerScore+=1

        elif userChoose == 'rock' and compChoose=='paper':
            result = 'you lose'
            ComputerScore+=1

        elif userChoose == 'paper' and compChoose=='rock':
            result = 'you win'
            PlayerScore+=1

        elif userChoose == 'paper' and compChoose =='scissor':
            result = 'you lose'
            ComputerScore+=1

        elif userChoose=='scissor' and compChoose=='paper':
            result = 'you win'
            PlayerScore+=1
        elif userChoose=='scissor'  and compChoose=='rock':
            result = 'you lose'
            ComputerScore+=1

        elif userChoose=='exit':
            print()
            print(f"Player left the game at round - {rounds}")
            print(f"Final - Score | {UserName} - {PlayerScore} : Computer - {ComputerScore} |")
            if PlayerScore > ComputerScore:
                print(f"Player Won the game by score of {PlayerScore}")
            else:
                print(f"Computer Won the game by score of {ComputerScore}")

            print("\n-------------------")
            print("Thanks For Playing!")
            print("-------------------")
            break

        # give the result of the game who 
        # wins or loses
        if rounds == 20:
            print(f"\nyou choose {userChoose} and computer choose {compChoose} , result is {result}!")
            print("-------------------")
            print(f"{UserName}: {PlayerScore} , Computer Score: {ComputerScore}, Draws: {draws} ")
            print("-------------------")
            print(f"<<<<< Game over at round: {rounds} >>>>>")
            print(f"Final - Score | {UserName} - {PlayerScore} : Computer - {ComputerScore} |")
            if PlayerScore > ComputerScore:
                print(f"Player Won the game by score of {PlayerScore}")
            else:
                print(f"Computer Won the game by score of {ComputerScore}")

            print("\n-------------------")
            print("Thanks For Playing!")
            print("-------------------")
            break

        if userChoose == 'reset': 
            reset()
            print(f"Game restarted!")

        else:
            print()
            print(f"Round - {rounds}")
            print("-------------------")
            print(f"you choose {userChoose} and computer choose {compChoose} , result is {result}!")
            print("-------------------")
            print(f"{UserName}: {PlayerScore} , Computer Score: {ComputerScore}, Draws: {draws} ")
            print("-------------------")



def user_name():

    user_name = input("Enter player name: ").strip().upper()
    print(f"\nHey {user_name} welcome to the game!")
    print(f"""Here are the rules of the game,
              1. Rock beats Scissor
              2. Paper beats Rock 
              3. Scissor beats Paper
            """)
    return user_name

def  user_choose():

    user_choice = input("Enter a choice (rock, paper, scissor, reset, exit): ").lower().strip()
    while user_choice not in ['rock', 'paper', 'scissor','exit','reset']:
        user_choice = input("Invalid input. Please enter a choice (rock, paper, scissor, reset , exit): ").lower().strip()
    return user_choice 

def computer_choose():
    
    choices =['rock','paper','scissor']
    current_time = int(time.time()*1000)
    i = current_time % len(choices)
    return choices[i]

def reset():

    global ComputerScore,PlayerScore,rounds,draws
    ComputerScore=0
    PlayerScore=0
    rounds = 0
    draws = 0


if __name__ == '__main__':
    play_game()