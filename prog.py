#!/user/bin/python

def main():
    
    print "Guess a number bewteen 1 and 100."
    randomNumber = 50
    found = False
    while not found:
        userGuess = input("Your guess: ")
        if userGuess == randomNumber:
            print "You got it!"
            found = True
        elif userGuess > randomNumber:
            print "Too big"
        else:
            print "Too small"

if _name_ == "_main_":
    main()

