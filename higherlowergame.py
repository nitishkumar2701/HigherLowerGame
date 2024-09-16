import game_data
import random
import ascii

print(ascii.game_intro)
print("Welcome to Higher Lower Game \n Find the correct option who has more instagram followers\n")
gamedata = game_data.data
random_number_a = random.randint(0,len(gamedata)-1)
random_number_b = random.randint(0,len(gamedata)-1)

A_data = gamedata[random_number_a]
B_data = gamedata[random_number_b]
Score = 0
GamePlay = True

while GamePlay:
    if(A_data['Name'] == B_data['Name']):
        A_data = gamedata[random.randint(0,len(gamedata)-1)]
        
    print(f"{A_data['Name']} | {A_data['Description']} | {A_data['Country']}")
    print(ascii.versus)
    print(f"{B_data['Name']} | {B_data['Description']} | {B_data['Country']}")
    print(f"\nScore - {Score}")
    user_input = input("\nChoose A or B -> \n").lower()
    if(user_input == "b"):
        if(B_data['FollowerCount'] > A_data['FollowerCount']):
            A_data = B_data
            B_data = gamedata[random.randint(0,len(gamedata)-1)]
            GamePlay = True
            Score += 1
        else:
            GamePlay = False
            print("Oops! You Guessed It Wrong")
            print(f"You score is - {Score}")
    elif(user_input == "a"):
        if(A_data['FollowerCount'] > B_data['FollowerCount']):
            B_data = A_data
            A_data = gamedata[random.randint(0,len(gamedata)-1)]
            GamePlay = True
            Score += 1
        else:
            GamePlay = False
            print("Oops! You Guessed It Wrong")
            print(f"You score is - {Score}")
    else:
        print("Please enter valid choice A or B")
        GamePlay = True
