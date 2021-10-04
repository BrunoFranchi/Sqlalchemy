from testando import engine, tabela_pessoa

connect = engine.connect()
insert = tabela_pessoa.insert()

pessoa = insert.values(nome='Bruno Rogerio', idade=31)
pessoa1 = insert.values(nome='Davi Franchi', idade=6)
pessoa2 = insert.values(nome='Vanessa Santos', idade=30)

connect.execute(pessoa)
connect.execute(pessoa1)
connect.execute(pessoa2)



