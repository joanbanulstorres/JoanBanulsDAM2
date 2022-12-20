from PIL import Image # Importamos el módulo 'Image' de la librería 'PILL'

img = Image.new('RGBA', (30,30), color = 'red')
img.putpixel((0, 0),(0, 0, 255, 255))   # pone un pixel azul en el punto (0, 0)
    
img.save('miimagen.png')
