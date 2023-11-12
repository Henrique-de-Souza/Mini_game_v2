from turtle import Turtle 
from time import sleep
from tqdm import tqdm

# Inicializar uma Turtle
t = Turtle()

# Definindo velocidade 
t.speed(1)

# função para obter a direção e com ela as condições
def obter_direcao():
   direção = str(input('Para qual direção devo me movimentar? [F/ T] ')).upper().strip()[0]
   if direção == 'F':
        print('Vamos para frente!!!')
        sleep(1)
        print()
        rotacao_turtle(t)
        print()
        distancia = obter_distancia()
        t.forward(distancia)   
        return direção
   
   if direção == 'T':
        print('Vamos para trás!!!')
        sleep(1)
        print()
        rotacao_turtle(t)
        print()
        distancia = obter_distancia()
        t.backward(distancia)
        return direção

       

def obter_distancia():
    print()
    resposta = int(input('Quantos pixels devo andar nessa direção? '))
    print(f'Deslocando {resposta} pixels')
    sleep(1)
    return resposta


def rotacao_turtle(turtle):
    rotacao = str(input('''Pressione [D] para rotacionar para direita
Pressione [E] para rotacionar para esquerda 
Pressione [N] para não rotacionar]\n\nSua opção:  ''' )).upper().strip()[0]
    
    if rotacao == 'E':
        print()
        rotacao_esquerda(turtle)

    elif rotacao == 'D':
        print()
        rotacao_direita(turtle)

    elif rotacao == 'N':
        rotacao_nula(turtle)


def rotacao_esquerda(turtle):
    print()
    graus = int(input('Quantos graus devo rotacionar para a esquerda? '))
    print(f'rotacionando {graus}° para a esquerda...')
    sleep(1)
    t.left(graus)
    

def rotacao_direita(turtle):
    print()
    graus = int(input('Quantos graus devo rotacionar para a direita?'))
    print(f'rotacionando {graus}° para a direita...')
    sleep(1)
    t.left(graus)

def rotacao_nula(turtle):
    print('usuario preferiu não rotacionar a Turtle...')
    sleep(1)
    t.left(0)
    t.right(0)


# PROGRAMA PRINCIPAL -----------------------------------------------------------------

# defidindo as direções de movimento e mediante a resposta, sua rotação. 
print('=' * 30)
print(f'{"VAMOS DESENHAR?":^30}')
print('=' * 30)
while True:
    print()
    obter_direcao()
    print()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        print('=' * 30)
        print(f'{"Até logo":^30}')
        print('=' * 30)
        break
    else:
        print('=' * 30)
        print(f'{"RECOMEÇANDO..."}')
        print('=' * 30)
        print()
        for c in tqdm(range(2)):
            print(c, end='')
            sleep(0.5)
        print()