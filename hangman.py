import random

from sympy import Q

def hman():
    print("Welcome",name.capitalize(),"\n")
    que = random.choice(['APPLE','TIGER','SUPERMAN','IRONMAN','FOOD','HANGMAN'])
    val = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chance = 10
    g = ''
    while (len(que) > 0):
        m = ''
        for q in que:
            if (q in g):
                m = m + q 
            else:
                m = m + '_' + ' '
            
        if (m == que):
            print("WORD : ",m)
            print("You Win!! ")
            break

        print("\nGuess the word: ",m)
        gu = input("Guess: ").upper()

        if (gu in val):
            g = g + gu
        else:
            print("\nEnter valid alphabat: ")
            gu = input("Guess: ").upper()
            
        if gu not in que:
            chance = chance - 1
            if chance == 9:
                print("\n9 turns left")
                print("  --------  ")
            if chance == 8:
                print("\n8 turns left")
                print("  --------  ")
                print("     O      ")
            if chance == 7: 
                print("\n7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if chance == 6:
                print("\n6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if chance == 5:
                print("\n5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if chance == 4:
                print("\n4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if chance == 3:
                print("\n3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if chance == 2:
                print("\n2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if chance == 1:
                print("\n1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if chance == 0:
                print("\nYou loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter Your Name: ")
hman()    
