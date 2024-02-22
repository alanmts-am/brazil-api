# IBGE API 

Esta ideia engloba uma forma mais direta de lidar com os dados do IBGE.

## Como rodar

O projeto utiliza Poetry para gerenciar todas as dependências. Ele deve ser instalado a depender da máquina.

Ubuntu/Debian (apt)

```Shell
apt install poetry
```

Para instalar todas as dependências

```Shell
poetry install
```

Para rodar a API localmente
```Shell
poetry run uvicorn app.main:app --host 0.0.0.0 --port {PORTA}
```

## Dados carregados pela API

- [X] Países (/paises)
- [X] Estados (/estados)
- [ ] Municípios (/municipios)

Todos os endpoints serão os mesmos a depender da sua url base

* /{base} - lista todos os dados sobre
* /{base}/{id} - lista os dados de um especiificamente
* /{base}/nomes - retorna apenas os nomes de cada um