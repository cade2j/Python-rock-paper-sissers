score = 0
import random
import time
print('Rock Paper Scissors By: Cade\nGithubs : Cade2j, Cade4j, Cade46\nHave fun')
input('Press enter to start')
while True:
 time.sleep(1)
 print('3')
 time.sleep(1)
 print('2')
 time.sleep(1)
 print('1')
 time.sleep(1)
 print(random.choice(['🪨 Rock', '📰 Paper', '✂ Scissors']))
 IN = input('Did you win(yes or no): ')
 if IN == "yes" or IN == "Y" or IN == "y" or IN == "Yes":
     print('Good job!!!')
     score = score + 1
 elif IN == "no" or IN == "N" or "IN" == "n" or IN == "No":
     print('Hope you win next time!')
 else:
    print('Error: Please type yes or no next time')
 print('Score: ' + str(score))
