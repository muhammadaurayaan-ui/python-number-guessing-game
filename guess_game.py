import random
secret_number=random.randint(1,50)
guess_count= 0
guess_limit= 3
while guess_count < guess_limit:
  guess=int(input("Enter your guess ranging (1 to 50) :"))
  guess_count+=1
  if guess>secret_number:
      print("Too High!")
  elif guess<secret_number:
      print("Too Low!")
  elif guess==secret_number:
    print("You Won!")
    break
else:
  print("Sorry You failed!")
  print(f"The correct Number was {secret_number}")
