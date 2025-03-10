# Napisati rekurzivnu count funkciju. 
# Funkcija prima listu i predikat i vraća koliko elemenata u listi zadovoljava predikat. 
# Predikat je funkcija koja prima jedan element liste i vraća True / False.

def count(lista, predikat):
    if not lista:
        return 0
    if predikat(lista[-1]):
        return 1+count(lista[:-1],predikat)
    return 0+count(lista[:-1],predikat)

# Napisati rekurzivnu funkciju koja generira listu stringova 
# koji predstavljaju sve moguće kombinacija slova „A“, „B“ i „C“ neke zadane dužine.
# Dužina stringova je zadana kao parametar funkcije. 
# Funkcija će imati dodatni parametar za prosljeđivanje djelomičnih stringova.

def abc(duzina, string):
    lst=[]
    if len(string)==duzina:
        lst.append(string) 
    else:
        lst.extend(abc(duzina,string+'a'))
        lst.extend(abc(duzina,string+'b'))
        lst.extend(abc(duzina,string+'c'))
    return lst

# Napisati iterativnu funkciju koja generira listu stringova koji 
# predstavljaju sve moguće kombinacija slova „A“, „B“ i „C“ neke zadane dužine.
# Dužina stringova je zadana kao parametar funkcije. Funkcija koristi stog umjesto rekurzije
# _,_,_,_  *,*,*,*
def abc_stog(duzina):
    stack=[""]
    slova=['a','b','c']
    lista=[]
    while stack:
        str=stack.pop()
        if len(str)==duzina:
            lista.append(str)
        else:
            for slovo in slova:
                stack.append(str+slovo)

    return lista


# Napisati funkciju koja prima listu pozitivnih cijelih brojeva. 
# Funkcija ispisuje sve kombinacije brojeva u listi koju zadovoljavaju iduću jednadžbu,  „brute-force“ algoritmom: 
# (zbroj brojeva)2 % 23 = 0 
# Funkcija će imati dodatni parametar za prosljeđivanje trenutne liste brojeva u zbroju.

def rjesenja(lista, trenutna_lista):
    #print(lista,trenutna_lista )
    if not lista and trenutna_lista and pow(sum(trenutna_lista),2)%23==0:
        print("KOMB:",trenutna_lista)
    if not lista:
        return
    rjesenja(lista[:-1],trenutna_lista)
    rjesenja(lista[:-1],trenutna_lista+[lista[-1]])