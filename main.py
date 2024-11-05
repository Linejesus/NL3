from math import *

def menu():
    while True:
        print("\n--------------------------------------------------------------------------\n")
        print("Selecione quantos polarizadores você tem (1-3): ")
        quantidade = input("\n1 - 1 Polarizador \n2 - 2 Polarizadores 2 \n3 - 3 Polarizadores \nSair = 4\n")
        if quantidade == "1":
            Pola()
        elif quantidade == "2":
            Polarizador()
        else:
            break
    


def Pola():
    intensidade = float(input("Digite o valor da intensidade: "))
    filtro = int(input("Digite 0 para filtro polarizado ou 1 para filtro não polarizado"))
    if filtro == 0:
        pass

def Polarizador():
    pass

if __name__ == '__main__':
    print("\nAutores: Aline Rocha de Jesus e Arthur Carvalho Rotkis")
    print("O objetivo deste projeto é demonstrar, por meio de um código Python, os polarizadores.")
