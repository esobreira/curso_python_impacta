def main():
    dict = {}
    dict['nome'] = 'Eberton'
    dict['sobrenome'] = 'Sobreira'
    dict['dt_nasc'] = '28/02/1982'
    dict['telefone'] = '11-96398-1794'

    print(dict)

    dict.pop('sobrenome')

    print(dict)

    dict.popitem()

    print(dict)

main()