



# Game
  
+++section;title=Docstring;hash=a08d0145b3c5479acb1c

Initializes the class through initializing the round information
  
+++

\
  
+++section;title=Path;hash=7090eb0d3c931a090b48

`yblackjack/yoco_exam_1.py`
  
+++

\
  
+++section;title=Source Code;hash=ca3167ab862031c8c72d
```
class Game (Player):


	'''
	Initializes the class through initializing the round information
	'''
	def __init__ (self, rounds_info):
		self.rounds_info = rounds_info
	

	'''
	Runs the round and prints out whether each of the results matches up with the test cases
	'''
	def run_rounds (self): 
		for round in self.rounds_info:	

			determined_winner = self.determine_round_winner (round['playerA'], round['playerB'])

			if round['playerAWins'] != determined_winner:
				print('Error: There is a mismatch between the winners')
				print ('The test case says that player1 win is ' + str(round['playerAWins']) + ' but\
				the program determined otherwise :(')

			else: 
				print ('Result is Correct! Both printed out ' + str(determined_winner))
			



	'''
	Compares the sorted scores and returns the winner
	'''
	def compare_sorted_scores (self, players):


		#get all the sorted scores and put it in a 2d list
		player1_scores, player2_scores = map (lambda player: player.get_sorted_scores(), players)


		#just a list with their lengths
		index = 0

		highest_card_winner = True

		#prevents index out of bounds errors
		while index < min (len(player1_scores), len(player2_scores)):

			if player1_scores[index][0] != player2_scores[index][0]:
				return player1_scores[index][0] > player2_scores[index][0]

			#accounting for face card differences
			elif player1_scores[index][0] == 10 and player1_scores[index][1] != player2_scores[index][1]:
				return player1_scores[index][1] > player2_scores[index][1]


			index +=1 

		return players[0].get_highest_card_suite() > players[1].get_highest_card_suite()


	'''
	Determines the round winner through first calling the total scores. If a winner
	cannot be determined, then we have to call compare_sorted_scores
	'''

	def determine_round_winner (self, player1_round, player2_round):


		player1, player2 = Player (player1_round), Player(player2_round)

		scores = player1.compute_score (), player2.compute_score()
	
		#check if they violate the 21 limit
		for index, score in enumerate(scores):


			if score > 21:
				return index != 0

			if score > scores [(index + 1)%2]:
				return index == 0

		return self.compare_sorted_scores ((player1, player2))
```  
+++

\
  
+++section;title=References;hash=a2db46e81411982535ae

**Line 211** `/yoco_exam_1.py`

```
	if not tests:
		print('There was an error parsing the json file')
		exit(1)

	game = Game (tests)
	game.run_rounds()



#parses the json file

```
\  
+++