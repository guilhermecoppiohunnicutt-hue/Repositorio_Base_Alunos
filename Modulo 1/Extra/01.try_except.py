# Utilizamos o try/except para apresentar uma exceção
# de uma maneira mais amigável ao usuário

try: # o código tenta executar o comando
    resultado = 10/0
except: # caso não consiga, ele apresenta qual é o erro.
    print('Ocorreu um erro na operação. Não é possível a divisão com denominador igual a zero.')