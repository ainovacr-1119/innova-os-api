from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])

@router.post("/")
def generar_articulo(prompt: dict):
    return {"status": "ok", "data": {"prompt": prompt}, "message": "Artículo generado de prueba"}
