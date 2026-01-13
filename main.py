from fastapi import FastAPI
from google.cloud import firestore

from endpoints.clientes import router as clientes_router
from endpoints.leads import router as leads_router
from endpoints.ventas import router as ventas_router
from endpoints.blog import router as blog_router

app = FastAPI(
    title="Innova-OS API",
    version="0.1"
)

# Firestore
db = firestore.Client()

# Routers (IMPORTANTE: solo un prefijo)
app.include_router(leads_router, prefix="/leads", tags=["Leads"])
app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])
app.include_router(ventas_router, prefix="/ventas", tags=["Ventas"])
app.include_router(blog_router, prefix="/blog", tags=["Blog"])

@app.get("/")
def root():
    return {
        "status": "ok",
        "product": "Innova-OS",
        "message": "API viva y funcionando 🚀"
    }

@app.get("/status")
def status():
    return {
        "status": "ok",
        "product": "Innova-OS",
        "message": "API viva y funcionando 🚀"
    }

@app.get("/test-firestore")
def test_firestore():
    doc_ref = db.collection("test").document("conexion")
    doc_ref.set({
        "status": "ok",
        "message": "Firestore conectado correctamente 🚀"
    })
    return {"status": "ok", "firestore": "conectado"}
