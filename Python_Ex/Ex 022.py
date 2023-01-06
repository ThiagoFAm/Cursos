#Crie um programa que leia o nome de uma pessoa e mostra.
# --> O nome com todas as letras maiúsculas.
# --> O nome com todas as letras minúsculas.
# --> Quantas letras ao todo sem considerar os espaços. 
# --> Quantas letras tem o primeiro nome.

Name_0 = input(str('Nome completo: ')).strip()
Name_1 = Name_0.split()


print(f"""Seu nome Maiúsculo: {Name_0.upper()}
Seu nome Minúsculo: {Name_0.lower()}
Qtde de letras: {len(Name_0) - Name_0.count(" ")}
Qtde de letras do primeiro nome: {len(Name_1[0])}""")
