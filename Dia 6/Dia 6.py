#Familia 
tupla = ()
tuplaHmos = ("Kevin", "Leonel")
tuplaHmas = ("Diana", "Teresa")
TuplaFam = tuplaHmos + tuplaHmas
len(TuplaFam)
TuplaFam = list(TuplaFam)
TuplaFam.append("Ruben")
TuplaFam.append("Jaqueline")
TuplaFam = tuple(TuplaFam) 
print(TuplaFam)
print("-------")
tphermanos, tpPas = TuplaFam[:4], TuplaFam[-2:]
print(tphermanos)
print(tpPas)
