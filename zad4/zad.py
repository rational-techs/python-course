# Misja na dziś:
# napisać 4 programy: dodawanie, odejmowanie, dzielenie i mnożenie
# każdy z nich należy zapisać (bez polskich znaków): dodawanie.py, odejmowanie.py, dzielenie.py, mnozenie.py
# poniżej napiszę program do dodawania, na jego bazie zróbcie resztę
# następnie prześlijcie sobie kod na wzajem i uruchomcie go, próbując popsuć np. zamiast liczby wpisać tekst :)

# powodzenia hackerzy :)

def dodawanie(a, b):
    wynik = a + b
    return wynik


liczba1 = int(input("podaj pierwszą liczbę "))
liczba2 = int(input("podaj drugą liczbę "))

wynik = dodawanie(liczba1, liczba2)

print('wynik to: ', wynik)

input() # ważne, bez tej linii, czarne okienko się zamknie 