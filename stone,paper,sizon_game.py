import random
list = ["s", "p","z"] 
while True:
    print("----------------------------------START GAME----------------------------------")
#s for stone
#p for paper
#z for sizon

    print("\n--->s for stone \n--->p for paper \n--->z for sizon")
    def game():
        i = 1
        for i in range(0,3):
            computer_choice = random.choice(list)
            user_choice = input("Enter your choice: ")
            if computer_choice == user_choice:
                print(f"computer choice is  {computer_choice} and your choice is {user_choice} ")
                print("try..again..!")
                i = i-1 
        
            elif computer_choice == "s" and user_choice == "p":
                print("computer choice is  STONE and your choice is PAPER ")
                print("You are Win....") 
             
            elif computer_choice == "s" and user_choice == "z":
                print("computer choice is  STONE and your choice is SIZON ")
                print("You are Loose....")
            
            elif computer_choice == "p" and user_choice == "s":
                print("computer choice is  PAPER and your choice is STONE ")
                print("You are Loose....")
            
            elif computer_choice == "p" and user_choice == "z":
                print("computer choice is  PAPER and your choice is SIZON ")
                print("You are Win....")
            
            elif computer_choice == "z" and user_choice == "s":
                print("computer choice is  SIZON and your choice is STONE ")
                print("You are Win....")
            
            elif computer_choice == "z" and user_choice == "p":
                print("computer choice is SIZON and your choice is PAPER ")
                print("You are Loose....")
            else:
                print("wrong choice...")
            
            i=i+1
    r = game()
    print("----------------------------------GAME OVER----------------------------------")