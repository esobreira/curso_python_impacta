import sqlite3

class Endereco(object):

    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.ddd = None
        self.ibge = None
        self.gia = None

    def cria_tabela(self):
        conn = sqlite3.connect('enderecos.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ENDERECOS(cep text, logradouro text, complemento text, bairro text, localidade text, uf text, ddd text, ibge text, gia text)")
        conn.commit()

    def salvar(self):
        self.cria_tabela()
        conn = sqlite3.connect('enderecos.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ENDERECOS VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % 
        (self.cep, self.logradouro, self.complemento, self.bairro, self.localidade, self.uf, self.ddd, self.ibge, self.gia))
        conn.commit()