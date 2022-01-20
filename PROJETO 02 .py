# INÍCIO DO CÓDIGO.
# BASE
from random import randint
computador = randint(0,15)

# INTERATIVIDADE DO COMPUTADOR COM O USUÁRIO.

print(' ')
print('-=-' * 20)
print('Olá, Amigo!')
print('Sou seu Computador')
print('Vou pensar em um número entre 0 e 15, tente adivinhar...')
print('Será que você consegue ADIVINHAR qual foi?')
print('-=-' * 20)

# COMPUTADOR FAZ A PERGUNTA AO USUÁRIO.

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual vai ser o seu palpite?:'))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma Vez VOCÊ CONSEGUE!')
        elif jogador > computador:
            print('Menor... Tente mais uma vez VOCÊ CONSEGUE!')
print('PARABÉNS! Acertou com {} tentativas.'.format(palpites) )
print(' ')
print('-=-' * 20)
print('....===PARABÉNS, A DESCONTRAÇÃO É UMA FORMA CORRETA DE ENFRENTAR O MEDO!===...')
print('Se você chegou até aqui, você é capaz de enfrentrar seus obstáculos.')
print('-=-' * 20)
print('Fim de Jogo!')
print(' ')
print('-=-' * 20)
print('Agora vamos para próxima etapa, VOCÊ É BOM DE RACIOCÍNIO?')

print(' ')
print('-=-' * 20)
print("SEGUNDA ETAPA, chegou a hora de MATAR A CHARADA! \n")

perguntas = {

    'Questão 01': {
        'pergunta': 'Se Alice entrou 05 vezes em sua casa, quantas vezes ela saiu?',
        'respostas': {
            'a': 'Alice Saiu 05 Vezes?',
            'b': 'Alice Saiu 04 Vezes?',
            'c': 'Alice Saiu 03 Vezes?',
            'd': 'Alice Saiu 02 Vezes?',},
             'resposta_certa': 'b',
    },
    'Questão 02': {
        'pergunta': 'Quando eu tinha 8 anos, a minha irmã tinha a metade da minha idade. Agora que tenho 55 anos, com quantos anos minha irmã está?',
        'respostas': {
            'a': 'Minha irmã está com 51 anos?',
            'b': 'Minha irmã está com 53 anos?',
            'c': 'Minha irmã está com 27 anos?',
            'd': 'Minha irmã está com 56 anos?'},
             'resposta_certa': 'a',

    },
    'Questão 03': {
        'pergunta': 'Há 7 passarinhos em um galho de árvore. Um menino atira em um deles, quantos passarinhos sobraram no galho?',
        'respostas': {
            'a': 'Ficaram 06 passarinhos?',
            'b': 'O Menino atirou nos outros?',
            'c': 'O Galho Quebou?',
            'd': 'Não Ficou Nenhum, porque os outros seis fugiram assustados'},
             'resposta_certa': 'd',

    },
     'Questão 04': {
        'pergunta': 'Há um pato entre dois patos, um pato atrás de um pato e um pato na frente de outro pato. De quantos patos estamos falando?',
        'respostas': {
            'a': '2 patos.',
            'b': '3 patos.',
            'c': '4 patos.'},
             'resposta_certa': 'b',

    },
}
respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Sua resposta:')

    if resposta_user == pv['resposta_certa']:

        print('PARABÉNS ACERTOU, Você esta indo Bem!')
        respostas_certas +=1
    else:
        print('QUE PENA, Você errou, Mas não fica triste você consegue tentando novamente!')

    print()


qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} resposta.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')

print(' ')
print('Fim da SEGUNDA etapa ')
print('-=-' * 20)
print(' ')
print("CHEGOU A HORA DA TERCEIRA ETAPA,")
print('Você esta concentrado(a) e preparado(a) para responder algumas perguntas que vai edificar seu FUTURO? \n')
print(' ')
print('-=-' * 20)
