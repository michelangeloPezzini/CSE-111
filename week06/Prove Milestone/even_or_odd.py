import random

vitoriaPlayer = 0
vitoriaComputer = 0

print("You will play even or odd against the computer.")
print("Good Luck! ")

def number_input():
  player_guess = int(input("Type a number between 1 and 10: "))
  return player_guess

while True:
    player = number_input()
    computer = random.randint(0, 11)
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
print("\nThe End")
