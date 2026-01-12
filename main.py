from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "product": "Innova-OS",
        "message": "API viva y funcionando 🚀"
<<<<<<< HEAD
    }
    }
>>>>>>> 767f92e4f6e8c95cd86e5284b231d4bbf01eff38
