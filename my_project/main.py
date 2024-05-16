# main.py
from fastapi import FastAPI
from diffusers import DDIMPipeline
from PIL import Image
import os

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Welcome to Butterfly Generator"}

@app.get("/generate_butterfly")
async def generate_butterfly():
    pipeline = DDIMPipeline.from_pretrained('Apocalypse-19/sd-butterflies-ceyda-32')
    image = pipeline().images[0]

    save_path = "static/butterfly.png"
    image.save(save_path)

    return {"message": "Butterfly generated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
