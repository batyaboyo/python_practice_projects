from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = "./edited"

for file in os.listdir(path):
    img = Image.open("f{path}/{filename}")
    
    edit = img.filter(imageFilter.SHARPEN).convert("L")
    
    factor = 1.5
    enhancer = ImageEnhancer.contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')