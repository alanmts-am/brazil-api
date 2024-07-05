FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y 
RUN pip install poetry

COPY . /app

RUN poetry lock --no-update && poetry install --no-root --no-interaction --no-ansi

EXPOSE 5555

CMD [ "poetry","run","uvicorn","app.main:app","--host","0.0.0.0","--port","5555" ]
