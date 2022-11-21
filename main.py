
def calcular(v,h,sequencia):
    robo_lugarV = 0
    robo_lugarH = 0
    direcao = 0
    for ordem in sequencia:

        # 0 Norte
        # 1 leste
        # 2 Sul
        # 3 Oeste

        # D
        if ordem == "D" and direcao == 0:
            direcao = direcao + 1
        elif ordem == "D" and direcao == 1:
            direcao = direcao + 1
        elif ordem == "D" and direcao == 2:
            direcao = direcao + 1
        elif ordem == "D" and direcao == 3:
            direcao = direcao = 0

        # E
        if ordem == "E" and direcao == 0:
            direcao = direcao = 3
        elif ordem == "E" and direcao == 1:
            direcao = direcao - 1
        elif ordem == "E" and direcao == 2:
            direcao = direcao - 1
        elif ordem == "E" and direcao == 3:
            direcao = direcao - 1

        # F
        if ordem == "F" and direcao == 0 and robo_lugarV != v  :
            robo_lugarV = robo_lugarV + 1
        elif ordem == "F" and direcao == 1 and robo_lugarH != h:
            robo_lugarH = robo_lugarH + 1
        elif ordem == "F" and direcao == 2 and robo_lugarV != v:
            if robo_lugarV > 0 :
                robo_lugarV = robo_lugarV - 1
        elif ordem == "F" and direcao == 3 and robo_lugarH != h:
            if robo_lugarH > 0:
                robo_lugarH = robo_lugarH - 1

        # T
        if ordem == "T" and direcao == 0 and robo_lugarV != v:
            if robo_lugarV > 0:
                robo_lugarV = robo_lugarV - 1
        elif ordem == "T" and direcao == 1 and robo_lugarH != h:
            if robo_lugarH > 0:
                robo_lugarH = robo_lugarH - 1
        elif ordem == "T" and direcao == 2 and robo_lugarV != v:
            robo_lugarV = robo_lugarV + 1
        elif ordem == "T" and direcao == 3 and robo_lugarH != h:
            robo_lugarH = robo_lugarH + 1

        if direcao == 0:
            direcao2 = "N"
        elif direcao == 1:
            direcao2 = "L"
        elif direcao == 2:
            direcao2 = "S"
        elif direcao == 3:
            direcao2 = "O"
    return [direcao2,robo_lugarH,robo_lugarV]



dimensoes = input("entre com as dimensoes")
sequencia = input("entre com as testes")


#largura
h = int(dimensoes.split()[0])
#comprimento
v = int(dimensoes.split()[1])

print(calcular(v,h,sequencia))

