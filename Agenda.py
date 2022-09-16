from agendaTele import agentaTelefonica
registro=[]

#Crear contactos
def nuevocontacto(nombreCliente, noDPI, direccion):
    registro.append(agentaTelefonica(nombreCliente,noDPI,direccion))


#mostrar contactos
def mostrarcontactos():
    for i in range(len(registro)):
        print(registro[i].verNombre())
        print(registro[i].verNoDPI())
        print(registro[i].verdireccion())
        print('\n\n')
    print('------------------------------------------')

#Buscar contacto y modificar

def buscarymodificar(nombreCliente, nuevaDireccion):
    posicion=None
    for i in range (len(registro)):
        if nombreCliente==registro[i].verNombre():
            posicion=i
            break
    if posicion==None:
        return 'El cliente ingresado no existe'
    else:
        registro[posicion].modificardireccion(nuevaDireccion)
        return 'Datos del cliente actualizados con éxito'

#Buscar y eliminar
def buscaryeliminar(nombreCliente):
    posicion= None
    for i in range(len(registro)):
        if nombreCliente==registro[i].verNombre():
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
            nombre=input('Ingrese el nombre del cliente: ')
            dpi=int(input('Ingrese el número de DPI del cliente: '))
            direccion=input('Ingrese la direccion del cliente: ')
            nuevocontacto(nombre,dpi,direccion)
            print('------------------Cliente registrado con éxito------------------\n\n')
        
        elif op==2:
            mostrarcontactos()
            print('\n')
        
        elif op==3:
            nombre=input('Ingrese el nombre del cliente: ')
            nuevadireccion=input('Ingrese nueva dirección del cliente: ')
            print(buscarymodificar(nombre,nuevadireccion))
            print('------------------------------------------------------\n\n')
        
        elif op==4:
            nombre=input('Ingrese el nombre del cliente: ')
            print(buscaryeliminar(nombre))
            print('------------------------------------------------------\n\n')
        elif op==5:
            print('------------------SALIENDO DEL PROGRAMA------------------\n\n')
        else:
            print('Número de opción no válido')
        
main()

          