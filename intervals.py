import sys

sys.stdout.write("Enter a number: ")
number = int(input())
if (number > -15 and number <= 12) or (number > 14 and number < 17) or (number >= 19):
  print(True)
else:
  print(False)