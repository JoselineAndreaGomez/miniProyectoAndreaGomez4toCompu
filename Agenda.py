from agendaTele import agentaTelefonica
registro=[]

#Creacion de objetos
def nuevoRegistro(nombreCliente, noDPI, direccion):
    registro.append(agentaTelefonica(nombreCliente,noDPI,direccion))

#Mostrar los registros por nombre

def mostrarRegistros():
    for i in range(len(registro)):
        print(registro[i].verNombre())
    print('------------------------------------------')

#Buscar registro y actualizar datos

def buscarRegistroActualizar(nombreCliente, nuevoDPI, nuevaDireccion):
    posicion=None
    for i in range (len(registro)):
        if nombreCliente==registro[i].verNombre():
            posicion=i
            break
    if posicion==None:
        return 'El cliente ingresado no existe'
    else:
        registro[posicion].modificarDPI(nuevoDPI)
        registro[posicion].modificardireccion(nuevaDireccion)
        return 'Datos del cliente actualizados con éxito'

#Buscar el registro para obtener la posición y eliminar el registro
def buscarRegistroEliminar(nombreCliente):
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

#arranque del programa

def main():
    op=0
    while op!=5:
        print('CONTROL DE LA AGENDA TELEFÓNICA \n',
        '1. Añadir nuevo registro \n',
        '2. Ver clientes registrados \n',
        '3. Modificar registro de un cliente \n',
        '4. Eliminar cliente\n',
        '5. SALIR DEL CONTROL DE TELEFONÍA \n\n'
        )
        op=int(input('Ingrese una opción del menú: '))
        if op==1:
            nombre=input('Ingrese el nombre del cliente: ')
            dpi=int(input('Ingrese el número de DPI del cliente: '))
            direccion=input('Ingrese la direccion del cliente: ')
            nuevoRegistro(nombre,dpi,direccion)
            print('------------------Cliente registrado con éxito------------------\n\n')
        
        elif op==2:
            mostrarRegistros()
            print('\n\n')
        
        elif op==3:
            nombre=input('Ingrese el nombre del cliente: ')
            nuevoDpi=int(input('Ingrese el nuevo DPI del cliente: '))
            nuevadireccion=input('Ingrese nueva dirección del cliente: ')
            print(buscarRegistroActualizar(nombre,nuevoDpi,nuevadireccion))
            print('------------------------------------------------------\n\n')
        
        elif op==4:
            nombre=input('Ingrese el nombre del cliente: ')
            print(buscarRegistroEliminar(nombre))
            print('------------------------------------------------------\n\n')
        elif op==5:
            print('------------------SALIENDO DEL PROGRAMA------------------\n\n')
        else:
            print('Número de opción no válido')
        
main()

          