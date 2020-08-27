import requests
import json
from Endereco import Endereco

def main():
    cep = input("Digite um cep: ")
    result = requests.get("https://viacep.com.br/ws/%s/json/" %cep)

    if result.status_code == requests.codes.ok:
        j = json.loads(result.text)
        endereco = Endereco()
        endereco.cep = j['cep']
        endereco.logradouro = j['logradouro']
        endereco.complemento = j['complemento']
        endereco.bairro = j['bairro']
        endereco.localidade = j['localidade']
        endereco.uf = j['uf']
        endereco.ddd = j['ddd']
        endereco.ibge = j['ibge']
        endereco.salvar()
    else:
        print("Cep não encontrado.")

main()