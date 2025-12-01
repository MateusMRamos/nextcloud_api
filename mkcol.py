from fastapi import APIRouter
from utils.nextcloud_service import criar_pasta

router = APIRouter()

@router.post("/{nome_pasta}")
def mkcol(nome_pasta: str):
    sucesso = criar_pasta(nome_pasta)

    if sucesso:
        return {"status": "Pasta criada com sucesso", "pasta": nome_pasta}
    else:
        return {"erro": "Falha ao criar pasta"}
