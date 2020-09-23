numar= 6348
ultima_cifra=numar%10
penultima_cifra=(numar//10)%10
cifra_doi=((numar//10)//10)%10
cifra_unu=numar//1000
suma_cifrelor=ultima_cifra+penultima_cifra+cifra_doi+cifra_unu
citul=numar//9
rest=numar%9
rasturnatul=ultima_cifra*1000+penultima_cifra*100+cifra_doi*10+cifra_unu
print("Ultima cifra este =", ultima_cifra)
print("Penultima cifra este = ", penultima_cifra)
print("A doua cifra este =", cifra_doi)
print("Prima cifra este ", cifra_unu)
print("Citul impartirii la 9 este =", citul)
print("Restul impartirii la 9 este =", rest)
print("rasturnatul este =", rasturnatul)