#Faça um algoritmo que leia o salário de um funcionário e meostre seu novo salário, com 15% de aumento.

def promocao(salario):
    p = float(0.15) #porcentagem da promoção. Foi posta em decimal para facilitar o calculo.

    promo = float(salario + (salario * p)) #Equação da nova folha de pagamento

    return promo #Retornando o valor do novo salário do funcionário.

novo_salario = promocao(salario) #Definindo o retorno como 'novo_salario'
print(f'O funcionário recebeu uma promoção de 15%, resultante em R${novo_salario}') #Exibição.
