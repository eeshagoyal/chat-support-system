class text_queries():

	def __init__(self):
		self.data = {

			"Who are you?": "Hi! I am FinHawk customer support",

			"Tell me about FinHawk": "It is the best available online solution for people who want to enter into stock trading market",

			"Who are the founders?": "It's Abhipriya Gupta and Abhishek Batra",

			"What does FinHawk do?": "We're building an ecosystem to help people achieve their financial goals in an educated and informed way.",

			"Where can I find FinHawk on the internet?": "You can find us on angel.co"

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
