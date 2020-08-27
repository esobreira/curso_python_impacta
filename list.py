def main():
    #lista = [1, 2, 3, 4]
    lista = [1, 'Eberton', True, 3.14]
    #print(lista)
    for x in lista:
        print(x)

    lista.append('Rafaela')

    for x in lista:
        print(x)

    lista.pop()
    lista.remove('Eberton')
    lista.insert(2, 'Guilherme')

    for x in lista:
        print(x)

    lista.insert(0, 'Gabriele')

    for x in lista:
        print(x)

    lista.reverse()
    #lista.sort() #só pode ordenar o mesmo tipo de valor
    lista.sort(reverse=True)

main()