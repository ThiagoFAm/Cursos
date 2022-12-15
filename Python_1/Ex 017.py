#Faça um programa que leia o comprimeto do cateto oposto e do cateto adjacente da hipotenusa de um triaângulo retângulo, calculo e mostre o comprimeto da hipotenusa.

import math

def pitagoras(cat1, cat2):

    cat_adjacente = float(math.pow(cat1, 2))
    cat_oposto = float(math.pow(cat2, 2))

    cat_soma = float(cat_oposto + cat_adjacente)

    hip = math.sqrt(cat_soma)

    return cat1, cat2, hip

cat1 = float(input('Cateto Oposto: '))
cat2 = float(input('Cateto Adjacente: '))

teorema_pitagoras = pitagoras(cat1, cat2)

print(f'Temos um trinâgulo retângulo com\nCateto Adjacente = {cat1}\nCateto Oposto = {cat2}\nTem como hipotenusa o seguinte resultado: {teorema_pitagoras[2]}')
