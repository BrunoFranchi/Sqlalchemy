from sqlalchemy import create_engine, String, Integer, Column, Table, MetaData

engine = create_engine('sqlite:///meu_banco.db', echo= True)
metadata = MetaData(bind=engine)

tabela_pessoa = Table('pessoa', metadata,
                      Column('id', Integer , primary_key=True),
                      Column('nome', String(48)),
                      Column('idade', Integer))

metadata.create_all()

