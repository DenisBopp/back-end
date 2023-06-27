# Cadastro de clientes Web
Este projeto tem como o objetivo a criação de um cadastro de clientes de uma aplicação Web para uma loja virtual.

---
## Como executar
As bibliotecas necessárias estão listadas no arquivo 'requirements.txt', é necessário que as versões sejam
mantidas para a compatibilidade e funcionamento do sistema.

## Ambientes virtuais
Para evitar conflito entre versões de bibliotecas, é fortemente indicado que a aplicação rode em um ambiente virtual, para criar este ambiente execute o seguinte procedimento:
```
mkdir (pasta de trabalho)
cd (pasta de trabalho)
python -m venv .venv
source .venv/bin/activate (Linux)
    ou
.venv\bin\activate.bat (windows)
```

## Organização das pastas do aplicativo

```
Pasta de trabalho
├── app.py
├── database
│   └── db.sqlite3
├── log
│   └
├── logger.py
├── model
│   ├── base.py
│   ├── cliente.py
│   ├── __init__.py
│   └── __pycache__
├── __pycache__
├── README.md
├── requirements.txt
└── schemas
    ├── cliente.py
    ├── error.py
    ├── __init__.py
    └── __pycache__
```

## Execução da aplicação
Para executar a API execute o seguinte comando:
### Produção
```
(env)$ flask run --host 0.0.0.0 --port 8000
```
### Desenvolvimento
```
(env)$ flask run --host 0.0.0.0 --port 8000 --reload --debugger
```

Abra o navegador no endereço: [http://localhost:8000/#/](http://localhost:8000/#/) para acessar a documentação.
