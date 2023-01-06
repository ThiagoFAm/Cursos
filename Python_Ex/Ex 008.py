#Escreva um programa que leia um valor em metros e o exiba convertidos em centímetros e milímetros.

def conversao(m):
    cm   = float(m * 100)
    mili = float(m * 1000)

    return m, cm, mili

#Definindo uma variável para cada valor.
#OBS: Quando for definir variaveis respectivamente, tem que ser na ordem.
m, cm, mili = conversao(metros)

#Imprimindo o resultado.
print(f'm  = {m}\ncm = {cm}\nml = {mili}')