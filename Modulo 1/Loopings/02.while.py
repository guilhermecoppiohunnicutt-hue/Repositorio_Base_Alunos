
bombons = 10

while bombons > 0: # enquanto bombons > 0  o o while continua executando
    print(f'Eu tenho {bombons} bombons.')
    bombons -= 1  # diminui um bombom
    print(f'Comi 1 e fiquei com {bombons} bombons.') # informa a quantidade
    # de bombonsapos a subtraçao
    if bombons == 0:   # quando a quantidade de bombons for zero
        print('Acabaram os bombons.')  # informa que acabaram os bombons
