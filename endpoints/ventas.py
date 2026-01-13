from fastapi import APIRouter

router = APIRouter(prefix="/ventas", tags=["ventas"])

@router.get("/")
def get_ventas():
    return {"status": "ok", "data": [], "message": "Lista de ventas de prueba"}

@router.post("/")
def create_venta(venta: dict):
    return {"status": "ok", "data": venta, "message": "Venta creada de prueba"}
