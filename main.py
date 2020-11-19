import order
import csv_management

print("*******************************************************")
print("*                SANDWICHES UCAB                       *")
print("*******************************************************\n")

op = -1

while op != 0:
    print("\tSeleccione una opción\n")
    print("1. Ver historial de compras")
    print("2. Ordenar sandwiches")
    print("3. Ver lista de precios")
    print("0. Salir")
    op = input()

    if op not in ['1', '2', '3', '0']:
        print("Opcion fuera de rango")
    else:
        if op == '1':
            print("*******************************************************")
            print("*                HISTORICO DE ORDENES                 *")
            print("*******************************************************\n")
            csv_management.print_all_orders()
        elif op == '2':
            order.order()
        elif op == '3':
            print("Opcion 3...")
        else:
            print("Hasta pronto!")
            exit(0)