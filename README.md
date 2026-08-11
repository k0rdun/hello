# Hello

Простой FastAPI-сервер, который принимает query-параметры `name` и `message` и возвращает HTML-страницу.

## Клонирование

```bash
git clone https://github.com/k0rdun/hello.git
cd hello
```

## Установка

```bash
python -m venv .venv
source .venv/bin/activate       # Linux
source .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload --port 8080
```
