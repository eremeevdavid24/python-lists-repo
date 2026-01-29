import random

game_images = [
    """
    _______
---'   _____)
      (______)
      (______)
      (_____)
---.__(____)
""",
    """
     _______
---'    ____)____
           __________)
          __________)
         _________)
---.__________)
""",
    """
    _______
---'   ____)____
          _______)
       ____________)
      (____)
---.__(___)
"""
]


comuter_choice = random.randint(0,2)


user_choice = int(input("Alege: 0 = Rock, 1 = Paper, 2 = Scissors: "))

print("CALCULATOR: ", game_images[comuter_choice])
print("UTILIZATOR: ", game_images[user_choice])

if user_choice == comuter_choice:
    print("Egalitate!")
elif user_choice == 0 and comuter_choice == 1:
    print("Ai castigat")
elif user_choice == 2 and comuter_choice == 0:
    print("Ai castigat!")
else:
    print("Ai pierdut!")