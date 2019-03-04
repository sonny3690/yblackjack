import json
from pprint import pprint
import operator



'''
Class: given information about a round, outputs detailed statistics about it that helps
determine Game the winner

@params round_info: {list of Strings}
'''
class Player:


	'''
	Initializes the class
	@params round_info: {list of Strings}
	'''

	def __init__ (self, round_info):
		self.player_round_info = round_info
		self.player_score = 0

		#contains the number on the first index, suite number on the second
		self.highest_card = [0,0]
		self.scores = []



		'''
	Initializes the class
	@params card: {String}
	'''
	def get_each_score (self, card):

		score = 0

		number, suite = card[:-1], card[-1]

		#indexes for the suites and face cards as a dictionary
		suite_diction = {'D':1, 'C':2, 'H':3, 'S': 4}
		face_card_diction = {'K': 3, 'Q': 2, 'J': 1}

		#if a face card, we return a large number, then we can take the modulo to 
		#store information about the type of face card
		if number == 'J' or number == 'K' or number== 'Q':
			score = 100 + face_card_diction[number]

		elif number == 'A':
			score = 11 
		else:
			score = int(number)

		return score, suite_diction[suite]

	def compute_score (self):


		for card in self.player_round_info:
			curr_score, suites = self.get_each_score (card)
			face_card_value = 0


			#case in which face value must be assigned 
			if curr_score > 100:
				face_card_value = curr_score % 10
				curr_score = int(curr_score/10)

			#add this to total player score
			self.player_score += curr_score

			if curr_score >= self.highest_card[0]:

				if curr_score == self.highest_card[0]:
					self.highest_card[1] = max (self.highest_card[1], suites)
				else:
					self.highest_card = [curr_score, suites]

			self.scores.append ((curr_score, face_card_value))

		return self.player_score


	def get_highest_card_suite(self):
		return self.highest_card[1]


	def get_sorted_scores (self):


		#first we sort by score
		kind = sorted(self.scores, key = lambda scores: scores[0], reverse=True)

		#then for each score, we must sort by the face value when the face cards come out
		return sorted(kind, key = lambda face_value: face_value[1], reverse=True)
		


class Game (Player):


	def __init__ (self, rounds_info):
		self.rounds_info = rounds_info
	

	def run_rounds (self): 
		for round in self.rounds_info:	


			determined_winner = self.determine_round_winner (round['playerA'], round['playerB'])

			if round['playerAWins'] != determined_winner:
				print('Error: There is a mismatch between the winners')
				print ('The test case says that player1 win is ' + str(round['playerAWins']) + ' but\
				the program determined otherwise :(')
			


	def compare_sorted_scores (self, players):



		#get all the sorted scores and put it in a 2d list
		player1_scores, player2_scores = map (lambda player: player.get_sorted_scores(), players)


		#just a list with their lengths
		index = 0

		highest_card_winner = True


		while index < min (len(player1_scores), len(player2_scores)):

			if player1_scores[index][0] != player2_scores[index][0]:
				return player1_scores[index][0] > player2_scores[index][0]

			#accounting for face card differences
			elif player1_scores[index][0] == 10 and player1_scores[index][1] != player2_scores[index][1]:
				return player1_scores[index][1] > player2_scores[index][1]


			index +=1 

		return players[0].get_highest_card_suite() > players[1].get_highest_card_suite()


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




def run_rounds ():

	tests  = parse_json()
	game = Game (tests)
	game.run_rounds()



def parse_json ():
	with open('yoco_tests.json') as f:
	    return json.load(f)

run_rounds()







