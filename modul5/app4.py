# def alegere_nr():
#     numere = []
#     while True:
#         numar = input("Introduceti un numar (Dupa ce ati introdus 6 numere, apasati tasta Q): ")
#         if len(numere) == 6:
#             break
#         try:
#             numar = int(numar)
#         except ValueError:
#             print('Number not valid: ')
#             continue
#         if 0 < numar <= 49:
#             numere.append(numar)
#
#     return numere

import random

def genereaza_numere_Castigatoare():
   return random.sample (range(1,50),6)
# numerele = genereaza_numere_Castigatoare()
# list = [genereaza_numere_Castigatoare()]
print(genereaza_numere_Castigatoare())
print(type(genereaza_numere_Castigatoare()))


