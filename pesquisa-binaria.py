def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

lista_numero = list()
for c in range(1,101):
    lista_numero.append(c)
print(len(lista_numero))
print(pesquisa_binaria(lista_numero, 100))