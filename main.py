from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get("/hello")
async def hello():
    return Response(content="<html><body><h1>Welcome</h1></body></html>", status_code=200, media_type="text/html")