from fastapi import APIRouter, File, UploadFile
from utils.nextcloud_service import enviar_arquivo

router = APIRouter()

@router.post("/")
async def upload_arquivo(file: UploadFile = File(...)):
    conteudo = await file.read()
    sucesso = enviar_arquivo(file.filename, conteudo)

    if sucesso:
        return {"mensagem": "Upload concluído!"}
    else:
        return {"mensagem": "Erro no upload."}
