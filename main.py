from math import *

def menu():
    while True:
        print("\n--------------------------------------------------------------------------\n")
        print("Selecione quantos polarizadores você tem (1-3): ")
        quantidade = input("\n1 - 1 Polarizador \n2 - 2 Polarizadores\n3 - 3 Polarizadores \n4 - Sair\n")
        if quantidade == "1":
            Pola()
        elif quantidade == "2":
            Polariza()
        elif quantidade == "3":
            Polarizador()
        else:
            break
    


def Pola():
    qualIntensidade = int(input("\n\n0 - Intensidade Inicial\n1 - Intensidade Final\nDigite qual intensidade você possui: "))
    intensidade = float(input("\nDigite o valor da intensidade (em W/cm²): "))
    feicheLuz = int(input("\n0 - Feiche de luz polarizado\n1 - Feiche de luz não polarizado\nDigite qual seu feiche de luz: "))
    
    if qualIntensidade == 0:
        if feicheLuz == 0:
            angulo = int(input("\nDigite o valor do ângulo (em graus): "))
            intensidadeDepois = intensidade * ((cos(angulo))**2)
        elif feicheLuz == 1:
            intensidadeDepois = intensidade / 2
        
        print(f"\nIntensidade Final: {intensidadeDepois:.2e} W/cm²")

    elif qualIntensidade == 1:
        if feicheLuz == 0:
            angulo = int(input("\nDigite o valor do ângulo (em graus): "))
            intensidadeAntes = intensidade / ((cos(angulo))**2)
        elif feicheLuz == 1:
            intensidadeAntes = intensidade * 2
        
        print(f"\nIntensidade Inicial: {intensidadeAntes:.2e} W/cm²")


def Polariza():
    qualIntensidade = int(input("\n\n1 - Primeira Intensidade\n2 - Segunda Intensidade\n3 - Terceira Intensidade\nDigite qual intensidade você possui: "))
    intensidade = float(input("\nDigite o valor da intensidade (em W/cm²): "))
    feicheLuz = int(input("\n0 - Feiche de luz polarizado\n1 - Feiche de luz não polarizado\nDigite qual seu feiche de luz: "))
    primeiroAngulo = float(input("\nDigite o valor do primeiro ângulo (em graus): "))
    segundoAngulo = float(input("\nDigite o valor do segundo ângulo (em graus): "))

    if qualIntensidade == 1:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            segundaIntensidade = intensidade / 2
            terceiraIntensidade = segundaIntensidade * (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
        
        print(f"\nIntensidade da luz após ela ter atravessado o primeiro filtro: {segundaIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o conjunto: {terceiraIntensidade:.2e} W/cm²")

    elif qualIntensidade == 2:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            primeiraIntensidade = intensidade * 2
            terceiraIntensidade = intensidade * (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
        
        print(f"\nIntensidade da luz incidente: {primeiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o conjunto: {terceiraIntensidade:.2e} W/cm²")

    elif qualIntensidade == 3:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            segundaIntensidade = intensidade / (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
            primeiraIntensidade = segundaIntensidade * 2 
        
        print(f"\nIntensidade da luz incidente: {primeiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o primeiro polarizador: {segundaIntensidade:.2e} W/cm²")

def Polarizador():
    qualIntensidade = int(input("\n1 - Primeira Intensidade\n2 - Segunda Intensidade\n3 - Terceira Intensidade\n4 - Quarta Intensidade\nDigite qual intensidade você possui: "))
    intensidade = float(input("\nDigite o valor da intensidade (em W/cm²): "))
    feicheLuz = int(input("\n0 - Feiche de luz polarizado\n1 - Feiche de luz não polarizado\nDigite qual seu feiche de luz: "))
    primeiroAngulo = float(input("\nDigite o valor do primeiro ângulo (em graus): "))
    segundoAngulo = float(input("\nDigite o valor do segundo ângulo (em graus): "))
    terceiroAngulo = float(input("\nDigite o valor do terceiro ângulo (em graus): "))

    if qualIntensidade == 1:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            segundaIntensidade = intensidade / 2
            terceiraIntensidade = segundaIntensidade * (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
            quartaIntensidade = terceiraIntensidade * (cos(radians(terceiroAngulo) - radians(segundoAngulo))**2) 
        
        print(f"\nIntensidade da luz após ela ter atravessado o primeiro polarizador: {segundaIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o segundo polarizador: {terceiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o conjunto: {quartaIntensidade:.2e} W/cm²")

    elif qualIntensidade == 2:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            primeiraIntensidade = intensidade * 2
            terceiraIntensidade = intensidade * (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
            quartaIntensidade = terceiraIntensidade * (cos(radians(terceiroAngulo) - radians(segundoAngulo))**2)
        
        print(f"\nIntensidade da luz incidente: {primeiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz depois de passar pelo segundo polarizador: {terceiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz depois de passar pelo conjunto: {quartaIntensidade:.2e} W/cm²")

    elif qualIntensidade == 3:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            segundaIntensidade = intensidade / (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
            primeiraIntensidade = segundaIntensidade * 2 
            quartaIntensidade = intensidade * (cos(radians(terceiroAngulo) - radians(segundoAngulo))**2)
        
        print(f"\nIntensidade da luz incidente: {primeiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o primeiro polarizador: {segundaIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz depois de passar pelo conjunto: {quartaIntensidade:.2e} W/cm²")

    elif qualIntensidade == 4:
        if feicheLuz == 0:
            pass

        elif feicheLuz == 1:
            terceiraIntensidade = intensidade / (cos(radians(terceiroAngulo) - radians(segundoAngulo))**2) 
            segundaIntensidade = terceiraIntensidade / (cos(radians(segundoAngulo) - radians(primeiroAngulo))**2) 
            primeiraIntensidade = segundaIntensidade * 2 
        
        print(f"\nIntensidade da luz incidente: {primeiraIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o primeiro polarizador: {segundaIntensidade:.2e} W/cm²")
        print(f"Intensidade da luz após ela ter atravessado o segundo polarizador: {terceiraIntensidade:.2e} W/cm²")


if __name__ == '__main__':
    print("\nAutores: Aline Rocha de Jesus e Arthur Carvalho Rotkis")
    print("O objetivo deste projeto é demonstrar, por meio de um código Python. O nosso programa calcula a intensidade que passa através dos polarizadores.\nNa física, a polarização é uma característica fundamental das ondas eletromagnéticas, que descreve a orientação espacial dos vetores campo elétrico e campo magnético.\nOs polarizadores funcionam como uma fenda permitindo que a luz passe somente em um plano. Se acontecer de dois polarizadores estarem alinhados na mesma direção, a luz passa pelo primeiro, mas no segundo não se vê nada, pois não haverá emergência de luz. O acontecimento da polarização da luz dá evidências claras de que ela é formada por ondas transversais.")
    menu()
