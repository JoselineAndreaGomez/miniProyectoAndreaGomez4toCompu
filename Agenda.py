from agendaTele import agentaTelefonica
registro=[]

#Crear contactos
def nuevocontacto(nombre,numero):
    registro.append(agentaTelefonica(nombre,numero))


#mostrar contactos
def mostrarcontactos():
    for i in range(len(registro)):
        print(registro[i].verNombre())
        print(registro[i].vernumero())
        print('\n')
    print('------------------------------------------')

#Buscar contacto y modificar

def bymcontacto(nombre,numero):
    posicion=None
    for i in range (len(registro)):
        if nombre==registro[i].verNombre():
            posicion=i
            break
    if posicion==None:
        return 'El cliente ingresado no existe'
    else:
        registro[posicion].modificarNum(numero)
        return 'Datos del cliente actualizados con éxito'

#Buscar y eliminar
def buscaryeliminar(nombre):
    posicion= None
    for i in range(len(registro)):
        if nombre==registro[i].verNombre():
            posicion=i
            break
    if posicion==None:
        return 'El cliente no existe'
    else:
        registro.pop(posicion)
        return 'Cliente eliminado con éxito'


#ARRANQUE DEL PROGRAMA------------------------------------------------------------
def main():
    op=0
    while op!=5:
        print('AGENDA TELEFÓNICA \n',
        '1. Crear contacto \n',
        '2. Ver contactos \n',
        '3. Modificar contactos \n',
        '4. Eliminar contacto\n',
        '5. SALIR DE LA AGENDA TELEFÓNICA\n\n'
        )
        op=int(input('Ingrese una opción del menú: '))
        if op==1:
            nombre=input('Ingrese el nombre del contacto: ')
            num=int(input('Ingrese el número del contacto: '))
            nuevocontacto(nombre,num)
            print('------------------Cliente registrado con éxito------------------\n\n')
        
        elif op==2:
            mostrarcontactos()
        
        elif op==3:
            nombre=input('Ingrese el nombre del contacto: ')
            nuevoNum=int(input('Ingrese el nuevo número: '))
            print(bymcontacto(nombre,nuevoNum))
            print('---------------------------------------------- \n\n')
            
        elif op==4:
            nombre=input('Ingrese el nombre del contacto: ')
            print(buscaryeliminar(nombre))
            print('------------------------------------------------------\n\n')
        elif op==5:
            print('------------------SALIENDO DEL PROGRAMA------------------\n\n')
        else:
            print('Número de opción no válido')
        
main()

          