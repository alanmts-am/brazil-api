# BRAZIL API 

Esta ideia engloba uma forma mais direta de lidar com os dados do IBGE.

## Como rodar

## Docker

Construa sua imagem

```Shell
docker build -t {NOME_IMAGEM} .
```

Inicie o container

```Shell
docker run -d -p {PORTA_CONTAINER}:{SUA_PORTA} {NOME_IMAGEM}
```
Por padrão, a porta é 5555

```Shell
docker run -d -p 5555:5555 {NOME_IMAGEM}
```

## Ambiente Virtual

O projeto utiliza Poetry para gerenciar todas as dependências. Utilize o pip ou outro gerenciador para baixar.

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

## Dados carregados pela API

- [X] Países (/paises)
- [X] Regiões (/regioes)
- [X] Estados (/estados)
- [X] Municípios (/municipios)

Para saber todos os endpoints da API, basta ir em "/docs" assim que ela iniciar

## Próximo Passo!!

- [ ] Novos endpoints
- [X] Parâmetro para filtrar