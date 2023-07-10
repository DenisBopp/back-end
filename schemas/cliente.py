from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Fulano de Tal"
    cpf: str = "000.000.000-00"
    celular: str = "(00) 00000-0000"
    email: str = "fulano.tal@hotmail.com"

class ClienteAtualizaSchema(BaseModel):
    """Define com deve ser a atualização dos dados
    """
    nome: Optional [str] = ""
    cpf: str = ""
    celular: Optional [str] = ""
    email: Optional [str] = ""

class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    cpf: str = ""

class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    cpf: str = ""

class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    clientes:List[ClienteSchema]

class ClienteViewSchema(BaseModel):
    """ Define como um produto será retornado:
    """
    nome: str = "Fulano de Tal"
    cpf: str = "000.000.000-00"
    celular: str = "(00) 00000-0000"
    email: str = "fulalo.tal@hotmail.com"

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "nome": cliente.nome,
        "cpf": cliente.cpf,
        "celular": cliente.celular,
        "email": cliente.email,
    }

def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "celular": cliente.celular,
            "email": cliente.email,
        })

    return {"clientes": result}
