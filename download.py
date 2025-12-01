from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from utils.nextcloud_service import baixar_arquivo
from io import BytesIO

router = APIRouter()

@router.get("/{nome_arquivo}")
def download(nome_arquivo: str):
    conteudo = baixar_arquivo(nome_arquivo)

    if conteudo is None:
        return {"erro": "Arquivo não encontrado"}

    return StreamingResponse(
        BytesIO(conteudo),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={nome_arquivo}"}
    )
