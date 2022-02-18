# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:11:32 2022

@author: jasju
"""

### Lista de Exercicios 03 - Igor  ####

## 01) Programa que pede uma nota (0 a 10) e pede outra até que 
## que o valor esteja nesse intervalo

'''while True:
    nota = int(input('Digite uma nota[0/10]: '))
    if nota <= 10:
        print('\nValor válido \n FIM!!')
        break
    else:
        print('Valor inválido!!')'''
        
## 02) Progrma que ler 5 numeros e informa soma e a média deles

'''s = 0

for n in range(0,5):
    val = float(input('Digite um valor: '))
    s+=val

print(f'Soma = {s} \nMédia = {s/5}')'''

## 03) Tabuada de qualquer número inteiro entre 1 a 10:

'''while True:
    n = int(input('Ver tabuada [1/10]: '))
    while n > 10:
        n = int(input('Ver tabuada [1/10]: '))
    for a in range(1,11):
        print(f'{n} x {a} = {n*a}\n')
    out = str(input('Dseja continuar[s/n]: ')).lower()[0]
    if out == 'n':
        print('FIM !!')
        break'''
        
## 04) receber dois números e imprimir os números do intervalo

'''l = []
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

l.append(n1)
l.append(n2)
sorted(l)

print('a sequência é:\n')

for a in range(int(l[0])+1,int(l[1])):
    print(f'{a}\n')'''
    
## 05) Ler duas notas dos alunos e emite um conceito baseado
# na média alcançada

'''while True:
    n1 = float(input('Primeira Nota: '))
    n2 = float(input('Segunda Nota: '))
    me = (n1+n2)/2
    
    print()
    print('-='*8, 'Resumo', '-='*8)
    
    if me > 9.0:
        print(f' Média = {me}\n Conceito A')
    elif me > 7.5 and me <=9.0:
        print(f' Media = {me}\n Conceito B')
    elif me > 6.0 and me <=7.5:
        print(f' Média = {me}\n Conceito C')
    elif me > 4.0 and me <=6.0:
        print(f' Média = {me}\n Conceito D')
    elif me >=0.0 and me <=4.0:
        print(f' Média = {me}\n Conceito E')
    cont = str(input('Continuar[s/n]: ')).lower()[0]
    if cont == 'n':
        break'''
        
## 06) programa que cria uma lsita que recebe nomes e imprime
## apenas os que tem menos que 5 letras 

'''nomes = []

while True:
    nm = str(input('Digite um nome: ')).split(' ')
    nomes.append(nm)
    
    cont = str(input('Continuar[s/n]: ')).lower()[0]
    if cont == 'n':
        break
print(nomes)

for a in nomes:
    for p in a:
        if len(p)<5:
            print(p)'''

## 07) Lista que recebe 20 numeros inteiros gaurdem em uma
## lsita e separe em duas outras impares e pares:

'''from random import randint
    
ns = []
imp = []
par = []


for p in range(0,20):
    n = randint(0, 100)
    ns.append(n)

for a in ns:
    if a % 2 == 0:
        par.append(a)
    else:
        imp.append(a)
        
print()
print('-='*43)
print()
print(f'Lista completa: {ns}')
print(f'Numéros pares: {par}')
print(f'Números impares: {imp}')
print()
print('-='*43)'''

## programa que guarda a temperatua médaia de cada mês do 
## ano e imprime mês e tempeturas acima da média [resolver com lista]
'''
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
         'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']
vl = []
md = 0

print('Media de Temperatura °C \n')

for a in meses:   
    temp = float(input(f'{a}: '))
    vl.append(temp)
    md+=temp

print()
print('-='*43)
print()
print(f'Meses com tempertura acima da média ( {md/12:.2f} )')
print()
for v, p in enumerate(vl):
    if p >= (md/12):
        print(f'{meses[v]} = {p}\n')
    
print('-='*43)   '''



    


        
        

