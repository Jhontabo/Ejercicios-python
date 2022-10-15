#Calculadora de IMC

def calculdora(peso,altura):
    imc=peso/(altura*altura)
    return imc


def pedirImc():

    peso=float(input('¿cual es tu peso en kilogramos?'))

    alturaMetros=int(input('¿Cual es tu altura en centimentros?'))

    altura=alturaMetros/100

    imc=calculdora(peso,altura)

    print(f'su imc es de {imc} ')
    if imc <=20:
        print("usted esta en delgadez ")
    elif imc >=20 and imc<26:
        print("usted tiene un peso normal ")
    elif imc>=26 and imc<30:
        print('Usted tiene sobrePeso')
    elif imc>30:
        print('Usted tiene sobre obesidad')
    else:
        print('Opcion no disponible')


pedirImc()