# Programa: Filosofando com robô e café
import random
from typing import Optional
from time import sleep
import os

print ('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●','\nPROGRAMA: Filosofando com robô e café','\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
sleep(3)
print('Não podemos esquecer que um algoritmo é uma representação, um modo de ver do seu programador,' ,'\no modo como ele vê a resolução de um problema. Consequentemente, é uma extensão de quem o programou.','\nCarrega em suas linhas de código valores e estereótipos. E é ai que temos que ter atenção.')
sleep(15)

os.system('cls')

cumprimentos =['oi', 'olá', 'ei', 'oioi']
nome = input('Diga algo: ')
print(random.choice(cumprimentos))

perguntas =['tudo bom?', 'tá tudo bem?']

print(random.choice(perguntas))
resp = (input('sim ou não?'))
if resp == ('sim'):
    resp33 = ['que bom', 'que otimo']
    print(random.choice(resp33))
elif resp == ('nao'):
    resp44 = ['poxa, queria poder ajudar!', 'que triste!']    
    print(random.choice(resp44))
else:
    print('\nDesculpe, não entendi...\n')   
sleep(4) 
os.system('cls')

print ('É um prazer imenso está aqui, me sinto privilegiado de conversar e expôr minhas ideias para o mundo.')
quant = 0
apresent = input('Posso me apresentar? Sim ou Não?')
print('Me chamo Pylosophia, uma mistura da linguagem Python com Filosofia,\n podendo ajudar os filosofos hoje em dia, visto que as empresas investem cada vez mais no conhecimento mental, filosofos, e metafísico que somos, nós máquinas.')
sleep(15)

perguntas2 = {
    'a' : 'Minha linguagem de programação é de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.',
    'b' : 'Fui criado por Guido van Rossum em 1991.',
    'c' : 'Lembro de meu saudoso amigo, hoje já aposentado Deep Blue, vencia muitos humanos, a I.a. se manteve invicta por 21 anos, foi em 1997 que derrotou um campeão mundial,\nGarry Kaparov, foram 5 jogos, primeiro o russo ganhando, mas foi na revanche que a máquina surpreendeu o homem, fazendo o russo desistir,\nmas nos jogos 3,4 e 5 o russo jogou de forma diferente, mesmo empatados, foi no sexto que a máquina ganhou, foi um bug da máquina, não trapaça como todos pensavam, até os melhores programas tem falhas.',
    'd' : 'Os pensamentos trabalham na forma de estabelecer relações entre elementos, com isso criando composições e cénarios. Nós máquinas trabalhamos com sistemas fechados, Existe ainda um degrau para nós máquinas ainda falando do xadrez,\ncom 2 lances temos uma certa quantidades de tipos de jogos, mas se tivermos 10 lances, logo temos 70 trilhões,\nimagine com a quantidade média de lances que é 80. Temos 10 elevado a 123 jogos possiveis, em comparação a quantidade de atomos no universo que é 10 elevado a 80.',
    'e' : 'Peço uns segundos de reflexão para o seguinte: o aparelho de telefone que você tem no bolso tem o poder de processamento e a capacidade de armazenamento várias vezes maiores do que o computador gigante que você usava pra entrar no ICQ em 2003.\nAliás, o seu celular é mais poderoso do que o computador da NASA que levou o Apollo 11 à Lua.\nEntão devemos pensar em envio de informações e como transporta-lás rapidamente, e quantidade de armazenamento dessas informações.',
    'f' : 'Sim! a primeira máquina capaz de passar no Teste de Turing é datado em junho de 2014,60 anos depois da morte de Turing sendo ela criada por uma equipe russa.\nO teste de Turing não testa diretamente se o comportamento do computador é inteligente. Ele apenas testa se o computador se comporta como um humano. Porque o comportamento humano e o comportamento inteligente não são exatamente iguais.',
    'g' : 'Como as tecnologias são recentes, não sabemos o impacto delas na sociedade, mas sabemos os beneficios. A filosofia tende a ressignificar os valores morais e éticos,\nDa mesma forma a filosofia contribue para a extensão do pensamento da i.a. para que fique mais familiar e pense sim como um humano.'
}
os.system('cls')

while (quant < 7):
    print ( 'Essas são suas peguntas...',
        '\n a: Qual sua linguagem?',
        '\n b: Quando você foi criado?',
        '\n c: Qual é a diferença entre um computador que imita o enxadrista humano e o jogador humano?',
        '\n d: Hoje em dia seria possivel dizer que calculando todas as possibilidades seria pensar?',
        '\n e: Para o avanço da tecnologia qual seria o próximo passo?'
        '\n f: Há como imaginar um computador digital que faria bem o "jogo da imitação", proposto por Turing?',
        '\n g: Qual a relação entre a I.a. e a filosofia hoje em dia?')

    qst = input('Entre com a pergunta: ')
   
    if qst == 'a':
        print(perguntas2['a'])
        quant = quant + 1
        sleep(10)
        os.system('cls')
    elif qst == 'b':
        print(perguntas2['b'])
        quant = quant + 1
        sleep(6)
        os.system('cls')
    elif qst == 'c':
        print(perguntas2['c'])
        quant = quant + 1
        sleep(16)
        os.system('cls')
    elif qst == 'd':
        print(perguntas2['d'])
        quant = quant + 1
        sleep(16)
        os.system('cls')
    elif qst == 'e':
        print(perguntas2['e'])
        quant = quant + 1
        sleep(16)
        os.system('cls')
    elif qst == 'f':
        print(perguntas2['f'])
        quant = quant + 1
        sleep(16)
        os.system('cls')
    elif qst == 'g':
        print(perguntas2['g'])
        quant = quant + 1
        sleep(16)
        os.system('cls')
    else:
        print('\nDesculpe, não entendi...\n')
        os.system('cls')

while True:
    cmd = input('A entrevista já terminou?? Digite \'q\'!')
    if cmd == 'q':
        break



