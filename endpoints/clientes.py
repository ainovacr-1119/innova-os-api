from fastapi import APIRouter

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.get("/")
def get_clientes():
    return {"status": "ok", "data": [], "message": "Lista de clientes de prueba"}

@router.post("/")
def create_cliente(cliente: dict):
    return {"status": "ok", "data": cliente, "message": "Cliente creado de prueba"}

@router.put("/{cliente_id}")
def update_cliente(cliente_id: int, cliente: dict):
    return {"status": "ok", "data": cliente, "message": f"Cliente {cliente_id} actualizado de prueba"}

@router.delete("/{cliente_id}")
def delete_cliente(cliente_id: int):
    return {"status": "ok", "message": f"Cliente {cliente_id} eliminado de prueba"}
