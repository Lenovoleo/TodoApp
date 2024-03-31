from fastapi import FastAPI, Response 

app = FastAPI()

@app.get("/")
def root():
    return Response("sdfjlksj")
    