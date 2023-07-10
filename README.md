# Cadastro de clientes Web
Este projeto tem como o objetivo a criação de um cadastro de clientes de uma aplicação Web para uma loja virtual.

## Ambientes virtuais
Para evitar conflito entre versões de bibliotecas, é fortemente indicado que a aplicação rode em um ambiente virtual, para criar este ambiente execute o seguinte comando:
```
sh install.sh PASTA_DE_TRABALHO
```
Onde PASTA_DE_TRABALHO é o diretório onde vai rodar a aplicação. Este comando vai criar o ambiente virutal e instalar as bibliotecas necessárias.

## Organização do arquivos e pastas do aplicativo
O seguintes arquivos e pastas fazem parte do projeto:
```
Pasta de trabalho
├── app.py
├── run.sh
├── install.sh
├── README.md
├── requirements.txt
├── logger.py
├── database
│   └── database_web.db
├── log
│   └── (arquivos de log)
├── model
│   ├── base.py
│   ├── cliente.py
│   └── __init__.py
└── schemas
    ├── cliente.py
    ├── error.py
    └── __init__.py
    
```
## Como executar
As bibliotecas necessárias estão listadas no arquivo 'requirements.txt', é necessário que as versões sejam
mantidas para a compatibilidade e funcionamento do sistema.
Para executar o projeto, execute o seguinte comando no console:

### Produção
```
sh run.sh
```
### Desenvolvimento
```
sh run.sh dev
```
Abra o navegador no endereço: [http://localhost:8000/#/](http://localhost:8000/#/) para acessar a documentação.
