#Escreva um programa que leia um valor em metros e o exiba convertidos em centímetros e milímetros.

def conversao(m):
    cm   = float(m * 100)
    mili = float(m * 1000)

    return m, cm, mili

#Variável float, por que melhor se encaixa em um contexto prático onde irá se obter numéros quebrados.

metros = float(input('Digite um valor em Metros: '))

#Definindo uma variável para cada valor.
#OBS: Quando for definir variaveis respectivamente, tem que ser na ordem.
m, cm, mili = conversao(metros)

#Imprimindo o resultado.
print(f'm  = {m}\ncm = {cm}\nml = {mili}')