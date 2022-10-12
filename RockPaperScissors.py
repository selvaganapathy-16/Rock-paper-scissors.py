import random
import time
list = ['ROCK', 'PAPER','SCISSORS']
print('Let\'s play ROCK, PAPER, SCISSORS..\U0001F600')
time.sleep(1)
while(1):
  x= random.choice (list)
  print('READY')
  time.sleep(1)
  print('SET')
  time.sleep(1)
  print('GO')
  a=input().upper()
  if a not in list:
    print('Please enter rock, paper or scissor')
    continue
  if a == x:
    print('It's a tie \U0001F605')
  elif a == 'ROCK' and x == 'SCISSORS':
    print (f'My choice is {x} you win \U0001F612')
  elif a == 'SCISSORS' and x == 'PAPER':
    print (f'My choice is {x) you win Ueee1F612')
  elif a == 'PAPER' and x == 'ROCK':
    print(f'My choice is (x) you win \U0001F612')
  else:
    print (f'My choice is {x} HaHa...I win \U0001F923')
  time.sleep(1)
