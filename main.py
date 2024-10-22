from fastapi import FastAPI
import models,router
from database import engine


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get('/')

async def home():
    return "welcome home"

app.include_router(router.router,prefix="/book",tags=["book"])