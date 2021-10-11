from fastapi import FastAPI
from app.config.routes import setup_routes


app = FastAPI()
setup_routes(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}
