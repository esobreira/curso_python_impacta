from prettytable import PrettyTable
from contato import Contato
from conexao import cria_database, salva_contato, busca_contatos
import requests
import json

contatos = []

def novo_contato():
    nome = input("Digite o Nome do Contato: ")
    email = input("Digite o E-mail: ")
    telefone = input("Digite o Telefone (xx-xxxx-xxxx): ")
    salva_contato(Contato(nome, email, telefone))
    #contatos.append(Contato(nome, email, telefone))

    #for contato in contatos:
        #print("Nome: {}, email: {}, Telefone: {}".format(contato.nome, contato.email, contato.telefone))
    

def lista_contatos():
    table = PrettyTable(["Id", "Nome", "Email", "Telefone"])

    for contato in busca_contatos():
        table.add_row([contato.id_contato, contato.nome, contato.email, contato.telefone])
        #print("Nome: {}, email: {}, Telefone: {}".format(contato.nome, contato.email, contato.telefone))

    print(table)

def lista_usuarios_api():
    response = requests.get("https://randomuser.me/api")
    if response.status_code == 200:
        resultado = response.json()

        contato = Contato(
            nome="{} {}".format(
                resultado['results'][0]['name']['first'],
                resultado['results'][0]['name']['last']),
            email=resultado['results'][0]['email'],
            telefone=resultado['results'][0]['phone'])
        salva_contato(contato)
    else:
        print("Erro ao obter dados.")
        return


cria_database()
#novo_contato()
lista_usuarios_api()
lista_contatos()