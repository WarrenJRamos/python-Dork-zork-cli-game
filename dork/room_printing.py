class Room1Printing():

    def print_move(self, room, direction):
        """
        Prints a statement to user after player moves a certain direction
        """
        if room == "room 1":
            if direction == "north":
                print("You enter the boss room.")
            if direction == "south":
                print("You cannot go/move south.")
            if direction == "east":
                print("There is a table in the room with a donut on top.")
            if direction == "west":
                print("There is a beautiful garden with the roadrunner's " +
                      "nest right \nin the center of the garden. The nest " +
                      "has eggs that look about \nready to hatch but no " +
                      "roadrunner parent to be seen.")

        if room == "room 2":
            if direction == "north":
                print("You are in the dean’s office. The dean is irritated " +
                      "that you are \nin the room. You have 1 minute to make " +
                      "him happy; otherwise, campus \nsecurity will arrive " +
                      "and take you away.")
            if direction == "south":
                print("You fall to your death.")
            if direction == "east":
                print("You are unable to go East.")
            if direction == "west":
                print("You are inside the Student Success Building. There " +
                      "is a locked cage \nwith a roadrunner inside. It looks " +
                      "starving and nervous. \nThere is a piece of paper " +
                      "next to the cage.")

        if room == "room 3":
            if direction == "north":
                print("You are in the dean’s office. The dean is irritated" +
                      " that you are in \nthe room. You have 1 minute to make " +
                      "him happy; otherwise, \ncampus security will arrive " +
                      "and take you away.")
            if direction == "south":
                print("You are unable to go South.")
            if direction == "east":
                print("You are inside the Student Success Building. There " +
                      "is a locked cage \nwith a roadrunner inside. It looks " +
                      "starving and nervous. \nThere is a piece of paper " +
                      "next to the cage.")
            if direction == "west":
                print("You are unable to go West.")

        if room == "room 4":
            if direction == "north":
                # Ask teammates about whether or not to include an extra parameter for this method
                print("The blue door is unlocked, and you enter a room with " +
                      "a gold key.")
                print("The dean is blocking the door and does not let you " +
                      "through. You cannot enter this room.")
            if direction == "south":
                print("You are inside the Student Success Building. There " +
                      "is a locked cage \nwith a roadrunner inside. It looks " +
                      "starving and nervous. \nThere is a piece of paper " +
                      "next to the cage.")
            if direction == "east":
                print("There is a table in the room with a donut on top.")
            if direction == "west":
                print("There is a beautiful garden with the roadrunner's " +
                      "nest right \nin the center of the garden. The nest " +
                      "has eggs that look about \nready to hatch but no " +
                      "roadrunner parent to be seen.")

        if room == "room 5":
            if direction == "north":
                print("You are unable to go North.")
            if direction == "south":
                print("You are in the dean’s office. The dean is irritated" +
                      " that you are in \nthe room. You have 1 minute to make " +
                      "him happy; otherwise, \ncampus security will arrive " +
                      "and take you away.")
            if direction == "east":
                print("You are unable to go East.")
            if direction == "west":
                print("You are unable to go West.")

    def print_look(self, room, direction):
        """
        Prints a statement after user looks a certain direction
        """
        if room == "room 1":
            if direction == "north":
                print("There is a door with a sign that says DANGER.")
            if direction == "south":
                print("There is bag of bird food with all sorts of insects " +
                      "that roadrunners love to eat.")
            if direction == "east":
                print("To the East, there is a sign that says Lounge.")
            if direction == "west":
                print("To the West, there is a sign that says Roadrunner's Nest")

        if room == "room 2":
            if direction == "north":
                print("There is a sign that says DANGER!!")
            if direction == "south":
                print("There is a 1000 ft cliff with spikes.")
            if direction == "east":
                print("There is an empty wall.")
            if direction == "west":
                print("There is a sign that says Student Success Building.")

        if room == "room 3":
            if direction == "north":
                print("There is a sign that says DANGER!!")
            if direction == "south":
                print("There is an empty wall.")
            if direction == "east":
                print("There is a sign that says Student Success Building.")
            if direction == "west":
                print("There is an empty wall.")

        if room == "room 4":
            if direction == "north":
                print("There is blue door that is being guarded by the dean.")
            if direction == "south":
                print("There is a sign that says Student Success Building.")
            if direction == "east":
                print("To the East, there is a sign that says Lounge.")
            if direction == "west":
                print("To the West, there is a sign that says Roadrunner’s Nest.")

        if room == "room 5":
            if direction == "north":
                print("There is an empty wall.")
            if direction == "south":
                print("There is a blue door")
            if direction == "east":
                print("There is an empty wall.")
            if direction == "west":
                print("There is an empty wall.")

    def print_score(self, score):
        """
        Prints out the score
        """
        print("You have a score of " + str(score))

    def print_diagnostic(self, health_score):
        """
        Prints out the health data of the player
        """
        print("You have a health score of: " + str(health_score))

    def print_get(self, item):
        """
        Prints the item stored into player inventory
        """
        print("You put the " + item + " in your inventory")

    def print_read(self, item):
        """
        Prints the item that is being read.
        """
        if item == "paper":
            print("I don't like this bird. Dispose of it for me. - Dean")
        else:
            print(item + "was not found")

    def print_drop_item(self):
        """
        Print the item being dropped
        """
        print("CHANGE THIS FOR FUTURE SPRINT")

    def print_open_item(self, item):
        """
        Print what happens after player open the item.
        """
        print("You successfully open the " + item +
              ", and the bird hops on your shoulder. " +
              "The bird is added to your inventory.")
        # Call the add_inventory() method here

    def print_move_moveable(self):
        """
        Prints what happens after the item is moved
        """
        print("CHANGE THIS LATER")

    def print_attack(self, creature):
        """
        Prints out what happens after the player attacks a creature
        """
        if creature == "dean":
            print("You run up to the dean and start punching him. He is in " +
                  "lots of pain but was able to call security to take you away. GAME OVER.")
            from dork.commandManager import CommandManager
            CommandManager.setGameOver(True)
        else:
            print("You cannot attack " + creature)

    def print_examine(self, item):
        """
        Print out what happens when the player examines an item
        """
        if item == "paper":
            print("I don't "+ "like this bird. Dispose of it for me. - Dean")
        elif item == "roadrunner":
            print("The roadrunner is in bad condition. It looks starving and nervous.")
        elif item == "cage":
            print("The cage is tight, dirty, and locked.")
        else:
            print(item + " is unable to be examined")

    def print_inventory(self, inventory):
        """
        Print out the player's inventory
        """
        print("You currently have:")
        for items in inventory:
            print(items + " ")

    def print_eat_food(self, item):
        """
        Print out what happens after player eats item.
        """
        if item == "donut":
            print("The donut is yummy. Unfortunately, the player dies " +
                  "as THE DONUT IS POISONOUS!!! GAME OVER")
            from dork.commandManager import CommandManager
            CommandManager.setGameOver(True)
        else:
            print(item + "is not something you can eat.")

    def print_feed_creature(self, food):
        """
        Print what happens after player feeds the runner
        """
        if food == "donut":
            print("Through one of the tiny openings in the cage, you drop " +
                  "the donut into the cage. The roadrunner finished the donut " +
                  "AND DIES!!! You figure out the donut is poisonous! GAME OVER!")
            from dork.commandManager import CommandManager
            CommandManager.setGameOver(True)
        if food == "bird food":
            print("Through one of the tiny openings in the cage, you drop some " +
                  "bird food into the cage. The roadrunner eats the food and seems " +
                  "energized.")
        if food is None:
            print("There is nothing to feed the bird with.")

    def print_give_item(self):
        """
        Print what happens after player gives the item
        """
        print("CHANGE THIS LATER")
        