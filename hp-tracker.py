#!/usr/bin/env python

 

# HP tracker

from sys import exit

 

class NPC:

    # class to track any NPCs that are created

    def __init__(self,name,hp):

        self.name = name

        # handle max hp and current hp separately to handle overhealing

        self.max_hp = hp

        self.current_hp = hp

        # all NPCs start alive

        self.status = 'Alive'

 

    # print NPC's current health status

    def __str__(self):

        return f'{self.name} current HP - {self.current_hp}'

   

    # handle damage dealt

    def take_damage(self,damage_value):

        self.damage_value = damage_value

        self.current_hp -= self.damage_value

        print(f'{self.name} has taken {self.damage_value} damage')

       

        # if hp goes below 0:

        if self.current_hp <= 0:

            self.current_hp = 0

            self.status = 'Dead'

            return self.status

   

    # handle any healing

    def heal(self,heal_value):

        self.heal_value = heal_value

        self.current_hp += self.heal_value

     

        # handle overhealing

        if self.current_hp > self.max_hp:

            # set current hp to max hp rather than overheal

            self.current_hp = self.max_hp

            print(f'{self.name} has been healed to {self.max_hp} HP')

        else:

            print(f'{self.name} has been healed to {self.current_hp} HP')

 

           

# Functions

 

def get_npc_name():

    # get NPC name and HP

    # check if they want to add more NPCs

    name = input('Enter NPC name/reference (Q to stop adding NPCs): ').lower()

    return name

   

   

def get_npc_hp():

    while True:

        try:

            hp = int(input('Enter NPC HP: '))

        except ValueError:

            hp = print('Invalid HP - please enter a number.')

        else:

            break

    return hp

   

           

def create_npc(name,hp):

    # create NPC

    npc = NPC(name, hp)

    return npc

 

def print_npc_status(party):

    # print a list of the current party

    print('\nCurrent NPC Status:')

    for k, v in party.items():

        print(f'NPC: {party[k].name} - Current HP: {party[k].current_hp}/{party[k].max_hp} - Status: {party[k].status}')

    print('\n')

   

 

def handling_game_mechanics_menu():

    option = input('Choose a mechanic you would like to handle: D - Damage Received; H - Healing Received: ').lower()

    return option

 

def get_target_npc():

    while True:

        npc = input('Enter target\'s name: ')        

        if npc in party.keys():

            break

        else:

            print('Please enter a valid target')

    return npc

       

# App logic

 

print('\n')

print('\n')

print('_______________Welcome to the DnD NPC HP tracker_______________')

print('\n')

print('\n')

 

# dictionary and variables to track all NPCs

party = {}

setting_up_party = True

handling_game_mechanics = True

death_count = 0

 

while setting_up_party:

 

    # get NPC name and HP, and check if more want to be added

    npc_name = get_npc_name()

    if npc_name == 'q':

        break

    else:

        npc_hp = get_npc_hp()    

        # create add NPC to party

        npc = create_npc(npc_name, npc_hp)

        party.update({npc_name: npc}) # nb - to access attributes of object in dict, use party['name'].attr

 

# print NPC's current status

print_npc_status(party)

 

# moving onto handling the game mechanics

 

while handling_game_mechanics:

    # ask user whether they're handling damage dealt or healing received

    option = handling_game_mechanics_menu()  

 

    if option == 'd':

        # get npc to be handled for damage

        target_npc = get_target_npc()                    

       

        # create loop to handle damage input

        while True:

            try:

                target_damage_value = int(input('Enter damage received: '))

                party[target_npc].take_damage(target_damage_value)

                # handle NPC death

                if party[target_npc].status == 'Dead':

                    death_count += 1

                #else:

                    #continue                

                # print NPC's current status

                print_npc_status(party)

               

                # if all NPCs are dead

                if death_count >= len(party):

                    print('All NPCs are dead! Combat over')

                    exit()

 

            except ValueError:

                print('Please enter a valid number for damage received')

            else:

                break

   

    elif option == 'h':

        # get npc to be handled for healing

        target_npc = get_target_npc()

        # create loop to handle healing input

        while True:

            try:

                target_healing_value = int(input('Enter healing received: '))

                party[target_npc].heal(target_healing_value)

 

                # handle healing from dead

                if party[target_npc].status == 'Dead':

                    party[target_npc].status = 'Alive'

                    death_count -= 1

 

                # print NPC's current status

                print_npc_status(party)

 

            except ValueError:

                print('Please enter a valid number for healing received')

            else:

                break

   

    # if option isn't d or h, repeat the menu

    else:

        # repeat the loop

        continue

       

 
