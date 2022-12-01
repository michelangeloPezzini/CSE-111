import random

vitoriaPlayer = 0
vitoriaComputer = 0

print("You will play even or odd against the computer.")
print("Good Luck! ")

#Função para pegar o numero do usuario
#função para gerar numero aleatorio/computador
#função para comparar numero do usuario e computador e declarar vitoria

def main():
    while True:
        player = user_input()
        computer = computer_number()
        total = player + computer
        letter = " "
        while letter not in "OE":
            letter = str(input("Even or Odd? [E/O] ")).strip().upper()[0]
        if letter == "E":
            if total % 2 == 0:
                print("-"*30)
                print("\033[32mYou WIN!\033[m")
                print(f"{player} + {computer} = {total}: Even")
                print("-"*30)
                vitoriaPlayer = vitoriaPlayer + 1
            else:
                print("-"*30)
                print("\033[31mYou Lose!\033[m")
                print(f"{player} + {computer} = {total}: Odd")
                print("-"*30)
                vitoriaComputer = vitoriaComputer + 1
            print(f"Player {vitoriaPlayer} x {vitoriaComputer} Computer")
            print("-"*30)
        elif letter == "O":
            if total % 2 == 1:
                print("-"*30)
                print("\033[32mYou Win!\033[m")
                print(f"{player} + {computer} = {total}: Odd")
                print("-"*30)
                vitoriaPlayer = vitoriaPlayer + 1
            else:
                print("-"*30)
                print("\033[31mYou Lose!\033[m")
                print(f"{player} + {computer} = {total}: Even")
                print("-"*30)
                vitoriaComputer = vitoriaComputer + 1
            print(f"Player {vitoriaPlayer} x {vitoriaComputer} Computer")
            print("-"*30)
        if vitoriaPlayer == 5:
            print(f"\nYou Won {vitoriaPlayer} x {vitoriaComputer}")
            break
        elif vitoriaComputer == 5:
            print(f"\nYou Lose {vitoriaComputer} x {vitoriaPlayer}")
            break
    


def user_input():
    player_input = int(input("Type a number: "))
    return player_input

def computer_number():
    computer_random = random.randint(0, 11)
    return computer_random


if __name__ == ("__main__"):
    main()


