
def encriptar(text):
    textFinal= ''
    for letra in text:
        ascii= ord(letra)
        ascii += 1
        textFinal += chr(ascii)
    return textFinal


def desencriptar(text):
    textFinal = ''
    for letra in text:
        ascii = ord(letra)
        ascii -= 1
        textFinal += chr(ascii)
    return textFinal


def encriptarArchivo(rutaArchivo):
    archivo =open(rutaArchivo,'r')
#el paramentro " a " sirve para agregar texto y el " w " para remplazar el contenido
    texto=archivo.read()
    archivo.close()
    textoEncriptado=encriptar(texto)


    archivo=open(rutaArchivo,'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se encripto")

def desencriptarArchivo(rutaArchivo):
    archivo =open(rutaArchivo,'r')
#el paramentro " a " sirve para agregar texto y el " w " para remplazar el contenido
    texto=archivo.read()
    archivo.close()
    textoDesencriptado=desencriptar(texto)


    archivo=open(rutaArchivo,'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se desencripto")

respuestaUsuario=input('presione e para encriptar y d para desencriptar :')

rutaArchivo=input(f'ingrese la ruta del archivo :')

if respuestaUsuario=='e':
    encriptar(rutaArchivo)
else:
    desencriptar(rutaArchivo)