import csv_management

def order():
    triple = 580
    doble = 430
    individual = 280
    ingredientes = [['ja', 'Jamón', 40], ['ch', 'Champiñón', 35], ['pi', "Pimentón", 30], ['dq', "Doble queso", 40],
                    ['ac', "Aceitunas", 57.5], ['pp', 'Pepperoni', 38.5], ['sa', 'Salchichón', 62.5]]

    nsand = 0  # número de sandwiches
    val = 1
    cuenta = 0  # total a pagar

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
                aux = 0
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

        # Agregar sandwich al archivo CSV
        nombreorden = "Sandwich " + ntam + " con " + nombreorden
        csv_management.append_order(nombreorden, cuentaindiv)
        print()
        print("Subtotal a pagar por un sándwich ", ntam, ": ", cuentaindiv)
        cuenta += cuentaindiv
        print("*********************************")
        auxi = 0
        resp = ''
        while auxi == 0:
            resp = input("¿Desea continuar [s/n]?: ")
            if resp != 's' and resp != 'n':
                print('Opción no válida')
            else:
                auxi = 1
        if resp == 'n':
            val = 0
        print()

    print('El pedido tiene un total de ', nsand, ' sándwich(es) por un monto de ', cuenta, '\n')
    print('Gracias por su compra, regrese pronto')
