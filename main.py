from room import Room
from item import Item
from character import Enemy
from character import Friend

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall.")
dining_hall.describe()

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with shiny wooden floors.")
ballroom.describe()

frisbee = Item("Frisbee")
frisbee.set_description("A disc to throw and have fun")
frisbee.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

jill = Enemy("Jill", "A wicked witch")
jill.set_conversation("Ding dong, the witch is here!")
jill.set_weakness("cauldron")

louise = Friend("Louise", "A friendly skeleton")
louise.set_conversation("How nice to see you here.")

dining_hall.set_character(dave)
ballroom.set_character(jill)
kitchen.set_character(louise)

current_room = kitchen

dead = False       

while dead == False:		
	print("\n")         
	current_room.get_details()

	inhabitant = current_room.get_character()
	if inhabitant is not None:
		inhabitant.describe()

        
	command = input("> ")
	# Check whether a direction was typed
	if command in ["north", "south", "east", "west"]:    
		current_room = current_room.move(command)
	elif command == "talk":
		# Add code here DONE
		if inhabitant is not None:
			inhabitant.talk()
	elif command == "fight":
		if inhabitant is not None:
			print("What will you fight with?")
			fight_with = input()
			if inhabitant.fight(fight_with) == False:
				print("You are dead!")
				dead = True
	elif command == "sleep":
		if inhabitant is not None:
			inhabitant.send_to_sleep()
	elif command == "hug":
		if inhabitant is not None:
			if isinstance(inhabitant, Friend):
				inhabitant.hug()
			else:
				print("I don't want to hug you!")
