#Valgsystem


Partier = ["arbeiderpartiet", "høyre", "senterpartiet","fremskrittspartiet", "sosialistisk Venstreparti", "rødt", "venstre", "miljøpartiet de grønne", "kristelig Folkeparti"]
Stemmer = [0] * len(Partier)

print("Partier:", Partier)

svar = ""
while svar != "ferdig":
    print("Velg et parti")
    svar = input("Svar: ")
    if svar in Partier:
        plass = Partier.index(svar)
        Stemmer[plass] = Stemmer[plass] + 1
        print("Du stemte på:", svar)
        
print("Resultat:")
for i in range(len(Partier)):
    if Stemmer[i] > 0:
        print(Partier[i], "fikk", Stemmer[i], "stemmer")
