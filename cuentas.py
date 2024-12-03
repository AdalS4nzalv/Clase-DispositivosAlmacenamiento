class DispositivosAlmacenamiento:
    __totalMB = 0.0
    __totalGB = 0.0
    __totalTB = 0.0
    __dispositivosNecesarios = 0

#Metodo: 1 metodo por cada caso de uso
# def nombreCasoUso(self,parametros(precondiciones separadas con comas))
    def convertirTamanoMBAGB(self,totalMB):
        self.__totalMB = totalMB
        self.__totalGB = self.__totalMB/1024
        return self.__totalGB
    def convertirTamanoGBATB(self,totalGB):
        self.__totalGB = totalGB
        self.__totalTB = self.__totalGB/1024
        return self.__totalTB
    def calcularDispositivosNecesarios(self,totalGB):
        self.__totalGB = totalGB
        self.__dispositivosNecesarios = self.__totalGB/4
        if self.__totalGB % 4 > 0:
            self.__dispositivosNecesarios = (self.__totalGB // 4) + 1
        else:
            self.__dispositivosNecesarios = (self.__totalGB // 4)
        return self.__dispositivosNecesarios
    
    