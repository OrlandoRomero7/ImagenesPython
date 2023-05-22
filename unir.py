from PIL import Image

def get_concat_v(im1, im2):
    #Crea un fondo blanco
    background = Image.new('RGBA', size=(400,400), color="black")
    #Redimensiona imagenes
    im1 = im1.resize((300,125))
    im2 = im2.resize((300,125))
    #Pega las imagenes en el fondo con las coordenadas dadas
    background.paste(im1, (50, 50))
    background.paste(im2, (50, 100+im1.height))
    return background

#Cargar imagenes a usar
im1 = Image.open('aceves.png')
im2 = Image.open('tecnm.jpg')

#Llamar a la funcion que concatena las imagenes y 
# lo que retorne se guarda como nueva imagen
get_concat_v(im1, im2).save('union.png') 
