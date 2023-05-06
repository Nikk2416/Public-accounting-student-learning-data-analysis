#El objetivo de este proyecto es constituir un programa el cual posibilite al usuario saber de que manera 
#distribuir sus costos de carga fabril entre sus articulos mendiante la aplicacion de 5 metodos distintos

#Solicitar al usuario la Cf (carga fabril) a distribuir
import Funciones_proyecto as fp
Cf_a_dist = fp.Solicitar_imp_cf()

#Solicitar al usuario la cantidad producida de Rlos  utilizando una lista y un diccionario

articulos = input('Escriba sus articulos separados por comas: ').split(',')
cantidades = {}

for art in articulos: 
    cantidades[art] = fp.Solicitar_cant_u() #para cada artículo se va a solicitar la cantidad producida y se almacena como valor del key: articulo
    print(cantidades)
#Se obtiene el total de unidades producidas en total
cantidad_total = sum(cantidades.values()) 

#Solicitarle al usiario que elija un método a utilizar
print('Muchas gracias por proporcionar los datos, ahora debe elegir entre uno de los siguientes métodos de distribución:\n1 = metodo por unidades\n2 = metodo por horas hombre\n3 = metodo por horas maquina\n4 = metodo por materiales directos\n5 = metodo por Mano de obra directa ')
print('------------------------------------------------------------------')

met_a_utilizar = fp.Solicitar_met()

print(f'elegiste el método {met_a_utilizar}') #Mostrar el método que eligió
Costo_unit_cf_por_art = {} #Creo diccionario vacio el cual luego va a contener el costo unitario por producto

#Evaluación de métodos
if met_a_utilizar == 1: #Creo el método por unidades
    cuota_cf = fp.met_unidades(Cf_a_dist,cantidad_total) #calculo la cuota de carga fabril
    for art in articulos:#Reparto la cuota para determinar el costo unitario de carga fabril
        Costo_unit_cf_por_art[art] = cuota_cf
    print(f'El costo unitario de cf por producto en este caso es de:\n{Costo_unit_cf_por_art}')
    
    
elif met_a_utilizar == 2: #Creo el método por horas hombre
    Horas_H = {}
    for art in articulos:
        Horas_H[art] = fp.Solicitar_cant_HH() #Solicito la cantidad de horas hombre por art
    art_x_HH = {}
    for art in articulos:
        art_x_HH[art] = Horas_H[art] * cantidades[art] #Guardo la cantdidad de articulos que se hacen en 1 hora por art
    print(f'en una hora se producen:\n{art_x_HH}')
    total_art_x_HH = sum(art_x_HH.values())
    cuota_cf = Cf_a_dist/total_art_x_HH
    for art in articulos:
        Costo_unit_cf_por_art[art] = round((Horas_H[art] * cuota_cf),2)
    print(f'El costo unitario de cf por producto en este caso es de:\n{Costo_unit_cf_por_art}')


elif met_a_utilizar == 3: #Creo el método por horas maquina
    Horas_M = {}
    for art in articulos:
        Horas_M[art] = fp.Solicitar_cant_HM() #Solicito la cantidad de horas hombre por art
    art_x_HM = {}
    for art in articulos:
        art_x_HM[art] = Horas_M[art] * cantidades[art] #Guardo la cantdidad de articulos que se hacen en 1 hora por art
    print(f'en una hora se producen:\n{art_x_HM}')
    total_art_x_HM = sum(art_x_HM.values())
    cuota_cf = Cf_a_dist/total_art_x_HM
    for art in articulos:
        Costo_unit_cf_por_art[art] = round((Horas_M[art] * cuota_cf),2)
    print(f'El costo unitario de cf por producto en este caso es de:\n{Costo_unit_cf_por_art}')
    

elif met_a_utilizar == 4: #Creo el método de distrib por material directo unitario
    md_por_art = {}
    for art in articulos:
        md_por_art[art] = fp.Solicitar_Mdu()
    total_md = sum(md_por_art.values())
    cuota_cf = Cf_a_dist/total_md
    for art in articulos:
        Costo_unit_cf_por_art[art] = round(((cuota_cf*md_por_art[art])/cantidades[art]),2)
    print(f'El costo unitario de cf por producto en este caso es de:\n{Costo_unit_cf_por_art}')
    

elif met_a_utilizar == 5: #Creo el método de distrib por mano de obra directa unitaria
    mod_por_art = {}
    for art in articulos:
        mod_por_art[art] = fp.Solicitar_Modu()
    total_mod = sum(mod_por_art.values())
    cuota_cf = Cf_a_dist/total_mod
    for art in articulos:
        Costo_unit_cf_por_art[art] = round(((cuota_cf*mod_por_art[art])/cantidades[art]),2)
    print(f'El costo unitario de cf por producto en este caso es de:\n{Costo_unit_cf_por_art}')


    
    
    



