import random

count=0
player_score=0
computer_score=0

while count<3:
     # Player's Choice
     player=input('Please enter your choice: ').lower()

     if player not in ('rock','paper','scissors'):
          print('You have to choose \'Rock\',\'Paper\',\'Scissors\' to play!\
               \nPlease Try again!')
          continue

     # Computer's Choice
     computer_list=['Rock','Paper','Scissors']
     # computer=random.choice(computer_list).lower()
     computer_choice=random.randint(0,2)
     computer=computer_list[computer_choice].lower()
     print('Computer chooses: '+computer)

     if computer=='rock':
          if player=='rock':
               print('Result: Draw!')
          elif player=='paper':
               print('Result: You win!')
               player_score+=1
          elif player=='scissors':
               print('Result: You lose!')
               computer_score+=1

     elif computer=='paper':
          if player=='paper':
               print('Result: Draw!')
          elif player=='scissors':
               print('Result: You win!')
               player_score+=1
          elif player=='rock':
               print('Result: You lose!')
               computer_score+=1

     elif computer=='scissors':
          if player=='scissors':
               print('Result: Draw!')
          elif player=='rock':
               print('Result: You win!')
               player_score+=1
          elif player=='paper':
               print('Result: You lose!')
               computer_score+=1

     count+=1

else:
     if player_score>1 and player_score>computer_score:
          print('Final result: Player win!\nYour score: '+str(player_score))
     elif computer_score>1 and computer_score>player_score:
          print('Final result: Computer win!\nComputer score: '+str(computer_score))
     else:
          print('Final result: Draw!')