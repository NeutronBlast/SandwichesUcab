import csv_management

def ordenar_bebida():
    op = 1
    cuenta = 0 #total a pagar por bebida(s)
    agregar = ''
    while op == 1: # ciclo que evalua si desea agregar bebida o no
        agregar = input("¿Desea agregar bebida(s) a la cuenta [s/n]?: ")
        if agregar != 's' and agregar != 'n':
            print('Opción no válida')
        elif agregar == 'n':
            op = 0
            return cuenta 
        else:     #Condicion si desea agregar bebida
            op = 0 
            bebidas = 0
            grande = 200
            pequeño = 100
            val = 1
            while val == 1:  # ciclo por cada bebida
                nombreorden = ''
                bebidas += 1
                cuenta_bebida = 0
                ntam = ''
                nsabor = ''
                valaux = 0
                
                while valaux == 0:  # ciclo para evaluar el tamaño de la bebida
                    tam = input("Tamaños: Grande ( g ) Pequeño ( p ): ")
                    if tam != 'g' and tam != 'p':
                        print("Debe seleccionar el tamaño correcto!!")
                    else:
                        valaux = 1
                        if tam == 'g':
                            print("Ha elegido el tamaño grande")
                            ntam = 'Grande'
                            cuenta_bebida += grande
                        elif tam == 'p':
                            print("Ha elegido el tamaño pequeño")
                            ntam = 'Pequeño'
                            cuenta_bebida += pequeño
                        
                print()
                print("Sabor de Bebida:")
                print("Coca-Cola           (co)")
                print("Frescolita          (fr)")
                print("7-up                (up)")
                valsabor = 0
                while valsabor == 0:    # ciclo para evaluar el sabor de la bebida
                    sab = input("Indique el sabor: ")
                    if sab != 'co' and sab != 'fr' and sab != 'up':
                        print("Debe seleccionar el sabor correcto!!")
                    else:
                        valsabor = 1
                        if sab == 'co':
                            print("Ha elegido el sabor Coca-Cola")
                            nsabor = 'Coca-Cola'
                        elif sab == 'fr':
                            print("Ha elegido el sabor Frescolita")
                            nsabor = 'Frescolita'
                        elif sab == 'up':
                            print("Ha elegido el sabor 7-up")
                            nsabor = '7-up'

                print("Usted seleccionó una bebida ", ntam, " sabor: ", nsabor)
                print()
                print("Subtotal a pagar por una bebida ", ntam, ": ", cuenta_bebida)

                # Agregar bebida al archivo CSV
                cuenta += cuenta_bebida
                nombreorden = "Bebida tamaño " + ntam  
                csv_management.append_order(nombreorden, cuenta_bebida)
                #
                print("*********************************")
                auxi = 0
                resp = ''
                while auxi == 0:
                    resp = input("¿Desea agregar otra bebida [s/n]?: ")
                    if resp != 's' and resp != 'n':
                        print('Opción no válida')
                    else:
                        auxi = 1
                if resp == 'n':
                    val = 0
                print()
            print('El pedido tiene un total de ', bebidas, ' bebida(s) por un monto de ', cuenta, '\n')
            return cuenta