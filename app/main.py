from fastapi import FastAPI
from fastapi.responses import FileResponse
from utils.metrics import sys_metrics

app = FastAPI()


@app.get("/")
async def root():
   return {"message": "Product Service is up and running"}
 
@app.get("/health")
async def health():
  return {"status": "ok"}

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("images/icon.png")

@app.get("/metrics")
async def metrics():
  return sys_metrics()
 
 