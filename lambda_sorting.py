lista = ['a', 'd', 'B', 'C']

print(sorted(lista, key = lambda s: s.upper()))
print(lista.sort())

dicionario = {'abc': 200, 'ghi': 100, 'def': 300}
print(sorted(dicionario, key = lambda x: dicionario[x]))

nomes = ['Diogo', 'Ana', 'Lucas', 'Thiago', 'Maria', 'Natália', 'Carla']

print(sorted(nomes, key = lambda s: s[-1]))

#Desafio ordenar aleatoramente a lista
from random import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(numeros, key = lambda x: random()))