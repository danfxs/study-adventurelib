from adventurelib import *

broom = Item('a broken broom', 'broom')

print(f'You sweep away cobwebs with {broom}')

Item.colour = 'grey'

mug = Item('mug')
mug.colour = 'red'

inventory = Bag()
inventory.add(mug)
inventory.add(broom)

@when('look at ITEM')
def look(item):
    obj = inventory.find(item)
    if not item:
        print(f"You do not have a {item}.")
    else:
        print(f"It's a sort of {obj.colour}-ish colour.")


class MaleCharacter(Item):
    subject_pronoun = 'he'
    object_pronoun = 'him'

wizard = MaleCharacter('a wizard')
wizard.def_name = 'the wizard'

start()
