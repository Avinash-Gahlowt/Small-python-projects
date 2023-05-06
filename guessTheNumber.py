import random  
RandNum=random.randint(1,100)
userGuess=None
guesses=0
while(userGuess!=RandNum ):
    userGuess=int(input("Guess The number "))
    guesses+=1
    if( userGuess==RandNum):
        print(f"You guessed the number right! in {guesses} guesses")
    else:
        if(userGuess>RandNum):
            print("You guessed it wrong! Kindly enter a smaller Number")
        else:
            print("You guessed it wrong! Kindly enter a larger Number")
try:
    with open('hiscore.txt','r') as f:
        hiscore=int(f.read())
        if hiscore>guesses: 
            with open('hiscore.txt','w') as f:
                f.write(str(guesses))
                       
#if game is played for the very first time and hiscore.txt doesn't exist
except IOError:
    with open("hiscore.txt",'w') as f:
        f.write(str(guesses))
