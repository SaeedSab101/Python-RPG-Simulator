import random
import time

#Dictionary for characters
characters = [
    {"name": "Swordsman⚔️", "hp": 650, "dmg": 100, "defence": 70, "special": 200, "specialName": 'Cross Slash', "specialCooldown": 4},
    {"name": "Archer🏹", "hp": 750, "dmg": 70, "defence": 50, "special": 130, "specialName": 'Arrow Barrage', "specialCooldown": 2},
    {"name": "Magician🧙", "hp": 700, "dmg": 80, "defence": 60, "special": 155, "specialName": 'Elemental Bash', "specialCooldown": 3},
    {"name": "Doctor🥼", "hp": 900, "dmg": 45, "defence": 95, "special": 80, "specialName": 'Deadly Mist', "specialCooldown": 2}
]

#print welcome message and rules
print('Welcome to this RPG Simulator\n')

print('You will choose a character for you and your oponent by entering a number between 1 and 4')
print('Each character has multiple moves: A to Attack, D to Defend, and S for Special')
print('Each special ability has a cooldown once it has been used')
print('Once your HP falls below 0 you lose! So Good Luck!\n')

print('----------------------------------------------------------------------------------------------------------------')
print('|Please select from one of the following characters below:                                                     |')
print('|1. Swordsman: 650 HP - Attack Power: 100 - Defence - 70 - Special: Cross Slash - 200 DMG - Cooldown: 4 Turns  |')
print('|2. Archer: 750 HP - Attack Power: 70 - Defence: - 60 - Special: Arrow Barrage - 130 DMG - Cooldown: 1 Turns   |')
print('|3. Magician: 700 HP - Attack Power: 80 - Defence: - 50 - Special: Elemental Bash - 160 DMG - Cooldown: 2 Turns|')
print('|4. Doctor: 900 HP - Attack Power: 45 - Defence: - 95 - Special: Deadly Mist - 80 DMG - Cooldown: 2 Turns      |')
print('----------------------------------------------------------------------------------------------------------------')

level = int(input('Select A Level Between 1 and 3 For The CPU (Easy, Normal, Hard) - '))

availableChars = [1, 2, 3, 4]

#set character for player and cpu
player1 = int(input('Player 1 Please Select A Character - '))
print(f'Player 1 Selected - {characters[player1 - 1]["name"]}' )
availableChars.remove(player1)
player2 = random.choice(availableChars)
print(f'Player 2 Selected - {characters[player2 - 1]["name"]}' )

def player1CurrentHP(char, character):
    return(f'Player 1 - {character} - Current HP: {char}')

def player2CurrentHP(char, character):
    return(f'Player 2 - {character} - Current HP: {char}')

#defending bool
defending_player1 = False
defending_player2 = False

#defend function
def defend(playerNum):
    global defending_player1, defending_player2

    if playerNum == 1:
        defending_player1 = True
    if playerNum == 2:
        defending_player2 = True

    print(f'\nPlayer {playerNum} Defends!')
    



#attack function
def attack(playerNum, damage, playerAttacking, charName):
    print(f'\nPlayer {playerNum} Attacks!')
    
    defendedDamage1 = damage - characters[player1 - 1]["defence"]
    defendedDamage2 = damage - characters[player2 - 1]["defence"]

    if playerAttacking == 1:
        if defending_player1 == True:
            if defendedDamage1 < 0 :
                defendedDamage1 = 0
            if charName == 50:
                characters[player2 - 1]["hp"] -= 45
                print('Magician Blocks With Electric Field And Causes 45 Damage')
            characters[player1 - 1]["hp"] -= defendedDamage1
            print(f"{defendedDamage1} Damage Done!")
        else:
            charHP -= damage
            print(f"{damage} Damage Done!")

    elif playerAttacking == 2:
        if defending_player2 == True:
            if defendedDamage2 < 0 :
                defendedDamage2 = 0
            if charName == 50:
                characters[player1 - 1]["hp"] -= 45
                print('Magician Blocks With Electric Field And Causes 45 Damage')
            characters[player2 - 1]["hp"] -= defendedDamage2
            print(f"{defendedDamage2} Damage Done!")
        else:
            charHP -= damage
            print(f"{damage} Damage Done!")


specialCooldown1 = 0
specialCooldown2 = 0

