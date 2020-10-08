class Caballo:
    def __init__(self,a,b,c,d):
        self.moves = []
        self.moves.append([1,2])   #1
        self.moves.append([2,1])   #2
        self.moves.append([2,-1])  #3
        self.moves.append([1,-2])  #4
        self.moves.append([-1,-2]) #5
        self.moves.append([-2,-1]) #6
        self.moves.append([-2,1])  #7
        self.moves.append([-1,2])  #8
        self.movesi = []
        self.movesi.append([-1,2])  #1
        self.movesi.append([-2,1])  #2
        self.movesi.append([-2,-1]) #3
        self.movesi.append([-1,-2]) #4
        self.movesi.append([1,-2])  #5
        self.movesi.append([2,-1])  #6
        self.movesi.append([2,1])   #7
        self.movesi.append([1,2])   #8

        self.conta = 0
        self.Principal(a,b,c,d)
    
    def Principal(self,a,b,c,d):        
        ini = [a,b]
        end = [c,d]
        switch = 0
        pFin = self.Posibles(switch,end)
        
        #Si el nodo final es mayor al inicial se buscan todos los puntos posibles mayores al inicial
        #de lo contrario, se buscan todos los puntos posibles menores al punto inicial
        adentro = True
        while adentro:
            if ini < end:
                switch = 1
            else:
                switch = 2
            p = self.Posibles(switch,ini)
            #Buscamos si hay algún cruce para el punto inicial contra la lista de posibles puntos finales
            resp = self.Intersec(pFin,p)
            if resp:
                ini = resp
                adentro = False
                break
            aux1 = []
            #Buscamos si alguno de los posibles de los 2 puntos principales de los posibles se cruzan con la lista de posibles final
            ini = p[0]
            self.conta +=1
            p0 = self.Posibles(0,ini)
            resp = self.Intersec(pFin,p0)
            if resp:
                ini = resp
                adentro = False
                break
            else:
                ini = p[1]
                p1 = self.Posibles(0,ini)
                resp = self.Intersec(pFin,p1)
                if resp:
                    ini = resp
                    adentro = False
                    break
                else:
                    #Si no hay cruces, entonces buscamos el posible nodo más cercano al final
                    aux = [end[0] - abs(p[0][0]),end[1] - abs(p[0][1])]
                    aux1 = [end[0] - abs(p[1][0]),end[1] - abs(p[1][1])]
                    aux2 = [end[0] - abs(p[2][0]),end[1] - abs(p[2][1])]
                    aux3 = [end[0] - abs(p[3][0]),end[1] - abs(p[3][1])]
                    iniArray = []
                    if ini < end:
                        if aux > aux1:
                            iniArray.append(p[0])
                        if aux1 > aux2:
                            iniArray.append(p[1])
                        if aux2 > aux3:
                            iniArray.append(p[2])
                        if aux3 > aux:
                            iniArray.append(p[3])
                        if len(iniArray) > 1:                            
                            iniArray.sort(reverse=True)
                    else:       
                        if aux3 > aux:                            
                            iniArray.append(p[3])
                        if aux2 > aux3:                            
                            iniArray.append(p[2])
                        if aux1 > aux2:
                            iniArray.append(p[1])
                        if aux > aux1:
                            iniArray.append(p[0])
                        if len(iniArray) > 1:
                            iniArray.sort()
                    ini = iniArray[0]            
            
            # Si alguna de las coordenadas está cerca al punto final, Buscamos intersección
            if ini[0] == end[0] or ini[0] == end[1] or ini[1] == end[0] or ini[1] == end[1]:
                pFin1 = self.Posibles(0,ini)
                resp = self.Intersec(pFin,pFin1)
                if resp:
                    ini = resp
                    adentro = False
                    break

        self.conta +=1 #Se suma el último movimiento al punto fin (b)
        print("Quantity: ",self.conta)                 

    def Intersec(self,pFin,pFin1):
        ans = None
        for pos in range(len(pFin1)):
            if pFin1[pos] in pFin:
                ans = pFin1[pos]
                self.conta +=1
                break
        return ans

    def Posibles(self,case,point):
        posibles = []
        for i in range(8):
            if case == 0:
                nextp = [point[0] + self.moves[i][0],point[1] + self.moves[i][1]]
                posibles.append(nextp)
            elif case == 1:
                nextp = [point[0] + self.moves[i][0],point[1] + self.moves[i][1]]
                if nextp>point:
                    posibles.append(nextp)
            elif case == 2:                
                nextp = [point[0] + self.movesi[i][0],point[1] + self.movesi[i][1]]
                if nextp<point:
                    posibles.append(nextp)
        return posibles

Caballo(-5,-5,5,5)
#Caballo(-2,4,-1,3)
#Caballo(4,-2,-2,2)