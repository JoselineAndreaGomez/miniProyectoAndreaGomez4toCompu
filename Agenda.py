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

def bymcontacto(nombre,nuevonom,numero):
    posicion=None
    for i in range (len(registro)):
        if nombre==registro[i].verNombre():
            posicion=i
            break
    if posicion==None:
        return 'El contacto ingresado no existe'
    else:
        registro[posicion].modificarNum(numero)
        registro[posicion].modificarNombre(nuevonom)
        return 'Contacto actualizado con éxito'

#Buscar y eliminar
def buscaryeliminar(nombre):
    posicion= None
    for i in range(len(registro)):
        if nombre==registro[i].verNombre():
            posicion=i
            break
    if posicion==None:
        return 'El contacto no existe'
    else:
        registro.pop(posicion)
        return 'Contacto eliminado con éxito'

#buscaracontacto en específico
def buscarEnEspecifico(nombre):
    if len(registro) ==0:
        print('El registro de números está vacía')
    else:
        encontrado=False
        for i in range (len(registro)):
            if registro[i].verNombre()==nombre:
                print('El número telefónico es: ',registro[i].vernumero())
                encontrado=True
                break
            else:
                encontrado=False
        if encontrado==False:
            print('Nombre ingresado no existente')


#ARRANQUE DEL PROGRAMA------------------------------------------------------------
def main():
    op=0
    while op!=7:
        print('AGENDA TELEFÓNICA \n',
        '1. Crear contacto \n',
        '2. Ver contactos \n',
        '3. Modificar contactos \n',
        '4. Eliminar contacto\n',
        '5. Buscar contacto en específico \n',
        '6. Mostrar registro en HTML \n'
        '7. SALIR DE LA AGENDA TELEFÓNICA\n\n'
        )
        op=int(input('Ingrese una opción del menú: '))
        if op==1:
            nombre=input('Ingrese el nombre del contacto: ')
            num=int(input('Ingrese el número del contacto: '))
            nuevocontacto(nombre,num)
            print('------------------Contacto registrado con éxito------------------\n\n')
        
        elif op==2:
            mostrarcontactos()
        
        elif op==3:
            nombre=input('Ingrese el nombre del contacto: ')
            nuevoNom=input('Ingrese el nuevo nombre: ')
            nuevoNum=int(input('Ingrese el nuevo número: '))
            print(bymcontacto(nombre,nuevoNom,nuevoNum))
            print('---------------------------------------------- \n\n')
            
        elif op==4:
            nombre=input('Ingrese el nombre del contacto: ')
            print(buscaryeliminar(nombre))
            print('------------------------------------------------------\n\n')

        elif op==5:
            nombre=input('Ingrese el nombre del contacto: ')
            print(buscarEnEspecifico(nombre))
            print('---------------------------------------------------- \n\n')

        elif op==6:
            print('Aquí va el registro ')
            print('---------------------------------------------------- \n\n')

        elif op==7:
            print('------------------SALIENDO DEL PROGRAMA------------------\n\n')
        else:
            print('Número de opción no válido')
            print('-------------------------------------------------------- \n\n')
#INICIAR EL PROGRAMA        
main()

          