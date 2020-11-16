#zadanie 1
def mieszanka(a_list, b_list):
    length = len(a_list)
    i = 0
    zwrot_list = []
    while i < length:
        if i+1/2 == 1:
            zwrot_list.append(a_list[i])
        else:
            zwrot_list.append(b_list[i])
    return zwrot_list

#zadanie 2
def zadanie2tekst(tekst):
    duzeLitery = tekst.upper()
    maleLitery = tekst.lower()
    zwrot = {
    "length": len(tekst),
    "letters": list(tekst.strip()),
    "big_letters": list(duzeLitery.strip()),
    "small_letter": list(maleLitery.strip())
    }
    return zwrot

#zadanie 3
def usunZTekstu(tekst, litera):
    zwrot = tekst.replace(litera, '')
    return zwrot

#zadanie 4
#zrozumialem "uwzgledniac bledne wartosci" jako kelvin/rankine ponizej 0 ?
def zamianaTemp(wartosc, typ):
    if typ == "fahrenheit":
        return wartosc * 1.8 + 32.00
    elif typ == "rankine":
        if (wartosc+273.15) * 9/5 > 0:
            return (wartosc+273.15) * 9/5
        else:
            return 0
    elif typ == "kelvin":
        if wartosc > -273.15:
            return wartosc + 273.15
        else:
            return 0
#zadanie 5
class Calculator:
    def add(self, a, b):
        return a+b
    def difference(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        return a/b

#zadanie 6
class ScienceCalculator(Calculator):
    def kwadrat(self, a):
        return a*a

#zadanie 7
def odTylu(tekst):
    zwrot = tekst[::-1]
    return zwrot
