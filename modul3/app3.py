cappucino = 4
espresso = 3.5

print("""1.Capucino...4lei
2.Espresso...3.5lei""")

optiune = input('ce optiune alegi? [1,2]')

print(optiune)
if optiune == str(1) :
    bancnota = int(input('Introduceti o bancnota: [5,10]'))
    if bancnota == 5 or bancnota == 10 :
        rest = bancnota - cappucino
        print(f'Veti primit restul de {rest}')
        print('Produsul se livreaza...')
    else:
        print('Introduceti o bancnota valida[5,10]')
elif optiune == str(2) :
    bancnota = int(input('Introduceti o bancnota: [5,10]'))
    if bancnota == 5 or bancnota == 10 :
        rest = bancnota - espresso
        print(f'Veti primit restul de {rest}')
        print('Produsul se livreaza...')
else:
    print('Introduceti o optiune valida [1,2]')



