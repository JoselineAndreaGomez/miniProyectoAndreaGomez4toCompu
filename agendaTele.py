class agentaTelefonica:
    def __init__(self,nombreCompleto,numero):
        self.__nombre=nombreCompleto
        self.__numero=numero
    
    #crear métodos GETTER
    def verNombre(self):
        return self.__nombre
    
    def vernumero(self):
        return self.__numero
    
    #métodos SETTER
    def modificarNombre(self,nuevonombre):
        self.__nombre=nuevonombre
    
    def modificarNum(self,nuevonum):
        self.__numero=nuevonum
