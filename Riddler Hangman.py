import random

import sys

def hangman():
    
    x = random.randint(0,4)
    book = ["martha", "riddler", "enygma", "harleyquinn", "jasontodd"]
    words = book[x]
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 8
    guessmade = ''
    
    while len(words) > 0:
        main = ""
        missed = 0
        for letter in words:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_ " + ""
        
        if main == words:
            print("\n" + main)
            print("\nSo you did it. Well done. I would have expected a child to work that one out, let alone the world's greatest detective.")
            break
        print("Guess the word: ", main)
        guess = input().lower()
        
        if guess.isalpha():
            guessmade = guessmade + guess
        else:
            print("Enter a valid character Bats!")
            guess = input()
        
        if guess not in words:
            turns -= 1
            if turns == 7:
                print("7 turns left Bats, can you do it?")
                print(" ------- ")
            if turns == 6:
                print("I thought you were the worlds best detective? 6 turns left!")
                print(" ------- ")
                print("    O    ")
            if turns == 5:
                print("Does your head hurt Batman? Understandable. You're no match for me. 5 turns left.")
                print(" ------- ")
                print("    O    ")
                print("    |    ")
            if turns == 4:
                print("Do you need my help, Batman? Do you give up? 4 turns left.")
                print(" ------- ")
                print("    O    ")
                print("    |    ")
                print("   /     ")
            if turns == 3:
                print("Can you defeat a mind such as mine? 3 turn left.")
                print(" ------- ")
                print("    O    ")
                print("    |    ")
                print("   / \   ")
            if turns == 2:
                print("There's no shame in cheating, if you admit you cannot solve my challenges. 2 turns left")
                print(" ------- ")
                print("  \ O    ")
                print("    |    ")
                print("   / \   ")
            if turns == 1:
                print("It's the E-nygma show! Only 1 turn left, Bats!")
                print(" ------- ")
                print("  \ O /  ")
                print("    |    ")
                print("   / \   ")
            if turns == 0:
                print("How many Bats do it take to solve my challenge? Obviously more than one. You've let an innocent man die Dark Knight.")
                print(" ------- ")
                print("      |  ")
                print("    O-   ")
                print("   /|\   ")
                print("   / \   ")
                break
                
def riddle():
    
    turns = 3
    answer = "mirror"
    
    print("\nHit me hard and I will crack, but you'll never stop me (from) staring back. What am I?")
    guess = ""
    while guess != answer:
        guess = input().lower()
        turns -= 1
        if guess != answer:
            if turns == 2:
                print("\nGive up? No, really. Give up. You cannot solve this. That is becoming increasingly obvious. 2 tries left.")
            if turns == 1:
                print("\nOh, please. I could have answered that one when I was six years old. 1 try left.")
            if turns == 0:
                print("\nLocked out again, Batman. Oh, sorry. Yes, you failed. Again. Cant even pass the first challenge!")
                sys.exit()
        else:
            print("\nAmazing. You actually solved my riddle. I suppose a reward is due. I'm running a little game of chance that you may be interested in playing, here's your invitation.\n")
        
        


print("Well looks like we caught a bat in our net!\n\nCan the greatest detective in the world solve my challenges and save Uncle Ben?")
print("\nChallenge 1, can you solve this riddle Bats? You have 3 tries!")
riddle()
print("Challenge 2, if you cant guess the word then Spidey is going to lose a relative. You have 8 tries!\n")
hangman()
