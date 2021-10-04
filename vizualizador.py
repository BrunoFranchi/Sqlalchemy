from sqlalchemy import select
from testando import tabela_pessoa

t = select([tabela_pessoa])

for linha in t.execute():
    print(linha)