print("Welcome to 'Guess the code'")
print("You have to guess the code within three chances and for each correct guess, you are rewarded a point.")
print("Also, you can decide the range within which the code will be generated.")
import random   
while True:
    y=input("Enter 'yes' to play or any other key to exit: ")
    if y!= "yes":
        print("Thank you for playing. Have a great day :)")
        break
    l=int(input("Enter the lower limit: "))
    u=int(input("Enter the upper limit: "))
    r=random.randint(l,u)
    count=0
    point=0
    while count<3:
        x=int(input("Guess the code: "))
        if x>r:
            if count<2:
                print("\n","Have one more try, your guess was too high.","\n")
        elif x<r:
            if count<2:
                print("\n","Have one more try, your guess was too low.","\n")
        else:
            print("\n","Gotcha!","You are rewarded a point.","\n")
            r=random.randint(l,u)
            point+=1
        count+=1
    if point==0:
        print("Your score is 0","\n","Better luck next time.",sep="\n")
    elif point==3:
        print("Your score is 3","\n","You are a pro player!",sep="\n")
    else:
        print("Your score is",point,"\n","Congrats, you are an intermediate player.")
