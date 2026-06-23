from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from viajei_api.schemas import Message

app = FastAPI()

@app.get('/', response_model=Message)
def read_root():
    return {"message": "Salve tropa"}

@app.get('/hello', response_class=HTMLResponse)
def hello_world():
    return """
    <html>
        <head>
            <title> Hello World! </title>
        </head>
        <body>
            <h1>Olá mundo!</h1>
        </body>
    </html>"""
