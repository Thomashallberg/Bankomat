from contextlib import nullcontext
import sys
from datetime import date
from tkinter import N


from termcolor import colored, cprint
transaktioner = {}
def ReadFromFile():
    AllaKonton = {}

    with open("saldo.txt", "r") as filen:
        for raden in filen:
            kontonamn = raden.split()
            print (f"{kontonamn[0]}")
            print (f"{kontonamn[1]}")
            AllaKonton[kontonamn[0]] = int(kontonamn[1])
            transaktioner [kontonamn[0]] = []
            #print(AllaKonton)
    return AllaKonton
allAccounts = ReadFromFile()
    #"namn": ["transaktion + today"]


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
                transaktioner[namn]= []
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
                print("4. Visa transaktioner")
                print("5. Tillbaka")
                action = input("Ange val:")
                if action == "1":
                    today = date.today()
                    belopp = int(input("ange belopp att sätta in"))
                    allAccounts[NuvarandeKonto] = allAccounts[NuvarandeKonto] + belopp
                    transaktioner[NuvarandeKonto].append(f"{NuvarandeKonto} satte in {str(belopp)} kronor: {str(today)}")


                elif action == "2":
                    today = date.today()
                    belopp = int(input("ange belopp att ta ut"))
                    if allAccounts[NuvarandeKonto] - belopp < 0:
                        print("Du har för lite pengar")
                    allAccounts[NuvarandeKonto] = allAccounts[NuvarandeKonto] - belopp
                    transaktioner[NuvarandeKonto].append(f"{NuvarandeKonto} tog ut {str(belopp)} kronor: {str(today)}")
                  
                if action == "3":
                    print(f"Du har {allAccounts[NuvarandeKonto]} kronor på ditt konto")
                elif action == "4":
                    print(transaktioner[NuvarandeKonto])
                    
                if action == "5":
                    break
    elif action == "3":
        print(allAccounts)
        inmatning = input("Vilket konto vill du ta bort?")
        if inmatning in allAccounts:
            del allAccounts[inmatning]
            print(allAccounts)

    elif action == "4":
        exit()