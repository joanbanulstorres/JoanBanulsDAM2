from PIL import Image

img = Image.new('RGBA', (30,30), color = 'black')

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
x = 0
y = 0
for letra in texto:
    print(letra)
    # Va poniendo en una imagen pixeles con distintas tonalidades de rojo, las cuales dependen del código ASCI de la letra
    img.putpixel((x,y),(ord(letra), 0, 0, 255))
    x = x + 1
    if x == 30:
        x = 0
        y = y + 1

img.save('miimagen.png')
