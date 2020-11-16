from datetime import datetime

lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz \n" \
        "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później \n" \
        "zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w \n" \
        "latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z \n" \
        "zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach \n" \
        "osobistych, jak Aldus PageMaker "
liczba_liter1 = 0
liczba_liter2 = 0
imie = "Piotr"
nazwisko = "Roszkowski"
for i in lorem:
    if i == nazwisko[3]:
        liczba_liter1 = liczba_liter1 + 1
for j in lorem:
    if j == imie[2]:
        liczba_liter2 = liczba_liter2 + 1
print("W tekscie jest " + str(liczba_liter1) + " liter "+ nazwisko[3] +" oraz " + str(liczba_liter2) + " liter " + imie[2])

#pkt3
print('{:>10}'.format('prawo'))
print('{:>30}'.format('bardziej prawo'))

print('{:.5}'.format('ucinamy'))

for i in range(1001):
    if i % 100 == 0:
        print('{:4d}'.format(i))

info = {'imie': 'Piotr', 'nazwisko': 'Roszkowski'}
print('Imie: {imie}   Nazwisko: {nazwisko}'.format(**info))

print('{:%Y-%m-%d %H:%M}'.format(datetime(2020, 10, 26, 12, 9)))

#pkt4
tekst = "Jakis ciag znakow"
print(dir(tekst))
help(tekst.replace("a","b"))
print(tekst.replace("a","b"))

#pkt5
print(imie[::-1].capitalize() + " " +nazwisko[::-1].capitalize())

#pkt6
A = list(range(1,11))
B = A[len(A)//2:]
A = A[:len(A)//2]
print(A)
print(B)

#pkt7
A = A + B
A.insert(0,0)
print(A)
kopiaA = A
kopiaA.sort(reverse=1)
print(kopiaA)

#pkt8
#nwm czy to o to chodzilo, slabo zrozumialem tresc zadania
krotka = ((150000,'Adam Kowalski'),(150001,'Kamil Kowalski'))
print(krotka)

#pkt9
slownik = dict((x,y) for x,y in krotka)
print(slownik)

#pkt10
telefony = ['000111222','000111222','111222333']
test = set(telefony)
print(test)

#pkt11
print(list(range(1,11)))

#pkt12
print(list(range(100,19,-5)))

#pkt13
slownik_imionNazwisk = dict({"Piotr": "roszkowski","Kamil": "kowalski","Marek": "nowosielski"})
slownik_imionNumerow = dict({"Adam" : "000111222", "Stanislaw": "111222333", "Aneta": "222333444"})
lista_slownikow = [slownik_imionNazwisk,slownik_imionNumerow]
wiadomosc = "W slowniku pierwszym do imienia Piotr przypisane jest naziwsko: {0} natomiast slowniku drugim pan Stanislaw ma numer: {1}".format(lista_slownikow[0].get("Piotr").capitalize(),lista_slownikow[1].get("Stanislaw"))
print(wiadomosc)
