import funções
import random
print('Paciência Acordeão')
print('\n==================')

print('\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')

print('\nExistem apenas dois movimentos possíveis:') 

print('\n1. Empilhar uma carta sobre a carta imediatamente anterior')
print('2. Empilhar uma carta sobre a terceira carta anterior.')

print('\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')

print('\n1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe. ')

print('\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ')

print('\nO jogo inicia agora')


print('\nO estado atual do baralho é: ')
baralho = funções.cria_baralho()
random.shuffle(baralho)
contador = 1
for i in baralho:
    print('{}. {}'.format(contador, i))
    contador +=1
escolha = int(input('Digite um número entre 1 e {}: '.format(len(baralho))))

mov_possivel = funções.lista_movimentos_possiveis(baralho, escolha-1)
if mov_possivel == []:
    escolha = int(input('A carta {} não possue nenhum movimento possível. Por favor, digite outro número entre 1 e {}: '.format(baralho[escolha - 1], len(baralho))))

elif mov_possivel == [1]:
    baralho = funções.empilha(baralho, escolha-1, escolha-2)
    contador = 1
    for i in baralho:
        print('{}. {}'.format(contador, i))
        contador +=1

elif mov_possivel == [3]:
    baralho = funções.empilha(baralho, escolha-1, escolha-4)
    contador = 1
    for i in baralho:
        print('{}. {}'.format(contador, i))
        contador +=1

else:
    escolha = int(input('A carta {} possue dois movimentos possíveis. Por favor, escolha qual o seu destino, {}.({}) ou {}.({}): '.format(baralho[escolha - 1], escolha-1, baralho[escolha-2], escolha-3, baralho[escolha-4])))
