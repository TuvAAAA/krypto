alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
krypterat= "lin"
ordlista = ["hej", "men", "att"]

for nyckel in range(0, len(alfabet)):
    dekrypterat = ""
    for b in krypterat:
        dekrypterat += alfabet[alfabet.index(b) - nyckel % 29]
    print(dekrypterat)
    if dekrypterat in ordlista:
        print(nyckel)
