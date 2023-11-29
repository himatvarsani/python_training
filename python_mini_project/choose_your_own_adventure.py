name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? (Type left or right): ").lower()

if answer == "left":
    answer = input(" You come to a river, you can walk around it or swim across? (Type walk or swim): ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator. You lose!")
    elif answer == "walk":
        print("You walked for many miles, and ran out of water. You lose!")
    else:
        print("Not a valid option. You lose!")
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (Type cross or back): ").lower()
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to him (yes or no)? ").lower()
        
        if answer == "yes":
            print("You talked to the stranger and he gives you GOLD. You WIN!")
        
        elif answer == "no":
            print("You ignored the stanger and he has put a curse on you. You Lose!")
        
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")
    
else:
    print("Not a valid option. You lose!")

print("Thank you for playing", name)