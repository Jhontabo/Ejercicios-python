name=input("what it´s your name? ")

old=int(input("how many years old?"))

mayorDeEdad= old>18

respuestaHijoDueño=input("eres el hijo del dueño?")
hijoDueño=respuestaHijoDueño=='si'


dejarPasar=mayorDeEdad or hijoDueño
if dejarPasar:
     print("Bienvenido puedes ingresar")
else:
    print('Lo siento no puedes ingresar')

