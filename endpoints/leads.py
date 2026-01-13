from fastapi import APIRouter

router = APIRouter(prefix="/leads", tags=["leads"])

@router.get("/")
def get_leads():
    return {"status": "ok", "data": [], "message": "Lista de leads de prueba"}

@router.post("/")
def create_lead(lead: dict):
    return {"status": "ok", "data": lead, "message": "Lead creado de prueba"}
