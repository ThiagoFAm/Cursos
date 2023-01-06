#Escreva um programa que leia um valor em metros e o exiba convertidos em centímetros e milímetros.

#Definimos Variável float, por que melhor se encaixa em um contexto prático onde irá se obter numéros quebrados.

metros = float(input('Digite um valor em Metros: '))

def conversao(m):
    cm   = float(m * 100)
    mili = float(m * 1000)

    #Imprimindo o resultado.
    print(f'm  = {m}\ncm = {cm}\nml = {mili}')

    return m, cm, mili

#Definindo uma variável para cada valor.
#OBS: Quando for definir variaveis respectivamente, tem que ser na ordem.
m, cm, mili = conversao(metros)

