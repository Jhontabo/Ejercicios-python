dictionary={'0':'cero',
            '1':'uno',
            '2':'dos',
            '3':'tres',
            '4':'cuatro',
            '5':'cinco',
            '6':'seis',
            '7':'siete',
            '8':'ocho',
            '9':'nueve',
    }


# se debe recorrer el diccionario con un for para poder completar de manera correta el proceso


text = input("ingrese un numero :")

textoFinal = ''

for letra in text:
    textoFinal += dictionary[letra] + ' '


print(textoFinal)