from fastapi import FastAPI

app = FastAPI()
# Run the server with: fastapi dev main.py

@app.get("/")
def read_root():
    return {"Hello": "World"}