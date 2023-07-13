#Final Project: Film Quiz Game

#Adding a welcome statement for users
def intro_message():
	print("\nHello! Welcome to my popular films quiz. \nYou will have three attempts to correctly answer each question. \nAt the end of the quiz, I will provide your score. \nAnswer the questions as accurately as possible for the best results!\n")
	return True

#Importing a quiz dictionary with my questions
from questions import quiz

class Rules:
#Creating a way to automatically tell player if their score is correct
	def check_ans(question, ans, attempts, score):
		if quiz[question]['answer'].lower() == ans.lower():
			print(f"You are correct! \nYour score is {score +1}!")
			return True
		else:
			print(f"That is the wrong answer :( \nYou have {attempts - 1} left! \nTry again...")
			return False

#Creating a way to allow players to have access to answer key
	def print_dictionary():
		for question_id, ques_answer in quiz.items():
			for key in ques_answer:
				print(key + ':', ques_answer[key])

#The game setup, adding an attempts rule where user can retry an answer 3 times and be alerted how many attempts they have left as well as a skip function
intro = intro_message()
while True:
	score = 0
	for question in quiz:
		attempts = 3
		while attempts > 0:
			print(quiz[question]['question'])
			answer = input("Enter Answer (To move to the next question, type 'skip') : ")
			if answer == "skip":
				break
			check = check_ans(question, answer, attempts, score)
			if check:
				score += 1
				break
			attempts -= 1
	break

#Adding an outro message
print("\nYour final score is {score}!\nThank you so much for playing !!!")


