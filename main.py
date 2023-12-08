from adventurelib import *
import adventurelib
import random

#Room.add_direction('up', 'down')
#Room.add_direction('enter', 'exit')

@when("scream")
def scream():
  print("You unleash a piercing shriek that reverberates around you.")


@when('go north')
@when('ir para cima')
@when('vai para norte')
def movimentar():
  say("""
    Você passa através de uma grande enorme estrada e chega na próxima floresta
  """)


@when('take THING')
def pegar(thing):
  say(f"Você pegou a {thing}")


@when("give ITEM to RECIPIENT")
def give(item, recipient):
  say(f"Você dá {item} para {recipient}")


# Algoritmo greedy deixa RECIPIENT somente com a última palavra
@when("give ITEM RECIPIENT")
def give2(item, recipient):
  say(f"Você dá {item} para {recipient}")


@when('shout', action='bellow')
@when('yell', action='holler')
@when('scream', action='shriek')
def shout(action):
  print(f'You {action} loudly.')


@when('look')
def look():
  print(current_room)


class TesteRoom():
  def __init__(self, dir):
    self.south = dir
    self.outside = None
  def __str__(self) -> str:
    return self.south


current_room = TesteRoom("Floresta")
current_room.south = "Praia"
playground = TesteRoom("Playground")
current_room.outside = playground


@when('go south')
def go_south():
  global current_room
  current_room = current_room.south
  print('You go south.')
  look()

@when('exit')
def exit_room():
  global current_room
  if current_room.outside:
    current_room = current_room.outside
  else:
    say("Exit what? You're already outside")
  look()


@when('cast SPELL', context='wonderland')
def cast(spell):
  say(f"You cast the {spell}.")

@when('enter mirror')
def enter_mirror():
  if get_context() == 'wonderland':
    say('There is no mirror here')
  else:
    set_context('wonderland')
    say('You step into the silvery surface, which feels wet and cool')
    say('You realise that clicking your heels will let you return')

@when('click heels', context='wonderland')
def click_heels():
  set_context(None)
  say('The momen your heels touch the world rearranges around you')

@when('land', context='wonderland.flying')
def land():
  set_context('wonderland')
  say('You gradually drop until you feel the earth beneath your feet')

@when('fly', context='wonderland')
def fly():
  set_context('wonderland.flying')
  say('You open your wings and go straight up to the sky')

space = Room("""
             You are drifting in space, It feels very cold.

             A slate-blue spaceshop sits completely silently to your left,
             its airlock open and waiting
             """)

spaceship = Room(
  """
  The bridge if the spaceship is shiny and white, with thousands of small, red, blicking lights.
  """
)

cur_room = space

@when('enter airlock')
def enter_spaceship():
  global cur_room
  if cur_room is not space:
    print("There is no airlock here.")
    return
  cur_room = spaceship
  print("You heave yourself into the airlock and slam your " +
        "hand on the button to close the outer door.")
  print(cur_room)

Room.can_scream_room = True
space.can_scream_room = False

@when('scream in room')
def screm_in_room():
  if cur_room.can_scream_room:
    print("You unleash a piercing shriek that " +
          "reverberates around you.")
  else:
    print(
      "You try to yell but there's no sound " +
      "in the vacuum of space."
    )

space.north = spaceship

print(space.north is spaceship)
print(spaceship.south is space)
print(space.exits())
print(type(space))
print(space.exit('north'))

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
  global cur_room
  print(cur_room)
  room = cur_room.exit(direction)
  if room:
    cur_room = room
    print(f'You go {direction}.')
    look()

def prompt():
  return '{hp}HP > '.format(hp=10)


def no_command_matches(command):
  print(random.choice(['Huh?', 'Sorry?', 'I beg your pardon?']))


adventurelib.no_command_matches = no_command_matches
adventurelib.prompt = prompt

start()