#special function
def special(playerNum, nameOfSpecial, specialDmg, playerAttacking, cooldown):
    global specialCooldown1, specialCooldown2

    if playerAttacking == 1:           
        if specialCooldown1 == 0:
            print(f"\nPlayer {playerNum} uses {nameOfSpecial}!")
            if(nameOfSpecial == "Deadly Mist"):
                characters[player2 - 1]["hp"] += 65
                print(f'Doctor Healed Up 65 HP! Current HP - {characters[player2 - 1]["hp"]}')
            characters[player1 - 1]["hp"] -= specialDmg
            print(f"{specialDmg} Damage Done!")
            specialCooldown1 = cooldown 
            print(f"Player {playerNum} Special Is Now On Cooldown. Turns Remaining Until Next Use: {specialCooldown1}")

        else:
            print(f"\nPlayer {playerNum} Tried To Use A Special But It Failed... \nTurns Remaining : {specialCooldown1}. \nDefending Instead")
            defend(playerNum)

    elif playerAttacking == 2:
        if specialCooldown2 == 0:
            print(f"\nPlayer {playerNum} uses {nameOfSpecial}!")
            if(nameOfSpecial == "Deadly Mist"):
                characters[player1 - 1]["hp"] += 65
                print(f'Doctor Healed Up 65 HP! Current HP - {characters[player1 - 1]["hp"]}')
            characters[player2 - 1]["hp"] -= specialDmg
            print(f"{specialDmg} Damage Done!")
            specialCooldown2 = cooldown
            print(f"Player {playerNum} Special Is Now On Cooldown. Turns Remaining Until Next Use: {specialCooldown2}")

        else:
            print(f"\nPlayer {playerNum} Tried To Use A Special But It Failed... \nTurns Remaining : {specialCooldown2}. \nDefending Instead")
            defend(playerNum)




def level1():
    move2 = random.randint(1,5)
    print(f'\nCPU - {player2CurrentHP(int(characters[player2 - 1]["hp"]), characters[player2 - 1]["name"])}')
    print_thinking_dots(3)
    if move2 == 1 or move2 == 2:
        attack(2, characters[player2 - 1]["dmg"], 1, characters[player2 - 1]["defence"])
    elif move2 == 3 or move2 == 4:
        defend(2)
    elif move2 == 5:
        special(2, characters[player2 - 1]["specialName"], characters[player2 - 1]["special"], 1, characters[player2 - 1]["specialCooldown"]) 

def level2():
    move2 = random.randint(1,3)
    print(f'\nCPU - {player2CurrentHP(int(characters[player2 - 1]["hp"]), characters[player2 - 1]["name"])}')
    print_thinking_dots(3)
    if move2 == 1:
        attack(2, characters[player2 - 1]["dmg"], 1, characters[player2 - 1]["defence"])
    elif move2 == 2:
        defend(2)
    elif move2 == 3:
        special(2, characters[player2 - 1]["specialName"], characters[player2 - 1]["special"], 1, characters[player2 - 1]["specialCooldown"]) 

def level3():
    move2 = random.randint(1,9)
    print(f'\nCPU - {player2CurrentHP(int(characters[player2 - 1]["hp"]), characters[player2 - 1]["name"])}')
    print_thinking_dots(3)
    if move2 >= 1 and move2 <= 3:
        attack(2, characters[player2 - 1]["dmg"], 1, characters[player2 - 1]["defence"])
    elif move2 == 4 or move2 == 5:
        defend(2)
    elif move2 >= 6 and move2 <= 9:
        special(2, characters[player2 - 1]["specialName"], characters[player2 - 1]["special"], 1, characters[player2 - 1]["specialCooldown"]) 
    

def print_thinking_dots(duration):
    print('CPU is thinking', end='', flush=True)
    for _ in range(duration):
        time.sleep(1)
        print('.', end='', flush=True)
    print()


while characters[player1 - 1]["hp"] > 0 and characters[player2 - 1]["hp"] > 0:
    defending_player1 = False        
    move1 = input(f'\n{player1CurrentHP(int(characters[player1 - 1]["hp"]), characters[player1 - 1]["name"])} \nWhat do you want to do? ')
    if move1 == 'A' or move1 == 'a':
        attack(1, characters[player1 - 1]["dmg"], 2, characters[player1 - 1]["defence"])
    elif move1 == 'D' or move1 == 'd':
        defend(1)
    elif move1 == 'S' or move1 == 's':
        special(1, characters[player1 - 1]["specialName"], characters[player1 - 1]["special"], 2, characters[player1 - 1]["specialCooldown"]) 

    if characters[player2 - 1]["hp"] < 0:
        print('\nGame Over! Player 1 Wins!')
        break

    defending_player2 = False
    
    if level == 1:
        level1()
        if characters[player1 - 1]["hp"] < 0:
            print('\nGame Over! Player 2 Wins!')    
            break
    elif level == 2:
        level2()
        if characters[player1 - 1]["hp"] < 0:
            print('\nGame Over! Player 2 Wins!')    
            break
    elif level == 3:
        level3()
        if characters[player1 - 1]["hp"] < 0:
            print('\nGame Over! Player 2 Wins!')    
            break

    if specialCooldown1 > 0: 
        specialCooldown1 = specialCooldown1 - 1
    elif specialCooldown1 == 0:
        specialCooldown1 = 0

    if specialCooldown2 > 0: 
        specialCooldown2 = specialCooldown2 - 1
    elif specialCooldown2 == 0:
        specialCooldown2 = 0

print('Good Game!👏')
