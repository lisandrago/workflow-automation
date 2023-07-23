#Final Project: Film Quiz Game

#Adding a welcome statement for users
def intro_message():
	print("\nHello! Welcome to my popular films quiz. \nYou will have three attempts to correctly answer each question. \nAt the end of the quiz, I will provide your score. \nAnswer the questions as accurately as possible for the best results!\n")
	return True

#Importing a quiz dictionary with my questions and answers
from questions import quiz

#Creating a way to automatically tell player if their score is correct, should always happen without prompt
def check_ans(question, ans, attempts, total_correct_answers):
	if quiz[question]['answer'].lower() == ans.lower():
		print(f"You are correct! \nYour score is {total_correct_answers +1}!")
		return True
	else:
		print(f"That is the wrong answer :( \nYou have {attempts - 1} left! \nTry again...")
		return False

#Creating a way to allow players to have access to answer key by typing in game
def print_dictionary():
	for question_id, ques_answer in quiz.items():
		for key in ques_answer:
			print(key + ':', ques_answer[key])

#The game setup, adding an attempts rule where user can retry an answer 3 times and be alerted how many attempts they have left
intro = intro_message()
while True:
	total_correct_answers = 0
	for question in quiz:
		attempts = 3
		while attempts > 0:
                        
                        #adding a skip function withing the game
			print(quiz[question]['question'])
			answer = input("Enter Answer (To move to the next question, type 'skip') : ")
			if answer == "skip":
				break
			check = check_ans(question, answer, attempts, total_correct_answers)
			if check:
				total_correct_answers += 1
				break
			attempts -= 1
	break

#Adding an outro message with my personalized name
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)

class Creator(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
	def outro(self):
                print("\nThank you so much for playing my,", self.firstname, self.lastname, "game today! I hope you enjoyed it!!!")
                
x = Creator("Lisandra", "Gonzalez's,")
x.outro()


