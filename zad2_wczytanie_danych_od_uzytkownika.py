# zadanie
# napisz dodawanie odejmowanie mnożenie i dzielenie liczb pobranych od użytkownika
# dla chętnych: kalkulator bmi :)



#Pomoc: 
# dzisiaj nasze programy staną się interaktywne
# będziemy pobierać coś od użytkownika (my jesteśmy programistami ofc :D)
# służy do tego funcja input(tekst) gdzie tekst to dowolny ... tekst np "Podaj liczbe"
# domyślnie, używając funckji input, zostanie nam zwrócony ciąg znaków - tekst - string
# by zamienić string na liczbę należy użyć funkcji int(tekst)


zmienna_wczytana_od_uzytkownika = input("podaj jakąś liczbę ")

zmienna_zamieniona_na_liczbe = input(zmienna_wczytana_od_uzytkownika)

# np proste dodawanie może wyglądać tak:

a = input("Podaj a ")
b = input("Podaj b ")

a = int(a)
b = int(b)

print(a + b)

#powyższe jest równoznaczne z 

a = int(input("Podaj a "))
b = int(input("Podaj b "))

print(a + b)
