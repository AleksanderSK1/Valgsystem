#Valgsystem

Partier = ["arbeiderpartiet","høyre","senterpartiet","fremskrittspartiet","sosialistisk venstreparti","rødt","venstre","miljøpartiet de grønne","kristelig folkeparti"]
Stemmer = [0] * len(Partier)

#Viser partiene du kan stemme på
def vis_partier():
    print("Disse partiene kan du stemme på:")
    print(Partier)

#Funksjon for selve stemmegivningen.
def stemmegivning():
    while True: #While løkke som kjøres frem til brukeren sier "ferdig"
        svar = input("Skriv navnet på partiet du vil stemme på (eller 'ferdig'): ")
        if svar == "ferdig":
            break
        if svar in Partier:
            plass = Partier.index(svar)
            Stemmer[plass] = Stemmer[plass] + 1
        else:
            print("Det partiet finnes ikke prøv igjen")
            
#Funksjonen som lagrer resultatene i en fil
def lagre_resultat():
    total = sum(Stemmer)
    f = open("valgresultat.txt","w")
    for i in range(len(Partier)):
        if Stemmer[i] > 0:
            f.write(Partier[i] + " fikk " + str(Stemmer[i]) + " stemmer (" + str(round(Stemmer[i]/total*100,1)) + "%)\n") #Denne gjør tallene om til prosent

vis_partier()
print("Skriv ferdig når du er ferdig med å stemme.")
stemmegivning()
lagre_resultat()
