import sqlite3
from contato import Contato

def cria_database():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contatos(id integer not null primary key autoincrement, nome text not null, email text not null, telefone text)")
    print("Banco e Tabela criados com sucesso.")
    conn.close()

def salva_contato(contato):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    #lista = [(contato.nome, contato.email, contato.telefone)]

    if contato.id_contato:
        cursor.execute("UPDATE contatos SET nome = ?, telefone = ? WHERE id = ?", (contato.nome, contato.telefone, contato.id_contato))
    else:
        cursor.execute("INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)", (contato.nome, contato.email, contato.telefone))
    
    conn.commit()
    print("Gravado com sucesso!")


def busca_contatos():
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    contatos = []
    cursor.execute("SELECT id, nome, email, telefone FROM contatos")
    for linha in cursor.fetchall():
        contatos.append(
            Contato(
                id_contato=linha[0],
                nome=linha[1],
                email=linha[2],
                telefone=linha[3]
            )
        )
    conn.close()
    return contatos