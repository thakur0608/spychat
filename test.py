from spy_details import friends ,Spy
from termcolor import colored


def select_friend ():
  item_number = 1
  for temp in friends:
      #print temp['name']
    print colored(('%d %s')  %(item_number , temp['name']),'magenta')
    item_number = item_number + 1
  friend_choice = int(raw_input("Choose from your friends"))
  friend_choice_position = friend_choice - 1
  print friend_choice_position

select_friend()

