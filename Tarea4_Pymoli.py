import os
import pandas

#Leer el archivo CSV
os.chdir ('D:\\OneDrive\\Documentos\\DataAnalitycs\\Tareas\\4\\')
df = pandas.read_csv('purchase_data.csv')

#Para contar el total de usuarios
usuarios = list(df.SN)
Validacion = set()
for x in usuarios:
    if x not in Validacion:
        Validacion.add(x)
totalusuarios = len(Validacion)

#Para contar el numero unico de items
items = list(df.ItemID)
Validacion2 = set()
for x in items:
    if x not in Validacion2:
        Validacion2.add(x)
totalitems = len(Validacion2)

#Promedio del precio
promedio = df["Price"].mean()

#Total de compras
compras = list(df.PurchaseID)
totalcompras = len(compras)

#Total de ingresos
ingresos = df['Price'].sum()

#Total en genero
totalgenero = len(list(df.Gender))

#Total de hombres
hombres = list(df.Gender)
totalhombres = 0
for x in hombres:
    if x == "Male":
        totalhombres = totalhombres + 1
porcentajehombres = totalhombres/totalgenero

#Total de mujeres
mujeres = list(df.Gender)
totalmujeres = 0
for x in mujeres:
    if x == "Female":
        totalmujeres = totalmujeres + 1
porcentajemujeres = totalmujeres/totalgenero

#Tota de otros
otros = list(df.Gender)
totalotros = 0
for x in otros:
    if x == "Other / Non-Disclosed":
        totalotros = totalotros + 1
porcentajeotros = totalotros/totalgenero

#Analisis de compra
operacionesgender = {
    'PurchaseID' : 'count',
    'Price' : ['mean','sum']
}
Opergender = df.groupby('Gender').agg(operacionesgender)

#Más gastadores
operacionesgast = {
    'PurchaseID' : 'count',
    'Price' : ['mean','sum']
}
Opergast = df.groupby(by=['SN']).agg(operacionesgast)

#Items populares
operacionespopu = {
    'ItemID' : 'count',
    'Price' : ['mean','sum']
}
Operpopu = df.groupby(by=['ItemName']).agg(operacionespopu)

#Items ingresos
operacionesing = {
    'ItemID' : 'count',
    'Price' : ['mean','sum']
}
Opering = df.groupby(by=['ItemName']).agg(operacionesing)

print ("Total de usuarios: ",len(usuarios))
print ("Total de usuarios no repetidos: ",totalusuarios)
print ("El total de items es: ",totalitems)
print ("El promedio es: $",promedio)
print ("El total de compras es de: ", totalcompras)
print ("Los ingresos fueron por: $",ingresos)
print ("El total de hombres es de: ","{:.2%}".format(porcentajehombres)," (",totalhombres,")")
print ("El total de mujeres es de: ","{:.2%}".format(porcentajemujeres)," (",totalmujeres,")")
print ("El total de otros es de: ","{:.2%}".format(porcentajeotros)," (",totalotros,")")
print (Opergender.sort_values(('PurchaseID','count'),ascending=False).head(5))
print (Opergast.sort_values(('Price','sum'),ascending=False).head(5))
print (Operpopu.sort_values(('ItemID','count'),ascending=False).head(5))
print (Opering.sort_values(('Price','sum'),ascending=False).head(5))