#Valgsystem

Partier = ["arbeiderpartiet","høyre","senterpartiet","fremskrittspartiet","sosialistisk venstreparti","rødt","venstre","miljøpartiet de grønne","kristelig folkeparti"]
Stemmer = [0] * len(Partier) # Her har jeg vaglt å bruke len så jeg slipper å lage en liste som dette [0,0,0,0,0,osv]
#Viser partiene du kan stemme på
def vis_partier():
    print("Disse partiene kan du stemme på:")
    print(Partier)

#Funksjon for selve stemmegivningen.
def stemmegivning():
    while True: #While løkke som kjøres frem til brukeren sier "ferdig"
        svar = input("Skriv navnet på partiet du vil stemme på (eller 'ferdig'): ")
        if svar == "ferdig": #If løkke som sier at hvis du skriver ferdig så breaker løkken.
            break
        if svar in Partier: #If løkke som gjør at hvis du skriver et parti feil eller et parti som ikke eksisterer så printer den en beskjed.
            plass = Partier.index(svar)
            Stemmer[plass] = Stemmer[plass] + 1
        else:
            print("Det partiet finnes ikke prøv igjen")
            
#Funksjonen som lagrer resultatene i en fil
def lagre_resultat():
    total = sum(Stemmer)
    f = open("resultat.txt","w")
    for i in range(len(Partier)):
        if Stemmer[i] > 0:
            f.write(Partier[i] + " fikk " + str(Stemmer[i]) + " stemmer (" + str(round(Stemmer[i]/total*100,1)) + "%)\n") #Denne gjør tallene om til prosent

vis_partier()
print("Skriv ferdig når du er ferdig med å stemme.")
stemmegivning()
lagre_resultat()
