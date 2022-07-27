from os import system
import sys
import colorama
from colorama import Fore, Back, Style
import time

import mysql.connector
from mysql.connector import Error

cnn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", db="tienda")

productos = []
precio_final = 0

colorama.init()

def agregar_producto():
    Cantidad = int(input("Ingrese la cantidad de productos: "))
    Nombre_producto = input("Ingrese el nombre del producto: ")
    Codigo_producto = int(input("Ingrese el codigo del producto: "))
    Valor_Unitario = int(input("Ingrese el precio del producto: "))
    total = Cantidad * Valor_Unitario
    productos.append([Cantidad, Nombre_producto, Codigo_producto, Valor_Unitario, total])
    print ("Valor total: ", total)
    cur = cnn.cursor()
    cur.execute("INSERT INTO carrito (Cantidad, Nombre_producto, Codigo_producto, Valor_Unitario, total) VALUES (%s, %s, %s, %s, %s)", (Cantidad, Nombre_producto, Codigo_producto, Valor_Unitario, total))
    cnn.commit()
    print("Producto agregado")
    time.sleep(1)
    system("cls")

def limpiar_carrito():
    cur = cnn.cursor()
    cur.execute("DELETE FROM carrito")
    cnn.commit()
    productos.clear()
    print(Fore.GREEN + "Carrito limpio" + Fore.RESET)
    system("cls") 
def generar_factura():
    print("----------------------------------------------------")
    print("Factura Generada")
    print("----------------------------------------------------")
    print("")
    print("Nombre: Los monitos de la Nona")
    print("direccion: Calle falsa 123")
    print("Telefono: 123456789")
    print("Fecha: ", time.strftime("%d/%m/%Y"))
    print("")
    print(Fore.GREEN +"Productos:" + Fore.RESET)
    cur = cnn.cursor()
    cur.execute("SELECT * FROM carrito")
    rows = cur.fetchall()
    for row in rows:
        print(Fore.GREEN +"*----------------------------------*" + Fore.RESET)
        print("Cantidad: ", row[1])
        print("Nombre del producto: ", row[2])
        print("Precio unitario: ", row[4])
        print(Fore.GREEN +"*----------------------------------*" + Fore.RESET)
    cur.execute("SELECT SUM(total) FROM carrito")
    for row in cur.fetchall():
        print(Fore.LIGHTCYAN_EX+"[SISTEMA] Precio total de la compra: "+Fore.RESET, row[0])    
    time.sleep(3)
    system("cls")



def mostrar_carrito():
    cur = cnn.cursor()
    cur.execute("SELECT * FROM carrito")
    rows = cur.fetchall()
    for row in rows:
        print("----------------------------------------------------")
        print("Cantidad: ", row[1])
        print("Nombre del producto: ", row[2])
        print("Precio unitario: ", row[4])
    time.sleep(2.2)    
    print(Fore.CYAN+"----------------------------------------------------"+Fore.RESET)
    cur.execute("SELECT SUM(total) FROM carrito")
    for row in cur.fetchall():
        print(Fore.LIGHTCYAN_EX+"[SISTEMA] Precio total de la compra: "+Fore.RESET, row[0])
    print(Fore.CYAN+"----------------------------------------------------"+Fore.RESET)
    time.sleep(3.5)
    system("cls")

def agregar_inventario():
    Cantidad = int(input("Ingrese la cantidad de productos: "))
    Nombre_producto = input("Ingrese el nombre del producto: ")
    Codigo_producto = int(input("Ingrese el codigo del producto: "))
    Valor_Unitario = int(input("Ingrese el precio del producto: "))
    total = Cantidad * Valor_Unitario
    productos.append([Cantidad, Nombre_producto, Codigo_producto, Valor_Unitario])
    cur = cnn.cursor()
    cur.execute("INSERT INTO inventario (Cantidad, Nombre_producto, Codigo_producto, Valor_Unitario) VALUES (%s, %s, %s, %s)", (Cantidad, Nombre_producto, Codigo_producto, Valor_Unitario))
    cnn.commit()
    print("Inventario Agregado")
    time.sleep(1)
    system("cls")
def mostrar_inventario():
    cur = cnn.cursor()
    cur.execute("SELECT * FROM inventario")
    rows = cur.fetchall()
    for row in rows:
        print("----------------------------------------------------")
        print("Cantidad: ", row[1])
        print("Nombre del producto: ", row[2])
        print("Precio unitario: ", row[4])
    time.sleep(2.2)    
    system("cls")

def menu():
    system("cls")
    while (True):
        print("")                                                           
        print(Fore.LIGHTRED_EX+"    ███      ▄█     ▄████████ ███▄▄▄▄   ████████▄     ▄████████".center(120))    
        print(Fore.LIGHTRED_EX+"▀█████████▄ ███    ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███".center(120))
        print(Fore.LIGHTRED_EX+"   ▀███▀▀██ ███▌   ███    █▀  ███   ███ ███    ███   ███    ███".center(120))  
        print(Fore.LIGHTRED_EX+"    ███   ▀ ███▌  ▄███▄▄▄     ███   ███ ███    ███   ███    ███".center(120))  
        print(Fore.LIGHTRED_EX+"    ███     ███▌ ▀▀███▀▀▀     ███   ███ ███    ███ ▀███████████".center(120))  
        print(Fore.LIGHTRED_EX+"    ███     ███    ███    █▄  ███   ███ ███    ███   ███    ███".center(120)) 
        print(Fore.LIGHTRED_EX+"    ███     ███    ███    ███ ███   ███ ███   ▄███   ███    ███".center(120))  
        print(Fore.LIGHTRED_EX+"   ▄████▀   █▀     ██████████  ▀█   █▀  ████████▀    ███    █▀ ".center(120))  
        print(""+Fore.RESET)
        print("-           Los monitos de la Nona                 -".center(121))
        print("")
        print("1. Agregar productos".center(120))
        print("2. Mostrar Carrito".center(117))
        print("3. Limpiar Carrito".center(117))
        print("4. Generar Factura".center(117))
        print("")
        print(Fore.CYAN +"------------------------------".center(117))
        print("5. Agregar Inventario".center(121))
        print("6. Mostrar Inventario".center(121))
        print(Fore.CYAN +"------------------------------".center(117))
        print(""+ Fore.RESET)
        opcion = input(Fore.LIGHTRED_EX+"Root@Tienda: "+Fore.RESET)
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_carrito()
        elif opcion == "3":
            limpiar_carrito()
        elif opcion == "4":
            generar_factura()    
        elif opcion == "5":
            agregar_inventario()
        elif opcion == "6":
            mostrar_inventario()
        else:
            print("[SISTEMA] Opcion no valida")
            time.sleep(1)
            system("cls")
menu()        