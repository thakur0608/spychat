from spy_details import spy,friends,Spy
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
import time
import csv


print colored('welcome to spychat','red')
print colored("Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? ",'blue')
response=raw_input()


STATUS_MESSAGES = ['This is thakur, good', 'quick learner, be quick.']



def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy={"name":row[0],"salutation":row[1],"age":row[2],"rating":row[3],"chats":[]}

            friends.append(spy)



def start_chat():
    load_friends()
    current_status_message = None
    show_menu=True
    while show_menu:
        menu_choices =colored("\nWhat do you want to do? \n 1. Add a status update \n 2. add friend \n 3.select friend \n 4.send message \n 5.read message \n 6.read chat  history 7.exit",'blue')
        menu_choice = raw_input(menu_choices)

        if menu_choice == '1':
           current_status_message= add_status(current_status_message)
        elif menu_choice == '2':
            add_friend()
        elif menu_choice == '3':
            select_friend()
        elif menu_choice == '4':
            send_message()
        elif menu_choice == '5':
            read_message()
        elif menu_choice=='6':
            read_chat_history()
        else:
           show_menu = False
           print colored('thank you for using spy chat','cyan')



def add_status(current_status_message):
    updated_status_message=current_status_message
    if current_status_message != None:
           print colored("Your current status message is " + current_status_message + "\n",'green')
    else:
           print colored('You don\'t have any status message currently \n','red')
    default = raw_input("Do you want to select from the older status (y/n)?")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper() == 'Y':
            item_position = 1
            for message in STATUS_MESSAGES:
                print colored(str(item_position) + ". " + message,'blue')
                item_position = item_position + 1
            message_selection = input("\nChoose from the above messages ")
            if len(STATUS_MESSAGES) >= message_selection:
             updated_status_message = STATUS_MESSAGES[message_selection - 1]
    return updated_status_message


def add_friend():
  new_friend = {
    'name': '',
    'salutation': '',
    'age': 0,
    'rating': 0.0,
    'chats':[]
  }

  new_friend['name'] = raw_input("Please add your friend's name: ")
  new_friend['salutation']= raw_input("Are they Mr. or Ms.?: ")
  new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

  new_friend['age'] = int(raw_input("Age?"))
  new_friend['rating'] = float(raw_input("Spy rating?"))
  if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy.rating:
      friends.append(new_friend)
      print 'spy added'
      with open('friends.csv', 'wb') as friends_data:
          writer = csv.writer(friends_data)
          writer.writerow([new_friend['name'],new_friend['salutation'],new_friend['rating'],new_friend['age']])
  else:
      print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
  return len(friends)
def select_friend ():
    item_number = 1
    for temp in friends:

        print colored(('%d %s') % (item_number, temp['name']), 'magenta')
        item_number = item_number + 1
    friend_choice = int(raw_input("Choose from your friends"))
    friend_choice_position = friend_choice - 1
    return friend_choice_position
def send_message():
  friend_choice = select_friend()
  print friend_choice
  original_image = raw_input("What is the name of the image?")
  output_path = 'result.jpg'
  text = raw_input("What do you want to say?")
  print 'loading......'
  Steganography.encode(original_image, output_path, text)
  print 'Image generated'
  new_chat = {
      "message": text,
      "time": datetime.now(),

      "sent_by_me": True
  }

  friends[friend_choice]['chats'].append(new_chat)
  print colored("Your secret message is ready!",'green')
def read_message():
   friend_choice = select_friend()

   output_path = raw_input("What is the name of the file?")
   secret_text = Steganography.decode(output_path)

   new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
              }

   friends[friend_choice]['chats'].append(new_chat)
   if (len(secret_text)>100):

     friends.remove(friends[friend_choice])
     print "friend deleted" \
           ""
   else:
     print secret_text

def read_chat_history():

    read_for = select_friend()

    print '\n'
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            print(colored("You said:", 'red')),

            print str(chat.message)
        else:
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),

            print(colored(str(friends[read_for].name) + " said:", 'red')),

            print str(chat.message)
if response.upper() == "Y":
    password = raw_input("Enter password")
    if password == "1234":
        print colored("WELCOME %s. %s HAVE A NICE DAY ",'green')%(spy.salutation,spy.name )
        start_chat()
    else:
        print colored("WRONG PASSWORD",'red')
else:
    spy_name=raw_input('what is your name  ')
    if len(spy_name)==0:
        print "enter valid name"
        exit('try again')
    spy_sallutation=raw_input('what we should call you MR. OR MS.')
    if len(spy_sallutation)==0:
        print"enter valid details"
        exit('try again')
    spy_age=int(raw_input('what is your age'))
    if spy_age<1:
        print"enter valid age"
        exit('try again')
    else:
        print colored("hello %s  ,%s ,age:%d",'green')%(spy_sallutation,spy_name,spy_age)
        print "glad to have you"

    spy_rating=raw_input('do you want to rate us yes or no:')
    if(spy_rating)=="yes":
        spy_rating=raw_input( "give rating from 1 to 5 :")
        if spy_rating>4.5:
            print "you are awesome"

        elif (spy_rating)>3 and len(spy_rating)<4.5:
            print "you arre good hope we would improve it"
        else :
            print"thank you we will try to improve"

    else :
        print colored("hope you would enjoy time",'green')
    start_chat()



