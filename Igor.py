# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 07:27:30 2022

@author: jasju
"""

## Desafios Igor

#) Programa que contenham tres valoes e retorne se são múltiplos

'''print('-='*20)
print('       PROGRAMA NÚMEROS MÚLTIPLOS   ')
print('-='*20)

l= []
c=0

while True:
    
    for i in range(0,3):    
        n = int(input('Digite número: '))
        l.append(n)
    l.sort()
        
    for i in l[::-1]: 
        if c == 0:
            a = i
            c+=1
        else:    
            if a % i == 0:
                c+=1
            a=i
        
    if c == 3:
        print(f'Os números {l} são múiplos.')
    else:
        print(f'Os números {l} não são multiplos')
    
    cont = str(input('Continuar[s/n]: ')).lower()[0]
    
    if cont == 'n':
        break'''
        

            
'''print('-='*20)
print('       PROGRAMA NÚMEROS MÚLTIPLOS   ')
print('-='*20)

l= []
d = []

while True:
    
    for i in range(0,3):
        n = int(input('Digite um número: '))    
        d.append(n)
        if i == 0:
            l.append(n)
            a = n
        else:
            if n % a == 0 or a % n == 0:
                l.append(n)
        a = n
    
    if len(l) == 3:
        print(f'Os números {d} são múlplos.')
    
    else:
         print(f'Os números {d} não são múlplos.')
    
    d.clear()
    l.clear()
    cont = str(input('Deseja continuar?[s/n] ')).lower()[0]
    
    if cont == 'n':
        break'''

## 2) programa com duas variáveis, tamanho do arquivo e 
# velocidade de Download, informar tempo em minutos 


'''print('-='*20)
print('       TEMPO PARA DOWNLOAD   ')
print('-='*20)


tam = float(input('Tamanho do Arquivo [Mb]: '))
vel = float(input('Velocicade [Mbps]: '))

print('--'*20)
print()
print(f'Tempo estimado: {round((tam/vel)/60,2)} min.')'''


# Crescimento populacional - n. de anos para um pais
# se igual a outro país A 80.000 3.0% crescimento 
# 200.000 1.5% crescimento

'''print('-='*20)
print('       POPULAÇÕES EQUIVALENTES   ')
print('-='*20)

while True:
    
    popA = int(input('População A: '))
    popB = int(input('População B: '))
    
    c=0
    
    while popA < popB:
        popA+=((popA*3.0)/100)
        popB+=((popB*1.5)/100)
        c+=1
    
    print()
    print(f'Em {c} anos A e B terão populações equivalentes.')
    print()
    cont = str(input('Calcular outro?[s/n] ')).lower()[0]
    if cont == 'n':
        break'''

# programa para resumir investigação - registra cinco 
# respostas e da o status do suspeito 



invest = dict()
c=0

perg = ['Telefonou para vítima [s/n]? ', 
        'Esteve no local do crime [s/n]? ',
        'Mora perto da vítima [s/n]? ',
       'Devia para a vítima [s/n]? ',
       'Já trabalhou com a vítima [s/n]? ']


invest['Nome'] = str(input('Investigado: '))

for p in perg:
    per = str(input(f'{p}'))
    while per not in 'sn':
         per = str(input(f'{p}'))
    if per == 's':
        c+=1
invest['Pontuação'] = c

if c < 2:
    invest['Status'] = 'Inocente'
elif c == 2:
    invest['Status'] = 'Suspeito'
elif c > 2 and c <= 4:
    invest['Status'] = 'Cúmplice'
else:
    invest['Status'] = 'Culpado'

print()
print('-='*20)
print("       RESUMO DA INVESTIGAÇÃO ")
print('-='*20)

for c, v in invest.items():
   print(f'{c}: {v}') 
    
