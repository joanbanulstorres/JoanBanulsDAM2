from PIL import Image

img = Image.open(r"miimagen.png")
print(img)
pixeles = img.getdata()
print(pixeles)
cadena = ""
for pixel in pixeles:
    #print(pixel)
    print(chr(pixel[0])) # pixel[0] -> nos interesa el canal R / a 'chr()' le das el número del carácter y te devuelve le carácter
    cadena = cadena + chr(pixel[0])

print(cadena)
