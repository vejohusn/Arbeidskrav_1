"""
Arbeidskrav 1 
USN - Python høst 2025
Beregninger med for kostnader mellom elbil og bensinbil
av Vegard H. Johansen
Versjon 5
"""

# KONSTANTER PR ÅR
EL_FORSIKRING = 5000
BENSIN_FORSIKRING = 7500
TRAFIKK_FORSIKRING = 8.38*365

# KONSTANTER PR KM
FORBRUK_EL = 2.00 * 0.2  # Forbruk pr km elbil = 2kr/kWh * 0,2kWh/km
FORBRUK_BENSIN = 1 # Forbruk pr km bensinbil = 1kr/km
BOM_EL = 0.1 # Bomavgift elbil 0,1kr/km
BOM_BENSIN = 0.3 # Bomavgift beninbil 0,3kr/km

# OPPSTARTS INFORMASJON
print("************************************************************")
print("Program som regner ut forskjellene mellomm elbil og bensinbil")
print("Skriv 'avslutt' eller Trykk Ctrl+C for å avslutte program")
print("************************************************************")

# FUNKSJON FOR Å MOTTA INNDATA (KM) FRA BRUKEREN AV PROGRAMMET
def km_inn(tekst_inn): 
    while True: #Kjøres til den brytes av return når man får gyldig verdi inn
        inndata = input(tekst_inn) # Input for hvor mange km den skal beregne 

        if(inndata.lower() == "avslutt"): #Legger inn en betingelse hvis bruker skriver avslutt istedet for km så avsluttes programmet
            exit()                        #Konverterer input til småbokstaver for å sikre hvis bruker skriver med store bokstaver eller en blading
        
        try: # Gjør sjekk på input data fra brukerern
            return float(inndata) # Returnerer verdi for beregning hvis det er et desimaltall eller et heltall i rett format.
        except ValueError:
            print("---FEIL---") # Skriver to linjer med tilbakemelding til brukeren om at han har skrevet inn feil format eller verdi.
            print("Du må skrive inn et heltall f.eks 1234 eller et desimaltall med komma f.eks 1234.6")

# FUNKSJON FOR Å REGNE PROSENT OG TEGNE EN "GRAFISK" FREMSTILLING
def prosent(el_bil, ben_bil):
    prosent = round((el_bil * 100) / ben_bil, 1) # Regner ut prosent med en desimal
    graf = int(round(prosent/10, 0)) # Lager et heltall mellom 1 og 10 som tilsvarer prosent
    print("Det er", prosent, "% billigere med El-bil") # Skriver % i tekst tilake til hovenfunksjonen
    grafstreng = "0% |" #Starter en streng som skal  bli den grafiske fremstilingen
    i = 0
    while i < 10: #Kjører en løkke som bygger sammen strengen som skal representere prosent grafisk
        if i < graf:
            grafstreng = grafstreng + "#" # SKriver # hvis heltallet fra prosent er større enn de 10 tellingene
        else:
            grafstreng = grafstreng + "-" # Skriver - hvis heltallet er mindre enn de 10 tellingene.
        i += 1
    grafstreng = grafstreng + "| 100%" #Skriver siste del av grafstrengen
    print(grafstreng) #Skriver grafstrengen til konsoll

# FUNKSJONFOR Å GJØRE UTREGNINGEN
def utregning():

    AntallKm = km_inn("Skriv inn antall km du kjører pr år: ") #Kaller funksjonen km_inn for å få en verdi til variabelen AntallKm

    AarligPrisEl =  round((FORBRUK_EL * AntallKm) + (BOM_EL * AntallKm) + EL_FORSIKRING + TRAFIKK_FORSIKRING, 2) # Utregning kostnader elbil
    AarligPrisBensin = round((FORBRUK_BENSIN * AntallKm) + (BOM_BENSIN * AntallKm) + BENSIN_FORSIKRING + TRAFIKK_FORSIKRING, 2) # Utregning kostnader bensinbil

    # Her skrives resultater tilbake til konsoll
    print(" ")
    print("Årlig pris for Elbil blir:" , str(AarligPrisEl) , "kr")
    print("Årlig pris for Bensinbil blir:" , str(AarligPrisBensin) , "kr")
    print("Elbil er" , str(round(AarligPrisBensin-AarligPrisEl, 2)) , "kr billigere enn bensinbil pr år" )
    prosent(AarligPrisEl, AarligPrisBensin)
    print("________________________________________________")

# EN WHILE LØKKE SOM KALLER UTREGNINGSFUNKSJONEN HELT TIL MAN AVSLUTTER PROGRAMMET MED Å AVSLUTTE DET MED CTRL+C
while True:
    utregning()

"""
REFERANSER:
- Forelesninger i kurset Python USN 2025
- Input fra brukeren: https://www.w3schools.com/python/python_user_input.asp 
- Konstanter og variabler: https://www.geekster.in/articles/python-variable-and-constants/
- Funksjoner: https://www.w3schools.com/python/python_functions.asp , https://www.geeksforgeeks.org/python/python-return-statement/ 
- Små og store bokstaver: https://stackoverflow.com/questions/1801668/convert-a-list-with-strings-all-to-lowercase-or-uppercase
- exit() av program: https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
- While løkke: https://www.w3schools.com/python/python_while_loops.asp
"""
