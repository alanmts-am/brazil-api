# BRAZIL API 

![Brazil flag GIF](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3N1NHRwZDZ1b2k2MnNqdWhwNDB4NHJ3MXQwcGdqbHZvMGp0MGNjciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bIqdxoOVJ2oak/giphy.gif)

[PT-BR](docs/README-PT-BR.md)

 This idea encompasses a more direct way of dealing with data from Brazil.

## How to Run

### Docker

Build your image

```Shell
docker build -t {IMAGE_NAME} .
```
Run container

```Shell
docker run -d -p {CONTAINER_PORT}:{YOUR_PORT} {IMAGE_NAME}
```

By default, the port is 5555

```Shell
docker run -d -p 5555:5555 {NOME_IMAGEM}
```

### Directly

The project uses Poetry to manage all dependencies. Use pip or other manager to download.

```Shell
pip install poetry
```

To install all dependencies

```Shell
poetry install
```

To run the API locally
```Shell
poetry run uvicorn app.main:app --host 0.0.0.0 --port {PORTA}
```

## Data Loaded by the API

- [X] Countries
- [X] Regions
- [X] States
- [X] Cities
  
To get all endpoints and what they returns, go to endpoint "/docs" when it starts

## Next Step!!

- [ ] New endpoints
- [X] Parameter to filter