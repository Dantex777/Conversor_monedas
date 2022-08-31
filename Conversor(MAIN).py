def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes: $" + dolares + " dólares.")

def conversor1(tipo_pesos, valor_dolar):
    dolares = input("Cuantos dolares quieres convertir a pesos " + tipo_pesos + "?." )
    dolares = int(dolares)
    pesos = dolares * valor_dolar
    pesos = str(pesos)
    print("Tienes: $" + pesos + " pesos " + tipo_pesos)


menu = """ ****************************************************************************************
        Hola, nuestro programa puede calcular tu cambio de divisa de COP, Pesos argentions o Mexicanos a dolares, o viceversa.💲🤑 🎨
            [1] COP a Dolares.
            [2] Pesos argentinos a dolares.
            [3] Pesos mexicanos a Dolares.
            [4] Dolares a COP.
            [5] Dolares a pesos argentinos.
            [6] Dolares a pesos mexicanos.
        Haz seleccionado: """

calcular= int(input(menu))

print ("        ****************************************************************************************") 


#COP a Dolares
if calcular == 1:
    conversor("colombianos", 3875)
#Argentinos a Dolares
elif calcular == 2:
    conversor("argentinos", 65)
#Mexicanos a Dolares
elif calcular == 3:
    conversor("Mexicanos", 24)
#Dolares a COP
if calcular == 4:
    conversor1("Colombianos", 3875)
#Dolares a Argentinos
elif calcular == 5:
    conversor1("argentinos", 65)
#Dolares a Mexicanos
elif calcular == 6:
    conversor1("Mexicanos", 24)
#Otro
else:
        print('Ingresa solo un numero de la lista')