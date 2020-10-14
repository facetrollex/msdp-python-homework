import random

randomNumber = random.randint(1, 100)

userNumber = -1

while userNumber != randomNumber:
    print('I made up a number. Can you guess it?')
    userNumber = int(input())
    if userNumber < randomNumber:
      print('Too low!')
    elif userNumber > randomNumber:
      print('Too high!')

print('Congratulations you won!')