# en sträng med alla bokstäver i det svenska alfabetet
alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
alfabet == list(alfabet)

# meddelandet som ska krypteras
meddelande = ["hej"]
m = list(meddelande)


# nyckeln är antalet positioner varje bokstav ska flyttas
nyckel = 1
# variabel för att lagra det krypterade meddelandet
resultat = ""

# UPPDRAG: Skriv en loop som skriver ut "ifk"
# Tips: Använd .index() och []

bokstav = "h"

le = alfabet.index(bokstav)

ny_bokstav = le + nyckel

print(alfabet[ny_bokstav])

meddelande-1 == meddelande





