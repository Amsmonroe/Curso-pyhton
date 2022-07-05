"""Hacer un programa para obtener una ficha con los siguientes datos, ademas de dar el tipo de dato que maneja"""

#OBTENER NOMBRE
nombre=input("ingresa tu nombre:")
print("Tu nombre es " + nombre) #para tipo de dato str se usa +
print("El tipo de dato es:", type(nombre))

#OBTENER NUMERO DE TELEFONO
tel=input("ingresa tu número de telefono:") #recordar que input devuelve el tipo cadena asi que necesitamos CASTEAR
casteo1=int(tel)
print("Tu numero de telefono es" , casteo1) #cuando es tipo de dato numerico se usa la ","
print("el tipo de dato es", type(casteo1))

#OBTENER DIRECCIÓN 
direc=input("ingresa tu dirección:")
print("Tu direccion es " + direc)
print("El tipo de dato es:", type(direc))

#OBTENER EDAD
edad=input("ingresa tu edad:") #recordar que input devuelve el tipo cadena asi que necesitamos CASTEAR
casteo2=int(edad)
print("Tu edad es" , casteo2) #cuando es tipo de dato numerico se usa la ","
print("el tipo de dato es", type(casteo2))

#OBTENER NACIONALIDAD
lidad=input("ingresa tu nacionalidad:")
print("Tu nacionalidad es " + lidad)
print("El tipo de dato es:", type(lidad))

#OBTENER FECHA NAC
dia=input("ingresa el dia de nacimiento con 2 digitos:")
mes=input("ingresa tu mes de nacimiento con 2 digitos:")
año=input("ingresa tu año de nacimiento con 2 digitos:")
fecha="Su fecha de nacimiento es el {}/{}/{}" #uso de plantillas
fecha_nac=fecha.format(dia,mes,año)
print(fecha_nac)
tipos=int(dia+mes+año)
print("el tipo de dato es", type(tipos))

#OBTENER ALTURA
alt=input("ingresa tu altura en metros:") #recordar que input devuelve el tipo cadena asi que necesitamos CASTEAR
casteo4=float(alt)
print("Tu Altura es" , casteo4 , "metros") #cuando es tipo de dato numerico se usa la ","
print("el tipo de dato es", type(casteo4))

#OBTENER PESO
peso=input("ingresa tu peso en kilos:") #recordar que input devuelve el tipo cadena asi que necesitamos CASTEAR
casteo5=float(peso)
print("Tu peso es" , casteo5 , "kg") #cuando es tipo de dato numerico se usa la ","
print("el tipo de dato es", type(casteo5))