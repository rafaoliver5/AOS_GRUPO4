from fastapi import FastAPI
from app.routes import recipes  

app = FastAPI(title="Recipes API")

app.include_router(recipes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

