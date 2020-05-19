def soma(list):
    if(len(list) == 0):
        return 0
    else:
        return list[0] + soma(list[1:])

print(soma([1,2,3,4,5]))