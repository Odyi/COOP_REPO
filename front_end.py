# Funksjon som skriver ut hovedmenyen for kalkulatoren
def printMeny():
    # Skriver ut menyen til brukeren
    print("------------------- Kalkulator -------------------")
    print("| 1. Regne                                       |")
    print("| 2. Avslutt                                     |")
    print("--------------------------------------------------")
    
    # Brukeren velger et menyvalg ved å skrive inn et tall
    menyvalg = input("Velg operasjon fra menyen: ")
    
    # Kaller funksjonen for å utføre den valgte menyoperasjonen
    utfoerMenyvalg(menyvalg)


# Funksjon som tar seg av å utføre brukerens menyvalg
def utfoerMenyvalg(valgtTall):
    # Hvis brukeren velger "1", utføres regne-operasjonen
    if valgtTall == "1":
        regne()  # Dette kaller en ekstern funksjon fra "back_end" som må være definert et annet sted

    # Hvis brukeren velger "2", vil de få muligheten til å avslutte programmet
    elif valgtTall == "2":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        
        # Hvis brukeren bekrefter med "J" eller "j", avsluttes programmet
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()  # Avslutter programmet
        else:
            # Hvis brukeren ikke bekrefter avslutningen, vises menyen igjen
            printMeny()
    else:
        # Hvis brukeren skriver inn et ugyldig valg, får de beskjed om det
        nyttForsoek = input("*** Ugyldig valg. Velg et tall 1 eller 2. Trykk for å fortsette *** ")
        # Menyen vises på nytt
        printMeny()


# Funksjon som setter programmet på pause til brukeren trykker en tast
def pause_og_fortsett():
    # Pause for brukerens input for å fortsette
    input("-- Trykk en tast for å fortsette --")
    # Viser hovedmenyen igjen
    printMeny()


# Kaller hovedfunksjonen for å vise menyen første gang når programmet starter
printMeny()
