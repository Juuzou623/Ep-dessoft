print('\033[31m'+'Isto eh vermelho'+'\033[0;0m')

print('teste pra ver se eu existo')

for i in baralho:
    if '♠' in i:
        print('{}. {}'.format(contador, i))
    elif '♥' in i:
        print('\033[31m'+'{}. {}'.format(contador, i)+'\033[0;0m')
    elif '♦' in i:
        print('{}. {}'.format(contador, i))
    else:
        print('{}. {}'.format(contador, i))
    contador +=1