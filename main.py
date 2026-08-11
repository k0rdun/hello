from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/", response_class=HTMLResponse)
def root(name: str = "", message: str = ""):
    return f"<h1>Hello {name}! {message}!</h1>"
