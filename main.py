from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def end_point():
    return "Hello, World!"