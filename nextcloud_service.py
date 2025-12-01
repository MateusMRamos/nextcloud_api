import requests
from config.config import NEXTCLOUD_URL, USERNAME, PASSWORD


# ================================
# 1) UPLOAD DE ARQUIVOS (PUT)
# ================================
def enviar_arquivo(nome_arquivo, conteudo):
    url = f"{NEXTCLOUD_URL}/remote.php/dav/files/{USERNAME}/{nome_arquivo}"

    resposta = requests.put(
        url,
        data=conteudo,
        auth=(USERNAME, PASSWORD)
    )

    print("STATUS CODE:", resposta.status_code)
    print("URL:", url)
    print("RESPOSTA:", resposta.text)

    return resposta.status_code in [200, 201, 204]


# ================================
# 2) DOWNLOAD DE ARQUIVO (GET)
# ================================
def baixar_arquivo(nome_arquivo):
    url = f"{NEXTCLOUD_URL}/remote.php/dav/files/{USERNAME}/{nome_arquivo}"

    resposta = requests.get(
        url,
        auth=(USERNAME, PASSWORD)
    )

    print("STATUS CODE:", resposta.status_code)
    print("URL:", url)

    if resposta.status_code == 200:
        return resposta.content  # conteúdo do arquivo

    return None


# ================================
# 3) CRIAR PASTA (MKCOL)
# ================================
def criar_pasta(nome_pasta):
    url = f"{NEXTCLOUD_URL}/remote.php/dav/files/{USERNAME}/{nome_pasta}"

    resposta = requests.request(
        "MKCOL",
        url,
        auth=(USERNAME, PASSWORD)
    )

    print("STATUS CODE:", resposta.status_code)
    print("URL:", url)
    print("RESPOSTA:", resposta.text)

    return resposta.status_code in [201, 405]
    # 201 = criada
    # 405 = já existe


# ================================
# 4) LISTAR PASTA (PROPFIND)
# ================================
def listar_pasta(pasta=""):
    url = f"{NEXTCLOUD_URL}/remote.php/dav/files/{USERNAME}/{pasta}"

    headers = {
        "Depth": "1",
        "Content-Type": "application/xml"
    }

    body = """<?xml version="1.0"?>
<d:propfind xmlns:d="DAV:">
    <d:prop>
        <d:displayname/>
        <d:resourcetype/>
        <d:getcontentlength/>
    </d:prop>
</d:propfind>
"""

    resposta = requests.request(
        "PROPFIND",
        url,
        data=body,
        headers=headers,
        auth=(USERNAME, PASSWORD)
    )

    print("STATUS CODE:", resposta.status_code)
    print("URL:", url)

    return resposta.text
