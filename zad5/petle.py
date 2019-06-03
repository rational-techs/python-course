# jak działam?
# dzisiaj nietypowe zajecia
# nie będę tłumaczyć jak działają poniższe pętle
# wy do tego dojdziecie :)



#Przykład:
print('zaczynam')
for i in range(0,100):
    print(i)

suma = 0
for i in range(0,10):
    suma = suma + i
    print(suma)

def add(x, y):
    wynik = x + y
    return wynik

# zakres "i" od 1 do 10 <1,10> lub <1,11)
for i in range(1, 11):

# zakres "j" od 1 do 10 <1,10> lub <1,11)
    for j in range(1,11):
        add(i, j)

####### koniec przykładu

# Zadania:

# 1. Napisać funkcje dodawanie, odejmowanie, mnożenie, dzielenie
# a następnie za pomocą pętli w pętli (patrz wyżej)
# wywołać te funkcje i zrobić działanie w stylu tabliczki mnożenia, dzielenia dodawania i odejmowania

# 2. Wyżej napisany program udoskonalić tak, by zakresy podawał użytkownik:

# start = int(input('podaj start '))
# stop = int(input('podaj stop '))
# for j in range(start, stop):
