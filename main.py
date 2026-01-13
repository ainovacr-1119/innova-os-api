from fastapi import FastAPI
from endpoints.clientes import router as clientes_router
from endpoints.leads import router as leads_router
from endpoints.ventas import router as ventas_router
from endpoints.blog import router as blog_router

app = FastAPI(title="Innova-OS API", version="0.1")

# Routers
app.include_router(clientes_router)
app.include_router(leads_router)
app.include_router(ventas_router)
app.include_router(blog_router)

@app.get("/status")
def status():
    return {"status": "ok", "product": "Innova-OS", "message": "API viva y funcionando 🚀"}
