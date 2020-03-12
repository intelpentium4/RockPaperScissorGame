#!/bin/python3

from random import randint

#Prompts the player to choose rock, paper, or scissor
player = input('rock (r) paper (p) or scissor (s)?')
print(player, 'vs', end=' ')
#adding a end=' ' to the end of a print makes it end with a space instead of a new line.

#Using rand, the computer will pick between 1, 2, or 3
chosen = randint(1,3)

#Converts the numbers into rock, paper, or scissor
if chosen == 1:
  computer = 'p'
elif chosen == 2:
  computer = 'r'
else:
  computer = 's'

#Prints the computer's chosen weapon
print(computer)

#Logic for deciding who won
if player == computer:
  print('DRAW!')
#if Player picks rock
elif player == 'r' and computer == 's':
  print('Player Wins!')
elif player == 'r' and computer == 'p':
  print('Computer Wins!')
#if Player picks paper
elif player == 'p' and computer == 'r':
  print('Player Wins!')
elif player == 'p' and computer == 's':
  print('Computer Wins!')
#if Player pcisk scissor
elif player == 's' and computer == 'p':
  print('Player Wins!')
elif player == 's' and computer == 'r':
  print('Computer Wins!')  
  
