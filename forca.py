from random import randint

palavras = {
    'bola' : 'coisa redonda',
    'foca' : 'bicho do mar',
    'bola' : 'coisa redonda',
    'foca' : 'bicho do mar',
    'Acender' : 'iluminação',
    'Afilhado' : 'padrinho',
    'Ardiloso' : 'difícil',
   'Áspero' : 'grosso',
    'Assombração' : 'medo',
    'Asterisco' : 'multiplicar',
    'Basquete' : 'esporte',
    'Caminho' : 'direção',
    'Champanhe' : 'bebida',
    'Chiclete' : 'bala',
    'Chuveiro' : 'banho',
    'Coelho' : 'animal',
    'Contexto' :'assunto',
    'Convivência' : 'família',
    'Coração' : 'corpo',
    'Desalmado' : 'pessoa sem alma',
    'Eloquente' : 'descolado',
    'Esfirra' : 'comida',
    'Esquerdo' : 'direita',
    'Exceção' : 'menos esse',
}

lista_palavra = []
palavra = palavras.keys()
for i in palavra:
    lista_palavra.append(i)

lista_dica = []
dica = palavras.values()
for i in dica:
    lista_dica.append(i)

sorteio = randint(0, len(lista_palavra) - 1)

palavra_keys = lista_palavra[sorteio]
palavra_dica = lista_dica[sorteio]




palavra_secreta = palavra_keys


palavra_secreta = palavra_secreta.lower()

palavra_secreta_lista = []

palavra_vazia = []

def print_lado_a_lado(lista, chances):
    for i in range(0, len(lista)):
        print('{}'.format(lista[i]), end=" ")

    print(' você tem {} chances.'.format(chances))


for i in range(0, len(palavra_secreta)):
    palavra_secreta_lista.append(palavra_secreta[i])

for i in range(0, len(palavra_secreta_lista)):
    palavra_vazia.append(' ____ ')


chances = 5
print(end='\n\n\n')
print('                                             Bem vindo ao **JOGO DA FORCA**', end='\n\n')
print('Sua palavra tem {} caracteres: '.format(len(palavra_secreta_lista)))


while ' ____ ' in palavra_vazia:
    print()
    print('------------------')
    print("Digite uma letra: ")
    print('------------------', end='\n\n')


    chute = input('Resposta: ')

    chute = chute.lower()
    chute = chute.strip()
    print(end='\n\n\n')

    if chute not in palavra_secreta_lista:
        chances -=1
    if chances == 0:
        print('Você perdeu todas as suas chances')
        break
    if chances <= 3:
        print('Dica:', palavra_dica, end='\n')
    for i in range(0, len(palavra_secreta_lista)):
        if chute == palavra_secreta_lista[i]:
            palavra_vazia[i] = chute

    print_lado_a_lado(palavra_vazia, chances)



