map = 0
liv = 100
name = input("What do you name your Knight? -> ")
def castle():
    print("You " + name + " are a knight of honor. You have faught through masses and youre honored by the king. At your latest venture a witch told you of a deity of great power. But to gain such power you will have to set out and betray your kingdom.")
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
            print("You " + name + " stay true to your kingdom. However now there is another seeking the deity any you have to stop him.")
            training_ground()
        else:
            print()
            print("You " + name + " had a typo. Try again.")
            print()
def witch_house():
    map = 0
    liv = 100
    print()
    print("You " + name + " meet the witch at her home and get told about the other person seeking the deity.")
    asking = True
    while asking == True:
        print("A: Wait a little longer, B: Rush after the other person")
        valg = input("-> ")
        if valg == "A":
            asking = False
            print()
            map += 1
            print("The witch hands you " + name + " a map for your journey. You " + name + " take the map and head out in a rush.")
        elif valg == "B":
            asking = False
            print()
            print("You " + name + " head after the other person")
        else:
            print()
            print("You " + name + " had a typo. Try again.")
            print()
    # end while loop
    print("You " + name + " see the other person in the distance. However judging by his direction you " + name + " belive he is running the wrong way.")
    if map >= 1:
        print("You " + name + " look at your map and head the right direction.")
        print("You " + name + " get to the palace of this deity and wonder how to get in.")
        asking = True
        while asking == True:
            print("A: Sit and wait, B: Look for a lever, C: Find the entrance")
            valg = input("-> ")
            if valg == "A":
                asking = False
                # end while loop
                print()
                print("No time to waste the other person is closing in.")
                asking = True
                while asking == True:
                    print("A: Sit and wait, B: Look for a lever, C: Find the entrance")
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
                    elif valg == "B":
                        asking = False
                        # end while loop
                        print()
                        print("You " + name + " found a lever and pulled it. The floor sank and the ceiling got sealed.")
                        tomb()
                    elif valg == "C":
                        asking = False
                        # end while loop
                        print()
                        print("What did you expect. Youre not just going to find the entrance like that")
                        print("You " + name + " got shot by a crossbow. The other person got here")
                        liv -= 100
                        if liv <=0:
                            print("Should have started looking earlier.")
                            exit()
                    else:
                        print("You " + name + " had a typo. Try again.")

            elif valg == "B":
                asking = False
                # end while loop
                print()
                print("You " + name + " found a lever and pulled it. The floor sank and the ceiling got sealed.")
                tomb()

            elif valg == "C":
                asking = False
                # end while loop
                print()
                print("What did you expect. Youre not just going to find the entrance like that")
                asking = True
                while asking == True:
                    print("A: Sit and wait, B: Look for a lever, C: Find the entrance")
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
                    elif valg == "B":
                        asking = False
                        # end while loop
                        print()
                        print("You " + name + " found a lever and pulled it. The floor sank and the ceiling got sealed.")
                        tomb()
                    elif valg == "C":
                        asking = False
                        # end while loop
                        print()
                        print("What did you expect. Youre not just going to find the entrance like that")
                        print("You " + name + " got shot by a crossbow. The other person got here")
                        liv -= 100
                        if liv <=0:
                            print("Should have started looking earlier.")
                            exit()
                    else:
                        print("You " + name + " had a typo. Try again.")
            else:
                print("You " + name + " had a typo. Try again.")                             
    if map < 1:
        print("You " + name + " follow the person.")
        print("You " + name + " catch up to him thanks to a faster horse.")
        print("You " + name + " kill the person but youre now lost.")
        exit()

def tomb():
    liv = 100
    print("You " + name + " have entered the tomb.")
    print("You " + name + " start looking for the deity.")
    print()
    print("A: Keep looking, B: Leave due to boredom.")
    asking = True
    while asking == True:
        valg = input("-> ")
        if valg == "A":
            asking = False
            # end while loop
            print()
            print("After a while you " + name + " find the entrance to the deitys locker and open up.")
            print("The deity offers you " + name + " power if you " + name + " destroy the kingdom whom captured him.")
            print("The deity expains the kingdom whom captured him is your kingdom.")
            print("Do you still wish to follow the deity?")
            print()
            print("A: Yes B: No")
            asking = True
            while  asking == True:
                valg = input("-> ")
                if valg == "A":
                    asking = False
                    # end while loop
                    print()
                    print("You " + name + " have gotten the power of the deity and your kingdom fell to ruin. After reporting your success to the deity. You " + name + " realize he is free and he kills you " + name + ".")
                    liv -= 100
                    exit()

                elif valg == "B":
                    asking = False
                    # end while loop
                    print()
                    print("The deity ate you " + name + ".")
                    liv -= 100
                    exit()
                else:
                    print("You " + name + " had a typo. Try again.")

        elif valg == "B":
            print()
            print("Are you stupid")
            print("NO!")
            print("You have gotten this far.")
            print("Naw. Go back.")
            print("A: Keep looking, B: Leave due to boredom.")
        else: 
            print("You " + name + " had a typo. Try again.")
        
        
