from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime
from typing import Union
from model import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    nome = Column(String(50), unique=False, nullable=False)
    cpf = Column(String(50), primary_key=True, unique=True, nullable=False)
    celular = Column(String(100), unique=False, nullable=False)
    email = Column(String(50), unique=False, nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self,
                 nome:str,
                 cpf:str,
                 email:str,
                 celular:str,
                 data_insercao:Union[DateTime, None] = None):

        """
        Inclui um novo Cliente

        Argumentos:
            nome: nome do cliente.
            cpf: cadastro de pessoa jurídica do cliente
            email: email de contato do cliente
            celular: telefone celular do cliente
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.email = email

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
