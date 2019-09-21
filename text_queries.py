import csv

class text_queries():

	def __init__(self):

		with open('Text_Queries.csv', mode='r') as infile:
			reader = csv.reader(infile)
			self.data = {rows[0]:rows[1] for rows in reader}

	def getquery(self): 
		return self.data
