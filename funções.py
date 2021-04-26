def cria_baralho():
    cartas = []
    for naipe in range(1, 5, 1):

        cartas.append('A')

        for i in range(2, 11, 1):

            cartas.append(str(i))

        cartas.append('J')
        cartas.append('Q')
        cartas.append('K')

        if naipe == 1:
            for espada in range(0, 13, 1):
                cartas[espada] += '♠'

        elif naipe == 2:
            for copas in range(13, 26, 1):
                cartas[copas] += '♥'

        elif naipe == 3:
            for ouros in range(26, 39, 1):
                cartas[ouros] += '♦'

        else:
            for paus in range(39, 52, 1):
                cartas[paus] += '♣'
    return cartas

def extrai_naipe(carta):
    if '♦' in carta:
        return '♦'
    elif '♥' in carta:
        return '♥'
    elif '♣' in carta:
        return '♣'
    else:
        return '♠'

def extrai_valor(carta):
    for i in range(2, 11, 1):
        if str(i) in carta:
            return str(i)
    if 'K' in carta:
        return 'K'
    elif 'Q' in carta:
        return 'Q'
    elif 'J' in carta:
        return 'J'
    else:
        return 'A'