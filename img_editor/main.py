from PIL import Image, ImageEnhance, ImageFilter

import os

path = "./imgs"
pathOut = "./edited"

for file in os.listdir(path):
    img = Image.open(f"{path}/{file}")
    
    edit = img.filter(ImageFilter.SHARPEN).convert("L")
    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(file)[0]
    
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')