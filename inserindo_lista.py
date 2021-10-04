from testando import engine, tabela_pessoa

connect = engine.connect()
insert = tabela_pessoa.insert()

pessoal = []


while True:
    new = input('Deseja acrescentar um novo usuário?')
    if new == 'não':
        print('Final')
        break
    user_name = input('Informe o nome do novo usuário: ')
    user_age = input('Informe a idade: ')
    list = insert.values(nome= user_name, idade= user_age)
    connect.execute(list)
    pessoal.append(list)
