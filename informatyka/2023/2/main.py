# def binarny(n):
#     b = 1
#     poprzedniBit = n % 2
#     while n > 0:
#         aktualnyBit = n % 2

#         if poprzedniBit != aktualnyBit:
#             b += 1
#         n //= 2
#         poprzedniBit = aktualnyBit
#     return b
    

# n = int(input())
# wynik = binarny(n)
# print(f"Wynik: {wynik}")

# licznik = 0
# with open('bin.txt', 'r') as plik:
#     for linia in plik:
#         linia = linia.strip()
#         intLinia = int(linia, 2)
#         if binarny(intLinia) <= 2:
#             licznik += 1
# print(licznik)

# maxLiczba = 0
# with open('bin_przyklad.txt', 'r') as plik:
#     for linia in plik:
#         linia = linia.strip()
#         intLinia = int(linia)
#         if intLinia > maxLiczba:
#             maxLiczba = intLinia

# print(maxLiczba)

# def zamien_na_binarny(n):
#     if n == 0:
#         return "0"
    
#     tekst = []
#     while n > 0:
#         tekst.append(str(n % 2))
#         n //= 2

#     tekst.reverse()
#     wynik = ''.join(tekst)
#     return wynik
# wynik = zamien_na_binarny(67)
# print(wynik)

with open('bin.txt', 'r') as plik:
    for linia in plik:
        linia = linia.strip()
        p = int(linia, 2)
        
        p_podzielone = p // 2
        wynikXOR = p ^ p_podzielone
        
        cyfry = []
        while wynikXOR > 0:
            cyfry.append(str(wynikXOR % 2))
            wynikXOR //= 2
        cyfry.reverse()
        wynik = ''.join(cyfry)

        print(wynik)
