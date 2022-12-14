#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
def op(n):

    dobro  = int(n * 2)
    triplo = int(n * 3)
    raiz   = int(n ** 0.5)

    return dobro, triplo, raiz

#Definindo o número a ser usado no código.

num = int(input('Digite um número de sua escolha:'))

#Definindo uma variável para os valores retornados, os valores serão retornados como se fosse uma lista.

count = op(num)

#resultados.

print(f'dobro  = {count[0]}\ntriplo = {count[1]}\nraiz   = {count[2]}')
