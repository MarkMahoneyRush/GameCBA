from time import sleep #Mark
while True: #Marks code
    

    print("This is the division section. Answer very carefully as you are nearly out of the calculator.") #Mark
    sleep(5) #Mark
    print("If you answer the question wrong, you will be transported to the start of the calculator") #Mark
    sleep(5) #Mark
    print("This level will be your hardest challenge yet. Choose very wisely!!") #Mark
    sleep(5) #Mark
    while True:
        choice=input("What is 90 divided by 9?") #Mark
        if choice == "10": #mark
            print("correct! You move on!") #mark
            break #mark
        else: #mark
            print("incorrect!") #mark
    
    print("here is question 2! Get ready!") #mark
    while True:#mark
        choice=input("what is 72 divided by 8?") #mark
        if choice == "9": #mark
            print("You have fooled the calculator again! you move on!") #mark
            break
        else: #mark
            print("Wrong!") #mark
        
    print("You are now on question 3! Time is ticking!") #mark
    while True: #mark
        choice=input("what is 250 divided by 5!")#mark
        if choice == "50":#mark
            print("Correct answer. You are nearly out of the calculator")#mark
            break
        else:#mark
            print("incorrect!")#mark
            
    print("You are now on question 4! Nearly there!") #mark
    while True: #mark
        choice=input("what is 99 divided by 3!")#mark
        if choice == "33":#mark
            print("Correct answer. 1 more question left and you are free!")#mark
            break
        else:#mark
            print("incorrect!")#mark
            
    print("The final question! Good luck!") #mark
    while True: #mark
        choice=input("What is 180 divided by 6!?")#mark
        if choice == "30":#mark
            print("Correct answer. You have beaten me, you will be transported out of the calculator! You have won!")#mark
            break
        else:#mark
            print("incorrect!")#mark
            
            
