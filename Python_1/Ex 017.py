#Faça um programa que leia o comprimeto do cateto oposto e do cateto adjacente da hipotenusa de um triaângulo retângulo, calculo e mostre o comprimeto da hipotenusa.

import math #módulo matemático.

def pitagoras(cat1, cat2): #Função.

    cat_adjacente = float(math.pow(cat1, 2)) #pow, potência.
    cat_oposto = float(math.pow(cat2, 2)) #pow, potência.

    cat_soma = float(cat_oposto + cat_adjacente) #soma dos catetos.

    hip = math.sqrt(cat_soma) #Raiz quadrada da soma dos catetos.

    return cat1, cat2, hip #Retorno dos valores.

cat1 = float(input('Cateto Oposto: ')) #Entrada flutuante
cat2 = float(input('Cateto Adjacente: ')) #Entrada flutuante

teorema_pitagoras = pitagoras(cat1, cat2) #Armazenando os retornos em suas respectivas variáveis.

print(f'Temos um trinâgulo retângulo com\nCateto Adjacente = {cat1}\nCateto Oposto = {cat2}\nTem como hipotenusa o seguinte resultado: {teorema_pitagoras[2]}')
