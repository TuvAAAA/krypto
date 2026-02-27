nyckel = 3

ordlista = ["hej", "att", "kul"]

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

val = input("vill du inkryptera(1) eller vill du bruteforcea ett ord(2)")


if val == "1":

    m = input("vad vill du inkyptera?")


    for bokstav in m:

        plats_bokstav = alfabet.index(bokstav)
        ny_plats = plats_bokstav + nyckel

        if ny_plats >= 29:

            ny_plats = ny_plats - 29

            ny_bokstav = alfabet[ny_plats]
    
            print(ny_bokstav)
        
        else:
            ny_bokstav = alfabet[ny_plats]
            print(ny_bokstav)    

elif val == "2":

    krypterat = input("vad vill du brutforcea?")

    for nyckel in range(0, len(alfabet)):
        dekrypterat = ""
        for b in krypterat:
            dekrypterat += alfabet[alfabet.index(b) - nyckel % 29]
        print(dekrypterat)
        
        if dekrypterat in ordlista:
            print("nyckeln är", nyckel)