import sys
from datetime import date, timedelta
from termcolor import colored, cprint



def ReadFromFile():
    AllaKonton = {}

    with open("saldo.txt", "r") as filen: 
        for raden in filen:
            kontonamn = raden.split()
            AllaKonton[kontonamn[0]] = int(kontonamn[1])
    return AllaKonton

def AddTransactionToFile(transaktioner):
    with open("transaktioner.txt", "w") as myfile:
        for namn in transaktioner:
            
            for x in transaktioner[namn]:
                myfile.write(f"{x} \n")

def AddToFile(allAccounts):
    with open("saldo.txt", "w") as myfile:
        for namn in allAccounts:
            myfile.write(f"{namn} {allAccounts[namn]}\n")
allAccounts = ReadFromFile()
    
def ReadTransaktion():
    transaktioner = {}
        
    with open("transaktioner.txt", "r") as filen:
        for raden in filen:
            namnsplit = raden.split()
            namnet = namnsplit[0]
            if not namnet in transaktioner:
                transaktioner[namnet] = []
                transaktioner[namnet].append(raden)
            elif namnet in transaktioner:
                transaktioner[namnet].append(raden)

        return transaktioner
transaktioner = ReadTransaktion()

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
            if not namn in transaktioner:
                transaktioner[namn]= []
            if not namn in allAccounts:
                allAccounts[namn]=saldo
                print("Kontot skapat")
                print(allAccounts)
                AddToFile(allAccounts)
                
            else:
                print("Kontonamnet finns redan, hitta på ett nytt")
                AddToFile(allAccounts)
            
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
                    belopp = int(input("ange belopp att sätta in"))
                    if belopp > 0:
                        today = date.today()
                        allAccounts[NuvarandeKonto] = allAccounts[NuvarandeKonto] + belopp
                        transaktioner[NuvarandeKonto].append(f"{NuvarandeKonto} satte in {str(belopp)} kronor: {str(today)}")
                        AddToFile(allAccounts)
                        AddTransactionToFile(transaktioner)
                    else:
                        print("Du måste ange ett positivt nummer")
                elif action == "2":
                    belopp = int(input("ange belopp att ta ut"))
                    if belopp > 0:
                        if allAccounts[NuvarandeKonto] - belopp < 0:
                            print("Du har för lite pengar")
                        else:
                            today = date.today()
                            allAccounts[NuvarandeKonto] = allAccounts[NuvarandeKonto] - belopp
                            transaktioner[NuvarandeKonto].append(f"{NuvarandeKonto} tog ut {str(belopp)} kronor: {str(today)}")
                            AddToFile(allAccounts)
                            AddTransactionToFile(transaktioner)
                    else:
                        print("Du måste ange ett positivt nummer")
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
            AddToFile(allAccounts)
    elif action == "4":
        exit()