from fastapi import APIRouter
from utils.nextcloud_service import listar_pasta

router = APIRouter()

@router.get("/{pasta}")
def listar(pasta: str = ""):
    resposta = listar_pasta(pasta)
    return {"xml": resposta}
