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
    print("1. Skapa konto", "")
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
                cprint("1. Sätt in pengar","green")
                cprint("2. Ta ut pengar","red")
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
                        cprint(f"{NuvarandeKonto} satte in {str(belopp)} kronor: {str(today)}","green")
                    else:
                        cprint("Du måste ange ett positivt nummer","red","on_yellow")
                elif action == "2":
                    belopp = int(input("ange belopp att ta ut"))
                    cprint(f"Du tog ut {belopp} kronor","red")
                    if belopp > 0:
                        if allAccounts[NuvarandeKonto] - belopp < 0:
                            cprint("Du har för lite pengar","red","on_yellow")
                        else:
                            today = date.today()
                            allAccounts[NuvarandeKonto] = allAccounts[NuvarandeKonto] - belopp
                            transaktioner[NuvarandeKonto].append(f"{NuvarandeKonto} tog ut {str(belopp)} kronor: {str(today)}")
                            AddToFile(allAccounts)
                            AddTransactionToFile(transaktioner)
                    else:
                        cprint("Du måste ange ett positivt nummer","red","on_yellow")
                if action == "3":
                    cprint(f"Du har {allAccounts[NuvarandeKonto]} kronor på ditt konto","green")

                elif action == "4":
                    print(transaktioner[NuvarandeKonto])
                    
                if action == "5":
                    break
                
    elif action == "3":
        print(allAccounts)
        inmatning = input("Vilket konto vill du ta bort?")
        cprint(f"tog bort{inmatning}","green")
        if inmatning in allAccounts:
            del allAccounts[inmatning]
            print(allAccounts)
            AddToFile(allAccounts)
    elif action == "4":
        exit()