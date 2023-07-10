#-----------------------------------------------------------------------------#
# Flask -> Cadastro de Clientes
# Autor -> Denis Silva
# Data  -> 2023-06-25
# Versão-> 2.0
# Descrição -> Cadastro de clientes utilizando framework Fkask com banco
#               de dados SQLite, possui as seguintes funcionalidades:
#               - Inclusão de novos clientes
#               - Atualização de dados de clientes já cadastrados
#               - Exclusão de clientes
#               - Visualização de clientes cadastrados
# V 1.0 - Versão inicial do projeto
# V 1.1 - Ajustes nas funções e troca das rotas
#-----------------------------------------------------------------------------#

# Bibliotecas utilizadas
from flask_openapi3 import OpenAPI
from flask_openapi3 import Info
from flask_openapi3 import Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from model import Session, Cliente
from logger import logger
from schemas import *
from flask_cors import CORS

# Informação do aplicativo
info = Info(title="Cadastro de Clientes Web", version="1.1.0")
app = OpenAPI(__name__, info=info)
cors = CORS(app, resources={r"/clients/*": {"origins": "*"}})

# Definição das tags informativas
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc"
)
cliente_tag = Tag(
    name="Cliente",
    description="Aplicação de controle de clientes, implementa cadastro, \
    edição e remoção de clientes da base de dados."
)

#-----------------------------------------------------------------------------#
# Rotas
# home:    '/' -> Rota para a documentação, redireciona para '/openapi'
# cliente: '/clients' [GET] -> Busca todos os clientes cadastrados
# cliente: '/clients/client' [GET] -> Busca o cliente pelo seu cpf
# cliente: '/clients/insert' [POST] -> Adiciona novo cliente
# cliente: '/clients/delete' [DELETE] -> Exclui o cliente pelo seu cpf
# cliente: '/clients/update' [POST] -> Atualiza os dados do cliente pelo seu cpf
#-----------------------------------------------------------------------------#

@app.get(
    '/',
    tags=[home_tag]
)
def home():
    """
        Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post(
    '/clients/insert',
    tags=[cliente_tag],
    responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema}
)

def add_client(form: ClienteSchema):
    """
        Adiciona um novo cliente na base de dados
        Retorna uma representação dos clientes e comentários associados.
    """
    cliente = Cliente(
        nome=form.nome,
        cpf=form.cpf,
        celular=form.celular,
        email=form.email
        )

    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")

    try:

        # criando conexão com a base
        session = Session()

        # adicionando cliente
        session.add(cliente)

        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")

        return apresenta_cliente(cliente), 200

    except IntegrityError as e:

        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente com mesmo cpf já salvo na base :/"

        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")

        return {"mesage": error_msg}, 409

    except Exception as e:

        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo cliente :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")

        return {"mesage": error_msg}, 400

# Atualiza cliente
@app.put(
    '/clients/update',
    tags=[cliente_tag],
    responses={"201": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema}
)

def update_client(form: ClienteAtualizaSchema):
    """
        Atualiza os dados do cliente na base de dados
        Retorna uma representação dos clientes e comentários associados.
    """

    logger.debug(f"Atualizando cliente cpf: '{form.cpf}' nome: '{form.nome}'")

    try:

        # criando conexão com a base
        session = Session()

        # adicionando cliente
        cliente = session.execute(select(Cliente).filter_by(cpf=form.cpf)).scalar_one()

        if(form.nome!=''):
            cliente.nome = form.nome
        if(form.celular!=''):
            cliente.celular = form.celular
        if(form.email!=''):
            cliente.email = form.email

        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Atualizadas as informações do cliente de nome: \
                     #{cliente.nome}, cpf #{cliente.cpf}")

        return apresenta_cliente(cliente), 201

    except IntegrityError as e:

        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente com mesmo cpf já salvo na base :/"

        logger.warning(f"Erro ao adicionar cliente #{form.nome}, #{error_msg}")

        return {"mesage": error_msg}, 409

    except Exception as e:

        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao atualizar cliente '{cliente.nome}', {error_msg}")

        return {"mesage": error_msg}, 400


# Busca clientes
@app.get(
    '/clients',
    tags=[cliente_tag],
    responses={"200": ListagemClientesSchema, "404": ErrorSchema}
)

def get_clients():

    """
        Faz a busca por todos os clientes cadastrados na base de dados
        Retorna uma representação da listagem de clientes.
    """
    logger.debug(f"Coletando clientes ")

    # criando conexão com a base
    session = Session()

    # fazendo a busca
    clientes = session.query(Cliente).all()

    print(clientes)

    if not clientes:

        # se não há clientes cadastrados
        return {"clientes": []}, 200

    else:

        logger.debug(f"%d clientes econtrados" % len(clientes))

        # retorna a representação de cliente
        print(clientes)

        return apresenta_clientes(clientes), 200

@app.get(
    '/clients/client',
    tags=[cliente_tag],
    responses={"200": ClienteViewSchema, "200": ListagemClientesSchema, "404": ErrorSchema}
)

def get_client(query: ClienteBuscaSchema):

    """
        Faz a busca por um cliente específico à partir do cpf informado
        Retorna uma representação dos clientes e comentários associados.
    """
    # criando conexão com a base
    session = Session()
    
    cliente_cpf = query.cpf
    logger.debug(f"Coletando dados sobre cliente #{cliente_cpf}")
    
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.cpf == cliente_cpf).first()

    if not cliente:

        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar cliente '{cliente_cpf}', {error_msg}")

        return {"mesage": error_msg}, 404

    else:

        logger.debug(f"Cliente econtrado: '{cliente.nome}'")

        # retorna a representação de cliente
        return apresenta_cliente(cliente), 200


@app.delete(
    '/clients/delete',
    tags=[cliente_tag],
    responses={"200": ClienteDelSchema, "404": ErrorSchema}
)

def delete_client(form: ClienteDelSchema):

    """
        Exclui o cliente da base de dados à partir do cpf informado
        Retorna uma mensagem de confirmação da remoção.
    """
    print(form)
    cliente_cpf = form.cpf
    # cliente_nome = query.nome

    print(cliente_cpf)

    logger.debug(f"Deletando dados sobre cliente cpf #{form.cpf}")

    # criando conexão com a base
    session = Session()

    # fazendo a remoção
    count = session.query(Cliente).filter(Cliente.cpf == cliente_cpf).delete()
    session.commit()

    if count:

        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado cliente cpf #{cliente_cpf}")

        return {"mesage": "Cliente removido", "cpf": cliente_cpf}

    else:

        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente #'{cliente_cpf}', {error_msg}")

        return {"mesage": error_msg}, 404

    # retorna a representação de cliente
    return apresenta_cliente(cliente), 200

#-----------------------------------------------------------------------------#
# Fim da rotina
#-----------------------------------------------------------------------------#
