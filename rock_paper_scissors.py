
import random

print """ 
---------------------------------------------------------------------------- 
ROCK! PAPER! SCISSORS! THE GAME!!!
          _______              _______                 _______
      ---'   ____)         ---'   ____)____        ---'   ____)____
            (_____)                  ______)                 ______)
            (_____)                  _______)             __________)
            (____)                  _______)             (____)
      ---.__(___)          ---.__________)         ---.__(___)
      
----------------------------------------------------------------------------      
"""
scores = {'Player':0,'Computer':0}
while True:
		print scores
		print "RO-SHAM-BO! : Pick Your Choice!"
		command = raw_input(">")
		if command == "Rock":
				player_choice = "Rock"
				comp_choice = random.choice(['Rock', 'Scissors', 'Paper'])
				print "player_choice %s, comp_choice %s" % (player_choice, comp_choice)
				
				
