def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    #r, w, append, r+ leitura e escrita, 
    #rb, wb, r+b (windows binário)
    for linha in arquivo:
        print(linha)

def salvar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()


def main():
    ler_arquivo('pessoas.txt')
    salvar_arquivo('pessoas.txt', 'teste de escrita')
    ler_arquivo('pessoas.txt')


main()