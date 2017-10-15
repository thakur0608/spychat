import datetime
class Spy:
    def __init__(self, name, salutation, age, rating):
      self.name = name
      self.salutation = salutation
      self.age = age
      self.rating = rating

      self.chats = []
      self.current_status_message = None

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
spy = Spy('thakur', 'Mr.', 21, 4.7)
friend_one = {'name':'vishal', 'age': 21,'ratinng': 4.9,'chats':[]}
friend_two = {'name':'sant', 'age': 21,'ratinng': 4.9,'chats':[]}
friend_three = {'name':'saman', 'age': 21,'ratinng': 4.9,'chats':[]}
friends = [friend_one, friend_two, friend_three]