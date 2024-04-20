import random
# Rock
ascii_Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
ascii_papper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
ascii_Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("welcom to Rock, Papper, Scissors Game")
print(f"{ascii_Rock}\n{ascii_papper}\n{ascii_Rock}\n")

Comfirm=input("Press Enter to continuos Or Enter Help to show the rules ").capitalize()
if Comfirm=="Help":
    print ("""

                             ******Rules******
          1)You choose and the computer chooses
          2)Rock smashes Scossors>>>Rock wins 
          3)Scissors Cuts pappers>>>Scissors wins 
          4)Papper covers Rock>>>>>>Papper wins

""")
    
user_choice=input("Please Enter user choice")
if user_choice not in["rock","papper","scissors"]:
    print=("Invalid chioce Please try again")
else :
    if user_choice=="rock":
        print(f"Your chioce is {ascii_Rock}")
    elif user_choice=="papper":
        print(f"Your choice is {ascii_papper}")
    elif user_choice=="scissors":
        print(f"Your choice is {ascii_Scissors}")
computer_choice=random.choice(["rock","papper","scissors"])
if computer_choice=="rock":
        print(f"Computer chioce is {ascii_Rock}")
elif computer_choice=="papper":
        print(f"Computer choice is {ascii_papper}")
elif computer_choice=="scissors":
        print(f"Computer choice is {ascii_Scissors}")

if computer_choice==user_choice:
     print(f"sorry it's a tie Please try agian ")

elif ( 
     (user_choice=="rock"and computer_choice=="scissors")
     or 
     (user_choice=="papper"and computer_choice=="rock ")
     or
     (user_choice=="scissors"and computer_choice=="papper")
 
):
    print (f"Your choice {user_choice} Beats computer choice {computer_choice}")
else:
     print(f"Computer choice {computer_choice} Beats Your choice {user_choice}")

