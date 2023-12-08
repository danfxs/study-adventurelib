from adventurelib import *

Room.add_direction('up', 'down')
Room.add_direction('enter', 'exit')

cur_room = Room("")
tent = Room("Tent")
camp = Room("Camp")
river = Room("River")
camp.enter = tent
camp.down = river
camp.north = tent
cur_room = camp

@when('go room DIRECTION')
def go_into_direction(direction):
  global cur_room
  room = getattr(cur_room, direction)
  if room:
    cur_room = room
  print(cur_room)


start()