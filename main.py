from fastapi import FastAPI
from routes.mkcol import router as mkcol_router
from routes.upload import router as upload_router
from routes.download import router as download_router

app = FastAPI()

app.include_router(mkcol_router, prefix="/mkcol")
app.include_router(upload_router, prefix="/upload")
app.include_router(download_router, prefix="/download")

@app.get("/")
def root():
    return {"status": "API Nextcloud funcionando"}
