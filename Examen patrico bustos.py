import csv
import random
menu=-1
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
empleados=[]
nombres={}
def asignar_sueldo():
    for trab in trabajadores:
        nombres=trab
        trab=random.randint(300000,2500000)
        empleados.append([f"nombre:{nombres}",f"sueldo:",f"{int(trab)}"])
    for i in empleados:
        print(i)
    print("se han generado los suldos :D")

def clasificar_sueldo():
    try:
        print("sueldos menores a $800000")
        for i in empleados:
            valor=int(i[2])
        
            if valor <800000:
                print(i)
        print("sueldos entre $800000 y $2000000")
        for i in empleados:
            valor=int(i[2])
            if 800000<valor<2000000:
                print(i)
        print("sueldos mayores a $2000000")
        for i in empleados:
            valor=int(i[2])
            if 2000000<valor:
                print(i)
    except KeyError:
       print("no hay datos...")
def estadisticas():
    try:
        menor=2500000
        mayor=0
        promedio=0
        media=1
        for i in empleados:
            valor=int(i[2])
            if valor<menor:
                menor=valor
        print(f"el sueldo menor es de {menor}")
        for i in empleados:
            valor=int(i[2])
            if valor>mayor:
                mayor=valor
        print(f"el sueldo mayor es de {mayor}")
        for i in empleados:
            valor=int(i[2])
            promedio=promedio+valor
        promedio=(promedio/10)
        print(f"el promedio de los datos es de {promedio}")
        for i in empleados:
            valor=int(i[2])
            media*=valor
        media=media**(1/10)
        print(f"la media geometrica es {media}")
    except KeyError:
        print("no hay datos")


def salir():
    print("Saliendo del programa...")
    print("Desarrollado por Patricio Bustos")
    print("Rut:21899522-5")
    

def importar_csv():
    with open("trabajadores.csv",mode="w",newline="",encoding='utf-8') as file:
        archivo=csv.writer(file)
        archivo.writerow(["Nombre del empleado","sueldo base","descuento salud","descuento afp","sueldo liquido"])
        for i in empleados:
            valor=int(i[2])
            salud=valor*0.07
            afp=valor*0.12
            liquido=valor-salud-afp
            archivo.writerow([i[0],i[1],valor,salud,afp,liquido])
        

while menu!=0:
    print("1.- Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadísticas.")
    print("4.- Reporte de sueldos")
    print("5.- Salir del programa")
    try:
        menu=int(input(">>>"))
    except ValueError:
        print("solo se pueden ingresar caracteres numericos...")
    else:
        if menu==1:
            asignar_sueldo()
        if menu==5:
            salir()
            menu=0
        if menu==2:
            clasificar_sueldo()
        if menu==3:
            estadisticas()
        if menu==4:
            importar_csv()