map = 0
horse = 1
liv = 100
name = input("What do you name your Knight? -> ")
def castle():
    print("You " + name + " are a knight of honor. You have faught throug masses and youre honored by the king. At your latest venture a witch told you of a diety of great power. But to gain such power you will have to set out and betray your kingdom.")
    print()
    asking = True
    while asking == True:
        print("Do you accept? Yes:, No:")
        valg = input("-> ")
        if valg == "Yes":
            asking = False
            print()
            print("You " + name + " traverse out of the kingdom on a mission so nobody would konw of your journy. But there is another whom you will have to face.")
            witch_house()

        elif valg == "No":
            asking = False
            print()
            print("You " + name + " stay true to your kingdome. However now there is another seeking the diety any you have to stop him.")
            training_ground()
        else:
            print()
            print("You had a typo. Try again.")
            print()
def witch_house():
    map = 0
    horse = 1
    liv = 100
    print()
    print("You " + name + " meet the witch at her home and get told about the other person seeking the diety.")
    asking = True
    while asking == True:
        print("A: wait a little longer, B rush after the other person")
        valg = input("-> ")
        if valg == "A":
            asking = False
            print()
            map += 1
            print("The witch hands you a map for your journey. You " + name + " take the map and head out in a rush.")
        elif valg == "B":
            asking = False
            print()
            print("You " + name + " head after the other person")
        else:
            print()
            print("You had a typo. Try again.")
            print()
    # end while loop
    print("You " + name + " see the other person in the distance. However judging by his direction you " + name + " belive he is running the wrong way.")
    if map >= 1:
        print("You " + name + " look at your map and head the right direction.")
        print("You " + name + " get to the palace of this diety and wonder how to get in.")
        asking = True
        while asking == True:
            print("A: sit and wait, B: Look for a lever, C: Find the enterance")
            valg = input("-> ")
            if valg == "A":
                asking = False
                # end while loop
                print()
                print("No time to waste the other person is closing in.")
                asking = True
                while asking == True:
                    print("A: sit and wait, B: Look for a lever, C: Find the enterance")
                    valg = input("-> ")
                    if valg == "A":
                        asking = False
                        # end while loop
                        print()
                        print("You " + name + " got shot by a crossbow. The other person got here")
                        liv -= 100
                        if liv <=0:
                            print("Should have started looking.")
                            exit()
                    if valg == "B":
                        asking = False
                        # end while loop
                        print()
                        print("You " + name + " found a lever and pulled it. The floor sank and the sealing got sealed.")
                        tomb()
                    if valg == "C":
                        asking = False
                        # end while loop
                        print()
                        print("What did you expect. Youre not just going to find the enerance like that")
                        print("You " + name + " got shot by a crossbow. The other person got here")
                        liv -= 100
                        if liv <=0:
                            print("Should have started looking earlier.")
                            exit()

            if valg == "B":
                asking = False
                # end while loop
                print()
                print("You " + name + " found a lever and pulled it. The floor sank and the sealing got sealed.")
                tomb()

            if valg == "C":
                asking = False
                # end while loop
                print()
                print("What did you expect. Youre not just going to find the enerance like that")
                asking = True
                while asking == True:
                    print("A: sit and wait, B: Look for a lever, C: Find the enterance")
                    valg = input("-> ")
                    if valg == "A":
                        asking = False
                        # end while loop
                        print()
                        print("You " + name + " got shot by a crossbow. The other person got here")
                        liv -= 100
                        if liv <=0:
                            print("Should have started looking.")
                            exit()
                    if valg == "B":
                        asking = False
                        # end while loop
                        print()
                        print("You " + name + " found a lever and pulled it. The floor sank and the sealing got sealed.")
                        tomb()
                    if valg == "C":
                        asking = False
                        # end while loop
                        print()
                        print("What did you expect. Youre not just going to find the enerance like that")
                        print("You " + name + " got shot by a crossbow. The other person got here")
                        liv -= 100
                        if liv <=0:
                            print("Should have started looking earlier.")
                            exit()                             
    if map < 1:
        print("You " + name + " follow the peron.")
        print("You " + name + " catch up to him thanks to a faster horse.")
        print("You " + name + " kill the person but youre now lost.")
        exit()

def tomb():
    print("")

def training_ground():
    print()
    print("")

castle()