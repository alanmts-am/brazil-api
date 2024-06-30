# BRAZIL API 

Esta ideia engloba uma forma mais direta de lidar com os dados do IBGE.

## Como rodar

O projeto utiliza Poetry para gerenciar todas as dependências. Ele deve ser instalado a depender da máquina.

Ubuntu/Debian

```Shell
pip install poetry
```

Para instalar todas as dependências

```Shell
poetry install
```

Para rodar a API localmente
```Shell
poetry run uvicorn app.main:app --host 0.0.0.0 --port {PORTA}
```
## Ambiente virtual

Para um melhor funcionamento do projeto em sua máquina, é interessante que seja startado em um ambiente virtual. Nesse caso, pode-se usar virtualenv do Python

```Shell
pip install virtualenv
```
Depois basta indicar a basta da env para o python modules

```Shell
python3 -m venv {NOME_PASTA}
```

Para entrar no ambiente, basta chamar o binário

```Shell
source {NOME_PASTA}/bin/activate
```

Estando no ambiente, para sair basta chamar o binário

```Shell
deactivate
```

## Dados carregados pela API

- [X] Países (/paises)
- [X] Estados (/estados)
- [X] Regiões (/regioes)
- [X] Municípios (/municipios)

Todos os endpoints serão os mesmos a depender da sua url base

* /{base} - lista todos os dados sobre
* /{base}/{id} - lista os dados de um especificamente
* /{base}/nomes - retorna apenas os nomes de cada um