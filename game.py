#Dictionary for characters
characters = [
    {"name": "Swordsman", "hp": 650, "dmg": 100, "defence": 70, "special": 200, "specialName": 'Cross Slash', "specialCooldown": 4},
    {"name": "Archer", "hp": 750, "dmg": 70, "defence": 50, "special": 130, "specialName": 'Arrow Barrage', "specialCooldown": 2},
    {"name": "Magician", "hp": 700, "dmg": 80, "defence": 60, "special": 155, "specialName": 'Elemental Bash', "specialCooldown": 3},
    {"name": "Doctor", "hp": 900, "dmg": 45, "defence": 95, "special": 140, "specialName": 'Deadly Mist', "specialCooldown": 3}
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
print('|4. Doctor: 900 HP - Attack Power: 45 - Defence: - 95 - Special: Deadly Mist - 140 DMG - Cooldown: 3 Turns     |')
print('----------------------------------------------------------------------------------------------------------------')

#set character for player and cpu
player1 = int(input('Player 1 Please Select A Character - '))
print(f'Player 1 Selected - {characters[player1 - 1]["name"]}' )
player2 = int(input('Player 2 Please Select A Character - '))
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

    print(f'Player {playerNum} Defends!')
    



#attack function
def attack(playerNum, damage, playerAttacking):
    print(f'\nPlayer {playerNum} Attacks!')
    
    defendedDamage1 = damage - characters[player1 - 1]["defence"]
    defendedDamage2 = damage - characters[player2 - 1]["defence"]

    if playerAttacking == 1:
        if defending_player1 == True:
            if defendedDamage1 < 0 :
                defendedDamage1 = 0
            characters[player1 - 1]["hp"] -= defendedDamage1
            print(f"{defendedDamage1} Damage Done!")
        else:
            characters[player1 - 1]["hp"] -= damage
            print(f"{damage} Damage Done!")

    elif playerAttacking == 2:
        if defending_player2 == True:
            if defendedDamage2 < 0 :
                defendedDamage2 = 0
            characters[player2 - 1]["hp"] -= defendedDamage2
            print(f"{defendedDamage2} Damage Done!")
        else:
            characters[player2 - 1]["hp"] -= damage
            print(f"{damage} Damage Done!")


specialCooldown1 = 0
specialCooldown2 = 0

#special function
def special(playerNum, nameOfSpecial, specialDmg, playerAttacking, cooldown):
    global specialCooldown1, specialCooldown2

    if playerAttacking == 1:           
        if specialCooldown1 == 0:
            if(nameOfSpecial == "Deadly Mist"):
                characters[player2 - 1]["hp"] += 65
                print('\nDoctor Healed Up 65 HP!')
            characters[player1 - 1]["hp"] -= specialDmg
            print(f"Player {playerNum} uses {nameOfSpecial}! {specialDmg} Damage Done!")
            specialCooldown1 = cooldown 
            print(f"Player {playerNum} Special Is Now On Cooldown. Turns Remaining Until Next Use: {specialCooldown1}")

        else:
            print(f"\nPlayer {playerNum} Tried To Use A Special But It Failed... \nTurns Remaining : {specialCooldown1}. \nDefending Instead\n")
            defend(playerNum)

    elif playerAttacking == 2:
        if specialCooldown2 == 0:
            if(nameOfSpecial == "Deadly Mist"):
                characters[player1 - 1]["hp"] += 65
                print('\nDoctor Healed Up 65 HP!')
            characters[player2 - 1]["hp"] -= specialDmg
            print(f"Player {playerNum} uses {nameOfSpecial}! {specialDmg} Damage Done!")
            specialCooldown2 = cooldown
            print(f"Player {playerNum} Special Is Now On Cooldown. Turns Remaining Until Next Use: {specialCooldown2}")

        else:
            print(f"\nPlayer {playerNum} Tried To Use A Special But It Failed... \nTurns Remaining : {specialCooldown2}. \nDefending Instead\n")
            defend(playerNum)



while characters[player1 - 1]["hp"] > 0 and characters[player2 - 1]["hp"] > 0:
    defending_player1 = False        
    move1 = input(f'\n{player1CurrentHP(int(characters[player1 - 1]["hp"]), characters[player1 - 1]["name"])} \nWhat do you want to do? ')
    if move1 == 'A' or move1 == 'a':
        attack(1, characters[player1 - 1]["dmg"], 2)
    elif move1 == 'D' or move1 == 'd':
        defend(1)
    elif move1 == 'S' or move1 == 's':
        special(1, characters[player1 - 1]["specialName"], characters[player1 - 1]["special"], 2, characters[player1 - 1]["specialCooldown"]) 

    defending_player2 = False
    move2 = input(f'\n{player2CurrentHP(int(characters[player2 - 1]["hp"]), characters[player2 - 1]["name"])} \nWhat do you want to do? ')
    if move2 == 'A' or move2 == 'a':
        attack(2, characters[player2 - 1]["dmg"], 1)
    elif move2 == 'D' or move2 == 'd':
        defend(2)
    elif move2 == 'S' or move2 == 's':
        special(2, characters[player2 - 1]["specialName"], characters[player2 - 1]["special"], 1, characters[player2 - 1]["specialCooldown"]) 

    if specialCooldown1 > 0: 
        specialCooldown1 = specialCooldown1 - 1
    elif specialCooldown1 == 0:
        specialCooldown1 = 0

    if specialCooldown2 > 0: 
        specialCooldown2 = specialCooldown2 - 1
    elif specialCooldown2 == 0:
        specialCooldown2 = 0