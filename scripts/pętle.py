liczby = [1, 2, 3, 4, 5]

for i in liczby:
    print(i)

for i in range(5, 10):
    print(i)

licznik = 0

while licznik < 10:
    print(licznik)
    licznik += 1

licznik2 = 0

while True:
    print(licznik2)
    licznik2 += 1
    if licznik2 >= 5:
        break
        

for x in range(20):
    if x % 2 == 0:
        continue
    print(x)