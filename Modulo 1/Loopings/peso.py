# Crie um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso liquido.

# Etapas para resoluçao:
# 1) crie uma lista vazia para receber os pesos
# 2) crie um for para receber os pesos das 5 pessoas.
# 3) adicione os pesos recebidos a lista
# 4) utilize a funçao max() e min() ou ordene a lista e busque o primeiro e o ultimo elemento
# 5) apresente os resultados

pesos = []

for i in range(5):

    peso = float(input("Digite o seu peso em Kg:"))
    pesos.append(peso)
print(f'A lista dos pesos em Kg: ')

maior_peso = max(pesos)
menor_pesos = min(pesos)
print(f'O maior peso e {maior_peso} Kg e o menor peso e {menor_pesos} Kg. ')



# maior_peso = max(pesos)
# menor_peso = min(pesos)
# print(f'O maior peso é {maior_peso} Kg e o menor peso é {menor_peso} Kg.')

# outra maneira de resolver o maior e o menor
pesos.sort()
menor = pesos[0]
maior = pesos[-1]
print(f'O maior peso é {maior} Kg e o menor peso é {menor} Kg.')
