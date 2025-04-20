print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You are nearing the edge of the forest, would you like to go left or right?').lower()
if choice1 == "left":
    print('You are safe.... for now.')
    choice2 = input("You find yourself overlooking a rapid river. Would you like to 'swim' through it, or 'wait' for a boat?").lower()
    if choice2 == 'wait':
        print('A boat arrives and takes you safely across the river')
        choice3 = input('You made it across the river. Congrats nerd! On the other side of the river, you find three doors. One is red, one is blue, and one is yellow. Which door would you like to go through?' ).lower()
        if choice3 == "red":
            print('It was a bomb. You blew up. That is the whole door. Do you really think this treasure is worth it?')
        elif choice3 == "blue":
            print('Well, who would have guessed, it was a bomb. You died, dork')
        elif choice3 == "yellow":
            print('You did it! You find the great hidden treasure!! It is $1. Dont spend it all in one place kid')
        else:
            print('What does that even mean? You had to choose one of the three colors, dufus.')
    elif choice2 == "swim":
        print('Oof, the water was cold and flowing fast. You didnt make it chief')
    else:
        print('You wanna try that again? You had two choices big dog, swim or wait.')
elif choice1 == "right":
    print('You died, dork. For no specific reason either, you just died. It could have been spontaneous combustion, or the act of a cruel god, who knows. All I know is you went right, and you died.')
else:
    print('Not sure what you mean by that, pal. left or right?')