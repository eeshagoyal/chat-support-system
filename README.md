# chat-support-system
This is a Rule Based Chat Bot and does not employee Natural Language Processing.
All the Text Queries are stored in a CSV file and are automatically accessed by the chatbot script.
## Pre requisites 
	Python 2.7.15

## Instructions
	1. Open 3 separate Bash Terminal windows
	2. On first window run "python server.py"
	3. On second window run "python client.py"
	4. On third window run "python human_support.py"
	5. The client can select a query from the given list or choose to submit a new query
	6. If query exists in the set list of queries the server will reply accordingly
	7. If query does not exist in the set list of queries, the client query will be forwarded to the third window ie- human support. 
	8. The client and client support team can then take part in a real time chat 

## Note 
	socket.error: [Errno 48] Address already in use
	sudo lsof -i:5000
	kill listed PID
	
## References 
- https://medium.com/botsupply/rule-based-bots-vs-ai-bots-b60cdb786ffa
- https://www.geeksforgeeks.org/simple-chat-room-using-python/

## Alternatives methods to build chat support
- https://hybrid.chat/project/appointment-booking-chatbot/
- https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html