def training_ground():
    liv = 100
    print()
    print("You " + name + " start training and wonder if you should give 100 percent or 200 percent.")
    print("A: 100, B: 200")
    asking = True
    while asking == True:
        valg = input("-> ")
        if valg == "A":
            asking = False
            # end while loop
            print()
            print("You "+ name + " give 100 percent and start getting ready for the war. The guy has gotten the deity's power by now and is heading for the kingdom.")
            print("He arrived to the kingdom and is wageing war. You step out in the front lines and attack him. Your attack was successful, he was hurt mut he immediately struck back and it resulted in your demise.")
            liv -= 100
            exit()
        elif valg == "B":
            asking = False
            # end while loop
            print()
            print("You "+ name + " give 200 percent and start getting ready for the war. You " + name + " put in an extra effort and beat all the other knights, and even gain special powers to fight with.")
            print("The guy has gotten the deity's power by now and is heading for the kingdom. He arrived and started wageing war to the kingdom.")
            print("You " + name + " step out in the front lines and attack him. Your attack was successful, he was immensely hurt and couldn't strike back. You " + name + " don't give him any time to react and strike again. He falls to the groud of the dragon.")
            print("Your duel finally starts, now he is prepared. You brutally fight and he gets hevaly dammaged by your magic attacks, it seems your magic counters his dark magic. In the end you lose your leg and whine in pain but he had your sword through his skull")
            liv -= 40
            print("After getting special treatment from the medical bay you " + name + " feel ready to go for the deity to finish this.")
            liv += 20
            print("A: You go after the deity, B: You stay put")
            asking = True
            while asking == True:
                valg = input("-> ")
                if valg == "A":
                    asking = False
                    # end while loop
                    print()
                    tomb_war()
                if valg == "B":
                    asking = False
                    # end while loop
                    print()
                    print("The deity storms the kingdom and you are unable to fend it off.")
                    liv -= 100
                    exit()
def tomb_war():
    print("You " + name + " head for the tomb, using the map given by the king. You get there and destroy the floor to spare time. Down in the tomb you " + name + " look for the deity and finally stumble upon it.")
    print("A: You Refuse, B: You Accept")
    asking = True
    while asking == True:
        valg = input("-> ")
        if valg == "A":
            asking = False
            # end while loop
            print()
            print("The deity is way out of your leauge and you begin to lose.")
            print()
            print("A: You push through, B: You use plot armor")
            asking = True
            while asking == True:
                valg = input("-> ")
                if valg == "A":
                    asking = False
                    # end while loop
                    print()
                    print("Even thoug you " + name + " push for victory, it seems so far away. Thats when you" + name + " realize you " + name + " whould instead redo the seal your kind had done many years ago.")
                    print("You " + name + " start casting your magic in the musical way your king did. The deity falls to his knees and you leave to tell of the news.")
                    print("The king makes you his knight and after a few years you " + name + " start teaching the new recruits of the secret magic hiden away.")
                    print("You became a great leader and won!")
                    exit()
                if valg == "B":
                    print()
                    print("Did you honestly think i would let you pick this after all the other dumb answers, just try again, the other one is really good. Might need your reading glasses thoug, it's pretty long.")
                    print("A: You push through, B: You use plot armor")
        if valg == "B":
            asking = False
            # end while loop
            print("You " + name + " accept the deity's offer, and once you got power you " + name + " kill the deity to save the kingdom and rule on your own.")
            print("You start your tyrannic rule where no one is to oppose, and the usage of magic is prohibited. Magic usage leeds to execution.")
            print("You won! You powerhungry being.")
            exit()

castle()