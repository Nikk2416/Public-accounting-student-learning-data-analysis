#En este archivo voy realizando las funciones destinadas al proyecto principal

#Solicitar al usuario el importe de carga fabril a distribuir
def Solicitar_imp_cf(): #Defino la función
    while True: #Creo un bucle infinito para controlar errores
        Imp_cf = input('Por favor ingrese el total del costo en carga fabril a distribuir: ') #Solicito al usuario el importe
        try: 
           Imp_cf = float(Imp_cf) #Intento convertir el importe en un flotante
        except: print('Debes ingresar un numero') #Si no es posible muestro un mensaje y se repite el bucle
        else: 
            if Imp_cf > 0: break #Si el importe es positivo se termina el bucle
            else: print('Debe ser un número positivo') #Caso contrario se repite
    return Imp_cf #Retorno la variable que contiene el importe

#Solicitar cantidad producida
def Solicitar_cant_u():
    while True: #Creo un bucle infinito para controlar errores
        Q_art = input('Por favor ingrese el total de unidades producidas del artículo: ') #Solicito al usuario el importe
        try: 
           Q_art = int(Q_art) #Intento convertir la cantidad en un entero
        except: print('Debes ingresar un numero') #Si no es posible muestro un mensaje y se repite el bucle
        else: 
            if Q_art > 0: break #Si la cantidad es positiva se termina el bucle
            else: print('Debe ser un número positivo') #Caso contrario se repite
    return Q_art #Retorno la variable que contiene la cantidad de unidades

#Defino la funcion para solicitarle al usuario que método va a utilizar 
def Solicitar_met():
    while True:
         met_a_utilizar = input('por favor ingrese el método a utilizar: ')
         try: met_a_utilizar = int(met_a_utilizar)
         except: print('Por favor elija uno de los métodos propuestos')
         else:
             if met_a_utilizar in (1,2,3,4,5): break
             else: print('Por favor elija uno de los métodos propuestos')
    return met_a_utilizar
    


#Defino la función para realizar el primer método, el método de asignación por unidades producidas
def met_unidades(Cf_a_dist,cantidad_total):
    cuota_cf = Cf_a_dist/cantidad_total
    return cuota_cf

#Defino la función para solicitar las horas hombre por producto
def Solicitar_cant_HH():
    while True: #Creo un bucle infinito para controlar errores
        hh_art = input('Por favor ingrese las de horas hombre necesarias para producir un artículo: ') #Solicito al usuario el importe
        try: 
           hh_art = float(hh_art) #Intento convertir la cantidad en un flotante
        except: print('Debes ingresar un numero') #Si no es posible muestro un mensaje y se repite el bucle
        else: 
            if hh_art > 0: break #Si la cantidad es positiva se termina el bucle
            else: print('Debe ser un número positivo') #Caso contrario se repite
    return hh_art#Retorno la variable que contiene la cantidad de unidades


#Defino la función para solicitar las horas maquina por producto
def Solicitar_cant_HM():
    while True: #Creo un bucle infinito para controlar errores
        hm_art = input('Por favor ingrese las de horas maquina necesarias para producir un artículo: ') #Solicito al usuario el importe
        try: 
           hm_art = float(hm_art) #Intento convertir la cantidad en un flotante
        except: print('Debes ingresar un numero') #Si no es posible muestro un mensaje y se repite el bucle
        else: 
            if hm_art > 0: break #Si la cantidad es positiva se termina el bucle
            else: print('Debe ser un número positivo') #Caso contrario se repite
    return hm_art#Retorno la variable que contiene la cantidad de unidades


#defino la función para solicitar el material directo unitario a usar en cada articulo
def Solicitar_Mdu():
    while True:
        md_por_art = input('Por favor ingrese el importe de materiales directos necesarios para producir un artículo: ')
        try:
            md_por_art = float(md_por_art)
        except: print('Tenes que ingresar un número')
        else:
            if md_por_art > 0: break
            else: print('Debe ser un número positivo')
    return md_por_art

#defino la función para solicitar la mano de obra directa necesaria en cada articulo
def Solicitar_Modu():
    while True:
        mod_por_art = input('Por favor ingrese el importe de mano de obra directa necesaria para producir un artículo: ')
        try:
            mod_por_art = float(mod_por_art)
        except: print('Tenes que ingresar un número')
        else:
            if mod_por_art > 0: break
            else: print('Debe ser un número positivo')
    return mod_por_art
