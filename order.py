import csv_management
import bebidas
import time
import random

def order():
    triple = 580
    doble = 430
    individual = 280
    ingredientes = [['ja', 'Jamón', 40], ['ch', 'Champiñón', 35], ['pi', "Pimentón", 30], ['dq', "Doble queso", 40],
                    ['ac', "Aceitunas", 57.5], ['pp', 'Pepperoni', 38.5], ['sa', 'Salchichón', 62.5]]

    nsand = 0  # número de sandwiches
    val = 1
    cuenta = 0  # total a pagar por sandwich(es)
    cuenta_total = 0 # total a pagar, sandwich(es) mas bebida(s)

    while val == 1:  # ciclo para cada sandwich
        nsand += 1
        print("Sandwich número ", nsand, "\n")
        print("Opciones:")
        valaux = 0
        ntam = ''
        cuentaindiv = 0  # valor de ese sandwich
        nombreorden = "" # nombre de la orden individual para agregar en archivo CSV
        while valaux == 0:
            tam = input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): ")
            if tam != 't' and tam != 'd' and tam != 'i':
                print("Debe seleccionar el tamaño correcto!!")
            else:
                valaux = 1
                if tam == 't':
                    print("Ha elegido el tamaño triple")
                    ntam = 'Triple'
                    cuentaindiv += triple
                elif tam == 'd':
                    print("Ha elegido el tamaño doble")
                    ntam = 'Doble'
                    cuentaindiv += doble
                elif tam == 'i':
                    print("Ha elegido el tamaño individual")
                    ntam = 'Individual'
                    cuentaindiv += individual
        print()
        print("Ingredientes:")
        print("Jamón           (ja)")
        print("Champiñones     (ch)")
        print("Pimentón        (pi)")
        print("Doble Queso     (dq)")
        print("Aceitunas       (ac)")
        print("Pepperoni       (pp)")
        print("Salchichón      (sa)")
        valin = 0
        listin = []
        while valin == 0:  # ciclo para agregar ingredientes
            ingred = input("Indique ingrediente (enter para terminar): ")
            if ingred in ['ja', 'ch', 'pi', 'dq', 'ac', 'pp', 'sa']:
                listin.append(ingred)
            elif ingred != '':
                print("Ingrediente no válido!")
            else:
                valin = 1

        if not listin:
            print("Usted seleccionó un sándwich", ntam, " con queso")
        else:
            print("Usted seleccionó un sándwich", ntam, 'con ', end='')
            i = 0
            # ciclo para imprimir nombre de los ingredientes y sumar su valor a la cuenta
            while i < len(listin):
                cont = 0
                for ingre in ingredientes:
                    if ingre[0] == listin[i]:
                        break
                    else:
                        cont += 1
                ing = ingredientes[cont]
                cuentaindiv += ing[2]
                if i == len(listin) - 1:
                    print(ing[1])
                    nombreorden += ing[1]
                else:
                    print(ing[1], ", ", end='')
                    nombreorden += ing[1] + "-"
                i += 1


        nombreorden = "Sandwich " + ntam + " con " + nombreorden
        csv_management.append_order(nombreorden, cuentaindiv)
        print()
        print("Subtotal a pagar por un sándwich ", ntam, ": ", cuentaindiv)
        cuenta += cuentaindiv
        print("*********************************")
        auxi = 0
        resp = ''
        while auxi == 0:
            resp = input("¿Desea ordenar otro sandwich [s/n]?: ")
            if resp != 's' and resp != 'n':
                print('Opción no válida')
            else:
                auxi = 1
        if resp == 'n':
            val = 0
        print()

    cuenta_total += cuenta + bebidas.ordenar_bebida() #llamada a la funcion de ordenar bebidas y agregacion a la cuenta total

    print('El pedido tiene un total de ', nsand, ' sándwich(es) por un monto de ', cuenta, '\n')
    
    print('Total a pagar: ',cuenta_total)

    print()
    print()
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('ESTAMOS SORTEANDO UN AUTOMOVIL TESLA 0km')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print()
    print('¿Desea participar? el costo del boleto es 500')
    print()
    auxi=0
    #ciclo de toma de decision de la participacion en la rifa
    while auxi == 0:
        resp = input("¿Participar [s/n]?: ")
        if resp != 's' and resp != 'n':
            print('Opción no válida')
        else:
            auxi = 1
        #si desea participar, entra por este if, sino va directo al final
        if resp == 's':
            print('Gracias por participar! ')
            cuenta_total = cuenta_total + 500
            print('Tu nuevo total a pagar: ',cuenta_total)
            sorteoToken = input("Escoge un numero del 1-100: ") #Escpge un numero el cliente para la rifa
            print('Buena eleccion!')
            time.sleep(3)
            print('Seleccionando el boleto ganador')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('...')

            print('TENEMOS EL BOLETO GANADOR!!! y es el numero...')
            time.sleep(2)
            print('...')
            time.sleep(2)

            ganador = random.randrange(1, 101)      #se selecciona un boleto al azar del 1 al 100

            print(ganador,'!!!')
            time.sleep(1)
            if ganador == sorteoToken: #if del caso ganador
                print('ERES EL GANADOR DE UN NUEVO AUTOMOVIL TESLA 0KM, FELICIDADES!!')
                time.sleep(3)
            else :                      #if del caso perdedor
                print('MALA SUERTE!!! quizas para la proxima...')
                time.sleep(3)

    print('\nGracias por su compra!, regrese pronto')
