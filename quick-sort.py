def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivo = list[0]
        menores = [i for i in list[1:] if i <= pivo ]
        maiores = [i for i in list[1:] if i > pivo ]
        return quicksort(menores) + [pivo] + quicksort(maiores)
print(quicksort([9,2,3]))