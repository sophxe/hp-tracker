#!/usr/bin/env python

 

# HP tracker

from sys import exit

 

class NPC:

    # class to track any NPCs that are created

    def __init__(self,name,hp,condition="OK"):

        self.name = name

        # handle max hp and current hp separately to handle overhealing

        self.max_hp = hp

        self.current_hp = hp

        # all NPCs start alive

        self.hp_status = 'Alive'

        # all NPCs have no health conditions, e.g. blinded

        self.condition="OK"

 

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

            self.hp_status = 'Dead'

            return self.hp_status

   

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
    
    def condition_change(self,condition):
        
        self.condition = condition

 

           

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

        # only print condition when status is alive

        if party[k].hp_status == "Alive":

            print(f'NPC: {party[k].name} - Current HP: {party[k].current_hp}/{party[k].max_hp} - HP Status: {party[k].hp_status} - Condition: {party[k].condition}')
        
        else: 

            print(f'NPC: {party[k].name} - Current HP: {party[k].current_hp}/{party[k].max_hp} - HP Status: {party[k].hp_status}')

    print('\n')

   

 

def handling_game_mechanics_menu():

    option = input('Choose a mechanic you would like to handle: D - Damage Received; H - Healing Received; C - Condition Change: ').lower()

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

if __name__ == "__main__":

    try:

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

                        if party[target_npc].hp_status == 'Dead':

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

                        if party[target_npc].hp_status == 'Dead':

                            party[target_npc].hp_status = 'Alive'

                            death_count -= 1

        

                        # print NPC's current status

                        print_npc_status(party)

        

                    except ValueError:

                        print('Please enter a valid number for healing received')

                    else:

                        break
            
            elif option == 'c':
                

                target_npc = get_target_npc()

                # get and set condition           

                target_condition = input('Enter condition: ')

                party[target_npc].condition = target_condition

                print_npc_status(party)

        

            # if option isn't d/h/c, repeat the menu

            else:

                # repeat the loop

                continue
    
    except KeyboardInterrupt:
        print("\nClosing...")
