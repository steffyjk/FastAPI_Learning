from fastapi import FastAPI

minimal_app = FastAPI()


@minimal_app.get("/")
def read_root():
    return {"message": "Hello world!"}
