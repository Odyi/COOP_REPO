# front_end.py

from back_end import *  # Importerer evalueringsfunksjonen fra back_end

# Funksjon som skriver ut hovedmenyen for kalkulatoren
def printMeny():
    print("------------------- Kalkulator -------------------")
    print("| 1. Regne                                       |")
    print("| 2. Valutta                                     |")
    print("| 3. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Velg operasjon fra menyen: ")
    utfoerMenyvalg(menyvalg)

# Funksjon som tar seg av å utføre brukerens menyvalg
def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        regne()  # Kaller regnefunksjonen
    elif valgtTall == "2":
        convert_currency()
    elif valgtTall == "3":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if bekreftelse.lower() == "j":
            exit()  # Avslutter programmet
        else:
            printMeny()
    else:
        nyttForsoek = input("|| Ugyldig valg. Velg et tall 1 eller 2. Trykk for å fortsette ||")
        printMeny()

# Funksjon som utfører matematisk beregning
def regne():
    uttrykk = input("Skriv inn et uttrykk (f.eks. 5 + 6 + 7): ")
    resultat = evaluate_expression(uttrykk)  # Bruker evalueringsfunksjonen fra back_end
    print(f"Resultat: {resultat}")
    pause_og_fortsett()



# Funksjon som setter programmet på pause til brukeren trykker en tast
def pause_og_fortsett():
    input("|| Trykk en tast for å fortsette ||")
    printMeny()

# Kaller hovedfunksjonen for å vise menyen første gang når programmet starter
if __name__ == "__main__":
    printMeny()
