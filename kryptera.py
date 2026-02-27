# en sträng med alla bokstäver i det svenska alfabetet
nyckel = 3

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

m = "åäö"



for bokstav in m:

    # kolla om ny plats är längre än alfabetet, om det är det måste vi ta bort längden av alfabetet.   
    plats_bokstav = alfabet.index(bokstav)
    ny_plats = plats_bokstav + nyckel

    if ny_plats >= 29:

        ny_plats = ny_plats - 29

        ny_bokstav = alfabet[ny_plats]
    
        print(ny_bokstav)
        
    else:
        ny_bokstav = alfabet[ny_plats]
        
        print(ny_bokstav)      

    

 # meddelandet som ska krypteras

    #m = list(m)


    # nyckeln är antalet positioner varje bokstav ska flyttas

    # variabel för att lagra det krypterade meddelandet

    # UPPDRAG: Skriv en loop som skriver ut "ifk"
    # Tips: Använd .index() och []

