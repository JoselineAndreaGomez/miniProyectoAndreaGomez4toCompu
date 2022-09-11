class agentaTelefonica:
    def __init__(self,nombreCompleto,noDPI,direccion):
        self.__nombre=nombreCompleto
        self.__noDPI=noDPI
        self.__direccion=direccion
    
    #crear métodos GETTER
    def verNombre(self):
        return self.__nombre
    
    def verNoDPI(self):
        return self.__noDPI
    
    def verdireccion(self):
        return self.__direccion
    
    #métodos SETTER
    def modificarNombre(self,nuevonombre):
        self.__nombre=nuevonombre
    
    def modificarDPI(self,nuevoDPI):
        self.__noDPI=nuevoDPI
    
    def modificardireccion(self,nuevadireccion):
        self.__direccion=nuevadireccion