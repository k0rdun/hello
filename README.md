# Hello

Простой FastAPI-сервер, который принимает query-параметры `name` и `message` и возвращает HTML-страницу.

## Клонирование

```bash
git clone https://github.com/k0rdun/hello.git
cd hello
```

## Запуск через Docker

```bash
docker build -t hello .
docker run -d -p 8888:8080 --name hello hello
```

Сервер будет доступен по адресу: http://127.0.0.1:8888

## Запуск без Docker

```bash
python -m venv .venv
source .venv/bin/activate       # Linux
source .venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```
