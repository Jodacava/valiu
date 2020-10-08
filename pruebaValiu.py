
def turnosCelador(celaCan, diasCan, listDiaIni, listDiaFin):
    resultado = 0
    for i in range(celaCan):
        diaIni = listDiaIni[i]
        diaFin = listDiaFin[i]
        resultado += (diaFin - diaIni)
    return resultado

def cuentaPares(numList):
    conta = 0
    for i in range(len(numList)):
        if (i+1) < len(numList):
            if numList[i] > numList[i+1]:
                conta +=1
    return conta
    
#print(turnosCelador(3,10,[1,2,8],[4,5,9]))
#print(cuentaPares([1,3,2,5,4]))