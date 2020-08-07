list = ['Ala ', 'ma ', 'kota ', 9]

print(list[0:3])

cities = {'city': ['Kraków', 'Poznań', 'Bratysława']}

print(cities['city'][2])

suma = 1 + 2

reszta = 11 % 3

potega = 2 ** 2

zmienna = 'no hej ' * 10
print(zmienna)

print('zmienna ' + 'jest ' + 'super')

parzyste = [2, 4, 6, 8]
nieparzyste = [1, 3, 5, 7]

naturalne = parzyste + nieparzyste

print(naturalne)

print(1 != 1)

x = 5
print(x < 2)

imie = 'Tomek'
nazwisko = 'Skrzypiński'
wiek = 37

if imie in ['Tomek', 'Jan'] and wiek == 37:
    print('Cześć Tomek, masz 37 lat')
else:
    print('to nie ty')

zmienna1 = -1
zmienna2 = 2
zmienna3 = 3

if zmienna1 > 0:
    print('1')
elif zmienna2 == 2:
    print('2')
else:
    print('same falsy')