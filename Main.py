jobb = 1
kniv = 0
lommelykt = 0
bil = 1
bilnøkkler = 0
barn = 1
telefon = 0
klokke = 1
sikkerhetskort = 0
sugekopper = 0
tau = 0
liv = 100

print("Det er en vanlig dag, og du er ferdig på jobb.")
print("Du er på vei ut far jobben din men du legger merke til at du mangler telefon og bilnøkkler.")
print("Du snur i døra for å hente tingene dine. Men når du prøver å åpne heisen ser du at du også mistet sikkerhetskortet ditt.")
print("Du ser et kort på pulten til medarbeieren din og tar det.")
print()
asking = True
while asking == True:
    print("A: Ta kortet til medarbeieren din, B: Finn en annen vei opp")
    valg = input("-> ")
    if valg == "A":
        asking = False
        print()
        print("Du tok kortet og er på vei opp heisen")
        sikkerhetskort += 1
        print("Du er kommet til kontoret ditt men noe rart har skjedd. Rommet er låst")
        print()
        asking = True
        while asking == True:
            print("A: Du du finner en annen vei inn til kontoret ditt, B: Du drar til sjefen din og forklarer situasjonen")
            valg = input("-> ")
            if valg == "A":
                asking = False
                print()
                if kniv >= 1:
                    print("Du låser opp døra med kniven, finner tingene dine og drar hjem")
                else:
                    print("Du finner tingene dine men fikk litt vondt i albuen og du får sparken for å knuse veggen til kontoret.")
                    bilnøkkler += 1
                    telefon += 1
                    sikkerhetskort += 1
                    jobb -= 1
                    liv -= 10
                    exit()

            elif valg == "B":
                asking = False
                print("Sjefen låser opp rommet og du får tingene dine")
                bilnøkkler += 1
                telefon += 1
                sikkerhetskort += 1
                print("Du leverer kortet du tok tilbake og drar hjem")
                sikkerhetskort -= 1
                exit()
            else:
                print("Skrivefeil. Kanskje du glemte stor bokstav. Prøv på nytt.")
                print()

    elif valg == "B":
        asking = False
        print("Du drar heller til butikken og kjøper sugekopper")
        sugekopper += 2
        print("Du begynner å klatre opp skyskraperen du jobber på men du kjenner at sugekoppene sklir")
        print()
        asking = True
        while asking == True:
            print("A: Du fortsetter, B: Du knuser vinduet og hopper inn i fjerde etasje.")
            valg = input("-> ")
            if valg == "A":
                asking = False
                print()
                print("Du faller etter å ha klatret 5 meter lengre")
                liv -= 100
                if liv < 1:
                    print("Du døde. Skulle heller tatt heisen.")
                    exit()

            elif valg == "B":
                asking = False
                print("Du lander på litt av glasset og skjærer deg. Du hoppet vist inn på kjøkkenet og har også en kniv i benet.")
                liv -= 40
                kniv += 1
                print("En medarbeier roper etter deg mens du drar opp men du er for sliten til å svare. På vei opp trappene skjedde et strømbrudd og du kan ikke se.")
                print("Mens du går opp trappa snubler du i noe. Du plukker det opp og det var en lommelykt.")
                lommelykt += 1
                print("Nå som du kan se fortsetter du opp trappa og kommer til åttende etasje hvor kontoret ditt er. Du kommer til kontoret ditt.")
                print()
                asking = True
                while asking == True:
                    print("A: Du fortsetter med dine kreative løsninger for å komme til kontoret, B: Du finner en annen vei inn, C: Du drar til sjefen din og forklarer situasjonen")
                    valg = input("-> ")
                    if valg == "A":
                        asking = False
                        print("Du drar hele veien ned trappa og ut av bygget, drar inn i butikken igjen og kjøper et tau")
                        tau += 1
                        print("Du klatrar opp bygningen igjen og går inn hullet du lagde sist. Du går opp til åttende etasje igjen og kommer deg til kontoret ditt.")
                        print("Du bruker det ene sugerøret på døra og knyter tauet fast i den og det andre sugerøret og lurer hva du skal gjøre med det andre")
                        print()
                        asking = True
                        while asking == True:
                            print("A: Du holder den andre eneden og drar vendig hardt til døra åpnes, B: Du hiver den andre sugekoppen dut et vindu og klatrer ut vinduet mens du holder fast i tauet.")
                            valg = input("-> ")
                            if valg == "A":
                                asking = False
                                print()
                                print("Du finner tingene dine men må betale for det knuste vinduet og døra.")
                                bilnøkkler += 1
                                telefon += 1
                                sikkerhetskort += 1
                                print("Du leverer kortet du tok tilbake og drar hjem")
                                sikkerhetskort -= 1
                                exit()
                            elif valg == "B":
                                asking = False
                                print("Til slutt kommer du deg ned til sugerøreret, og hører et høylytt knekk inne i bygningen. Døra ble åpnet men sugekoppen løsnet fra døra i samme sleng.")
                                print("Du faller ned skyskraperen")
                                liv -= 100
                                if liv < 1:
                                    print("Du døde. Kun katter overlever et fall fra den høyden")
                                    exit()
                                if liv >=1:
                                    print("Hvordan? Nei du får ikke avslutting")
                                    exit()
                            else:
                                print("Skrivefeil. Kanskje du glemte stor bokstav. Prøv på nytt.")
                                print()
                    elif valg == "B":
                        asking = False
                        if kniv >= 1:
                            print("Du låser opp døra med kniven, finner tingene dine og drar hjem")
                        else:
                            print("Du finner tingene dine men fikk litt vondt i albuen og du får sparken for å knuse veggen til kontoret.")
                            bilnøkkler += 1
                            telefon += 1
                            sikkerhetskort += 1
                            jobb -= 1
                            liv -= 10
                            if liv < 1:
                                print("Du døde")
                            else:
                                exit()
                    elif valg == "C":
                        asking = False
                        print("Sjefen låser opp rommet og du får tingene dine")
                        bilnøkkler += 1
                        telefon += 1
                        sikkerhetskort += 1
                        print("Du leverer kortet du tok tilbake og drar hjem")
                        sikkerhetskort -= 1
                        exit()
                    else:
                        print("Skrivefeil. Kanskje du glemte stor bokstav. Prøv på nytt.")
                        print()
    else:
        print("Skrivefeil. Kanskje du glemte stor bokstav. Prøv på nytt.")
        print()

