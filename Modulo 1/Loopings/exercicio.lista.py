notas = [] # criei uma lista vazia que iria armazenar as notas recebidas

for i in range(4):
    nota = float(input(f'Informe a nota da prova {i+1}: '))
    if nota > 0:  # do aceita nota positiva
        notas.append(nota) # notas.append(nota) adiciona um elemento no final da lista
    else: # se a nota for negativa apresenta o print
        print('Valor inválido.')

print(f'Suas notas são: {notas}')  # linha opcional

media = sum(notas) / len(notas) # a funçao sun(notas) soma todas as notas da lista
# a funçao len(notas) informa o tamanho da lista nostas

if media >= 7: # se a media for maior que 7
    print(f'Suas notas foram {notas}, sua {media:.2f} e você está aprovado.')
elif 5 <= media < 7: # se a media for de 5 a 6.99
    print(f'Suas notas foram {notas}, sua {media:.2f} e você está de recuperação.')
else: # notas abaixo de 5, ou seja, de 4.99 para baixo
    print(f'Suas notas foram {notas}, sua {media:.2f} e você está reprovado.')
# {media:. 2f} formata a media para o resultado ter apenas 2 casas decimais