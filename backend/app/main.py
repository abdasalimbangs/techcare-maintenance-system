from fastapi import FastAPI


app = FastAPI(

    title="TechCare Mini API",
    description="API REST de la plateforme TechCare Mini",
    version="1.0.0"

)

@app.get("/")
def acceuil():
    return {
        "message": "Bienvenue sur l'API TechCare Mini",
        "statut": "operationnel"
    }