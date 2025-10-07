# let the python to guess a number and we are trying to find out the number
import random
        
def WellcomeMenu():
    condition=True
    print("well come \nwhat is your name:")
    while(condition):
        name=input("enter hear:")
        if name.isdigit():
            print("name cant be number....")
        else:
            print(f"well hello {name}\n\n")
            print("\n\t\t\tGAME RULES\n")
            print("\t 1)the user and compute guesses in between 1 to 10\n")
            print("\t 2)user shude select the difficulty level (easy,medium,hard)\n")
            print("\t 3)easy have 10 chances for both user and compute\n")
            print("\t 4)medium hace 5 chances and hard hace 3 chances\n")
            print("\t 5)user shude select the option for guess by him or computer\n")
            condition=False
    
def UserOption():
    print("let you to guess or computer to guess\n1).enter 1 you will guessing the number\n2).enter 2 computer guessing the number\n3).enter 3 to exit \n4).enter 0 for back menu")
    prmchoise=input("enter hear:")
    return prmchoise

def MenuOption():
    print("\n\t\tENTER THE MODE :\n")
    print("enter 1 for easy (you will get 10 chances)\nenter 2 for medium (you will get 5 chances)\nenter 3 for hard (you will get 3 chances)\n")
    print("ente 0 to exit\n")
    mode=int(input("enter your option:"))
    return mode
start=1
end=10
def guessnum(start,end):
    return random.randint(start,end)

def easy():
    option=UserOption()
    if int(option)==1:
        print("you will guessing number\n")
        print("you have 10 chances\n")
        atempts=10
        userguess(atempts)
    
    elif int(option)==2:
        print("you shude chuse a number\n")
        print("computer is guessing the number \n")
        atempts=10   
        computerguess(atempts)
            
    elif int(option)==3:
        print("you are now exited")
        exit()
    elif int(option)==0:
        game()
    else:
        print("\ninvalid option please enter again......!\n")
        easy()
def computerguess(atempts):
    usernumber=input("enter your number :")
    if usernumber.isdigit():
        computernumer=guessnum(start,end)
        count=0
        print(f"i gussed  {computernumer} is it your number")
        while (count !=atempts):
            userop=int(input("enter yes(0) or large(2) or small(1) :"))
            storegussnum=0
            count+=1
            
            if userop.is_integer():
                if userop==0: 
                    print(f"computer guessed {computernumer} computer win 😊\n")
                    print("whant to play again 1 to play 0 to exit\n")
                    againoption=int(input("enter heare :"))
                    if againoption==1:
                        game()
                    else:
                        exit()
                elif count==atempts:
                    print("computer is out of chances you win 🎉...\n")
                    print("whant to play again 1 to play 0 to exit\n")
                    againoption=int(input("enter heare :"))
                    if againoption==1:
                        game()
                    else:
                        exit()
                elif userop==2:
                    storegussnum=random.randint(int(usernumber),end)
                    print(f" i guessed {storegussnum} is it your number")
                elif userop==1:
                    storegussnum=random.randint(start,int(usernumber))
                    print(f" i guessed {storegussnum} is it your number") 
                else:
                    print("sorry im cant able to understand your option\nplease try again")
                    computerguess()  
            else:
                print("you enter invalid opration\nplease enter again")
                computerguess(atempts)
    else:
        print("Invalid option....\n")
        computerguess(atempts)

def userguess(atempts):
        numberstor=guessnum(start,end)
        count=0
        while(count != atempts):
            userinput=input("enter you number : ")
            count=count+1
            if userinput.isdigit():
                if numberstor==int(userinput):
                    print("correct answer congratulation 🎉\n")
                    print(f"i guessed {numberstor}\n")
                    print("whant to play again 1 to play 0 to exit\n")
                    againoption=int(input("enter heare :"))
                    if againoption==1:
                        game()
                    else:
                        exit()       
                elif count == atempts:
                    print("you are out of chanceses.....!\n")
                    print("computer win the game 😁\n")
                    print("whant to play again 1 to play 0 to exit\n")
                    againoption=int(input("enter heare :"))
                    if againoption==1:
                        game()
                    else:
                        exit()
                elif numberstor>int(userinput):
                    print(f"Incorrect {userinput} is to small number\n")
                elif numberstor<int(userinput):
                    print(f"Incorrect {userinput} is to large number\n")
                else:
                    print("you are now redirected to main menu....\n")
                    game()
            else:
                print(f"Invalid answer pleare enter again \n")
                userguess(atempts)

def medium():
    option=UserOption()
    if int(option)==1:
        print("you will guessing number\n")
        print("you have 10 chances\n")
        atempts=5
        userguess(atempts)
    elif int(option)==2:
        print("you shude chuse a number\n")
        print("computer is guessing the number \n")
        atempts=5  
        computerguess(atempts)
            
    elif int(option)==3:
        print("you are now exited")
        exit()
    elif int(option)==0:
        game()
    else:
        print("\ninvalid option please enter again......!\n")
        medium()

def hard():
    option=UserOption()
    if int(option)==0:
        game()
    elif int(option)==1:
        print("you will guessing number\n")
        print("you have 10 chances\n")
        atempts=3
        userguess(atempts)
    elif int(option)==2:
        print("you shude chuse a number\n")
        print("computer is guessing the number \n")
        atempts=3 
        computerguess(atempts)
            
    elif int(option)==3:
        print("you are now exited")
        exit()
    else:
        print("\ninvalid option please enter again......!\n")
        hard()

def game():
    menuoption=MenuOption()
    if menuoption==1:
        easy()
    elif menuoption==2:
        medium()
    elif menuoption==3:
        hard()
    else:
        print("you are exited......")
        exit()


WellcomeMenu()

if __name__==game():
    game()