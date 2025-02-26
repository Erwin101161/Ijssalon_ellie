mijn_prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}
aanbieding = "3.20"
reclame_tekst = "vandaag is in de aanbieding: vanille-ijs, 1 liter - slechts euro" +" " + aanbieding + "."
reclame_tekst3 = (reclame_tekst.swapcase())
reclame_tekst4 = ["VANDAAG", "IN", "DE", "AANBIEDING", ":", "VANILLE-IJS", "1", "LITER", "-", "SLECHTS", "EURO", "3.20"]
for e1 in reclame_tekst4:
    if len (e1) >=5:
        print(e1.upper())
    else:
        print(e1.lower())



    




















