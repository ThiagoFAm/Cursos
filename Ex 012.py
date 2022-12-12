#Faça um algoritmo que leia o preço de um produto e mostre seu novo produto, com 5% de desconto.

def desconto(preco_produto):
    d = float(0.05) #Desconto em porcentagem, deixei em decimal para facilitar o calculo.
    i = float(preco_produto * d) #Calculo para adquirir 5% do produto.
    novo_valor = preco_produto - i #Equação para subtrair os 5% do preço do produto.

    return preco_produto, novo_valor #Retornamos duas variáveis. Sendo a primeiro o preço que iremos inserir como entrada
                                     #E o novo preço com o desconto já aplicado.

preco_produto = float(input('Valor do produto que irá receber desconto: ')) #Entrada.
valor_antigo, valor_novo = desconto(preco_produto) #Armazenamento dos resultados retornados, respectivamente.
print(f'Preço antigo = {valor_antigo}\nPreço novo com 5% de desconto = {valor_novo}') #Exibindo  o valor dos valores.