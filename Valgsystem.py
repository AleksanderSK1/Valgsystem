#Valgsystem


Partier = ["arbeiderpartiet", "høyre", "senterpartiet","fremskrittspartiet", "sosialistisk venstreparti", "rødt", "venstre", "miljøpartiet de grønne", "kristelig folkeparti"]
Stemmer = [0] * len(Partier)
print(Partier)
print("Skriv ferdig hvis du er ferdig med å stemme.")

while True:
    svar = input("Velg et parti: ")
    if svar == "ferdig":
        break
    if svar in Partier:
        Stemmer[Partier.index(svar)] += 1
    else:
        print("Du stemte på et parti som ikke eksisterer")

total = sum(Stemmer)

f = open("valgresultat.txt", "w")
for i in range(len(Partier)):
    if Stemmer[i] > 0:
        f.write(Partier[i] + " fikk " + str(Stemmer[i]) + " stemmer (" + str(round(Stemmer[i]/total*100,1)) + "%)\n")

