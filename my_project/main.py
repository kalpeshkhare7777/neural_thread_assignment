# main.py (FastAPI)
from fastapi import FastAPI, Response
from diffusers import DDIMPipeline
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.get("/generate_butterfly")
async def generate_butterfly():
    pipeline = DDIMPipeline.from_pretrained('Apocalypse-19/sd-butterflies-ceyda-32')
    image = pipeline().images[0]

    # Convert the image to bytes
    img_byte_array = BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    # Return the image data in the response
    return Response(content=img_byte_array.getvalue(), media_type="image/png")
