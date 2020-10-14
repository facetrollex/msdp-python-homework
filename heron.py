import argparse
import math

parser = argparse.ArgumentParser(description='Triangle area')
parser.add_argument("a", type=int, help="A")
parser.add_argument("b", type=int, help="B")
parser.add_argument("c", type=int, help="C")
args = parser.parse_args()

if args.a <= 0 or args.b <= 0 or args.c <= 0:
  print('Invalid arguments')
else:  
  s = (args.a + args.b + args.c) / 2
  print(math.sqrt(s * (s - args.a) * (s - args.b) * (s - args.c)))