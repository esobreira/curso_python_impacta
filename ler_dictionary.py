def ler_arquivo():
    arquivo = open('contatos.txt', 'r')
    dict = {}
    for linha in arquivo:
        dict = linha.split('|')
        print(dict[0])
        

ler_arquivo()