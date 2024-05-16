from diffusers import DDIMPipeline
from PIL import Image  

def generate_butterfly_image(save_path):
    pipeline = DDIMPipeline.from_pretrained('Apocalypse-19/sd-butterflies-ceyda-32')
    image = pipeline().images[0]
    image.save(save_path)
    return image
