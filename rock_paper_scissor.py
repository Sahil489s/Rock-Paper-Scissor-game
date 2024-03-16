import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your move= Rock,Paper,Scissor = ")
com_choice=random.choice(item_list)

print(F"User Choice = {user_choice} Computer Choice = {com_choice}")

if user_choice==com_choice:
    print("Both chooses same : = Match Tie ")
elif user_choice =="Rock":
    if com_choice == "Paper":
        print("paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice== "Paper" :
    if com_choice=="Scissor":
        print("Scissor cuts paper:-computer win")
    else:
      print("paper covers Rock:-You win")  
elif user_choice == "Scissor":
    if com_choice =="Paper":
        print("Scissor cuts paper:-You win")
    else:
        print("Rock Smashes Scissor:-Computer Win")









