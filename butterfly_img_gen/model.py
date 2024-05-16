from diffusers import DDIMPipeline
from PIL import Image  
import PIL

pipeline = DDIMPipeline.from_pretrained('Apocalypse-19/sd-butterflies-ceyda-32')
image = pipeline().images[0]

save_path ="client/frontend/src/assets/images/butterfly.png"
image.save(save_path)
image