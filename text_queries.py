class text_queries():

	def __init__(self):
		self.data = {

			"Hello":"Hello",

			"What do you do?": "I am a chatbot. I will try my best to solve your queries.",

			"Tell me about FinHawk": "FinHawk is a tech start up which aims to be your one stop solution to all things finance. It provides you with consolidated information and advice about the stock market. ",

			"Who are the founders?": "Abhipriya Gupta and Abhishek Batra",

			"Are you available on Play Store?": "We are still in the initial development phase but we will be there really soon.",

			"How to apply?": "Connect with us on LinkedIn",

			"What is your product?" : "AI powered Web Application",
		}

	def getquery(self):
		return self.data


'''

dictionary = text_queries().getquery() 
print dictionary.keys() 

message = raw_input()

print type(message)

if dictionary.has_key(str(message)): 
	message = dictionary[message] 
	print message


print "done"

if message in list(dictionary.keys()): 
	message = dictionary[message] 
	print message
'''
