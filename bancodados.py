import sqlite3

conn = sqlite3.connect('galeria.db')

cursor = conn.cursor()

def criar_tabela():
    sql = "CREATE TABLE albums(titulo text, artista text, data_lcto text, dt_publ text, midia text)"
    cursor.execute(sql)
    conn.commit()

def select_dados2():
    sql = "SELECT * FROM albums"
    recordset = cursor.execute(sql)
    for rec in recordset:
        print(rec)

def select_dados():
    sql = "SELECT rowid, * FROM albums order by artista"
    cursor.execute(sql)
    for rec in cursor.fetchall():
        print(rec)

def insere_registro():
    sql = "INSERT INTO albums VALUES ('Eberton Plus', 'Eberton', '28/02/1982', '12/06/1987', 'BluRay')"
    cursor.execute(sql)    
    conn.commit()

def insere_muitos():
    albums = [
        ('Rafaela Album', 'Rafaela', '15/01/2014', '27/08/2020', 'DVD'),
        ('Guilherme Album', 'Guilherme', '02/09/2008', '27/08/2020', 'DVD')
    ]
    cursor.executemany("INSERT INTO albums VALUES (?, ?, ?, ?, ?)", albums)
    conn.commit

def atualiza_registro():
    sql = "UPDATE albums set artista = 'Qualquer Nome de Artista'"
    cursor.execute(sql)
    conn.commit()

def exclui_registro():
    sql = "DELETE FROM albums where data_lcto = '28/02/1982'"
    cursor.execute(sql)
    conn.commit()

def main():
    #criar_tabela()
    insere_registro()
    #select_dados()
    insere_muitos()
    atualiza_registro()
    select_dados()
    #exclui_registro()
    #select_dados2()


main()