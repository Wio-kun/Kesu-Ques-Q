def hus():
    print("Du er i et hus og har tre dører å dra gjennom")
    print("Du er nødt å dra gjennom en var dørene for å komme deg ut")
    print()
    print("A: dør 1, B: dør 2, C: dør 3, D: ???")
    valg = input("-> ")

    if valg == "A":
        rom1()
    if valg == "B":
        rom2()
    if valg == "C":
        rom3()
    if valg == "D":
        utgang()

def rom1():
    print("Det er et hull hær. Du faller ned. Ingen ser deg igjen.")
    print()
    exit()

def rom2():
    print("Det er ingenting hær en en annen dør.")
    print()
    print("A: dra tilbake, B: du blir i rommet, C: gå gjennom den nye døra")
    valg = input("-> ")
    if valg == "A":
        print()
        print("Du drar tilbake")
        hus()
    if valg == "B":
        (print)
        print("Hva hadde du forventet?")
        rom2()
    if valg == "C":
        print()
        print("Du fortsetter gjennom døra.")
        rom3()

def rom3():
    print("Det er ingenting hær en en annen dør. Du går gjennom døra.")
    print()
    print("A: dra tilbake, B: du blir i rommet, C: gå gjennom den nye døra")
    valg = input("-> ")
    if valg == "A":
        print()
        print("Du drar tilbake")
        hus()
    if valg == "B":
        print()
        print("Hva hadde du forventet?")
        rom3()
    if valg == "C":
        print()
        print("Du fortsetter gjennom døra.")
        rom2()


def utgang():
    print("Du kom deg ut men falt gjennom hullet som var rett utenfor døra")
    hus()

hus()