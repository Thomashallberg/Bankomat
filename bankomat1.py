import sys

from termcolor import colored, cprint

allAccounts = {}

while True:
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Ta bort konto")
    print("4. Avsluta")
    action = input("Ange val:")
    if action == "1":
            inmatning = input("Vad ska kontot heta?")
            person = inmatning
            namn = person
            saldo = 0
            if not namn in allAccounts:
                allAccounts[namn]=saldo
                print("Kontot skapat")
                print(allAccounts)
            else:
             print("Kontonamnet finns redan, hitta på ett nytt")
    elif action == "2":
        NuvarandeKonto = input("vilket konto vill du administrera?")
        if NuvarandeKonto in allAccounts:
            while True:
                print("1. Sätt in pengar")
                print("2. Ta ut pengar")
                print("3. Visa saldo")
                print("4. Tillbaka")
                action = input("Ange val:")
                if action == "1":
                    belopp = int(input("ange belopp att sätta in"))
                    allAccounts[namn] = allAccounts[namn] + belopp
                elif action == "2":
                    belopp = int(input("ange belopp att ta ut"))
                    if allAccounts[namn] - belopp < 0:
                        print("Du har för lite pengar")
                    allAccounts[namn] = allAccounts[namn] - belopp
                if action == "3":
                    print(f"Du har {allAccounts[namn]} kronor på ditt konto")
                if action == "4":
                    break
    elif action == "3":
        print(allAccounts)
        inmatning = input("Vilket konto vill du ta bort?")
        if inmatning in allAccounts:
            del allAccounts[inmatning]
            print(allAccounts)

    elif action == "4":
        exit()