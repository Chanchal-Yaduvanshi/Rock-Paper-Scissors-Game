
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user= int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if(user>=3 or user<0) :         #6th condn if user type any big no then we will not check any other condn
  print("You typed wrong number. You lose.\n")
else :
  game_images = [rock,paper,scissors]
  print(game_images[user])                 #shorter way

  print("Computer chose:")
  computer = random.randint(0,2)
  print(game_images[computer])             #shorter way

  if(user==computer) :      #4th condn
    print("It's a draw.\n")
  elif(user==0 and computer == 2) :   #rock>scissor 0>2  #2nd condn
    print("You wins.!\n")
  elif user==2 and computer==0 :     #scissor<rock 2<0   #3rd condn
    print("You lose.\n")
  elif(computer>user) :               #easy and 1st condn
    print("You lose.")
  elif user>computer :              #5th condn to catch user=1 and computer=0    paper>rock
    print("You win!\n")









