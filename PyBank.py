import os
import csv

conteo = 0
tprofit = 0
valores,fechas = [],[]
path = 'D://OneDrive//Documentos//DataAnalitycs//Tareas//3//budget_data.csv'

with open(path, mode="r") as archivo:
    cabecera = next(archivo)
    leer = csv.reader(archivo, delimiter=',')
    conteo = sum(1 for row in leer)

with open(path, mode="r") as archivo:
    leer = csv.reader(archivo, delimiter=',')
    cabecera = next(archivo)
    for row in leer:
        tprofit += int(row[1])

cambio = []
neto = []
with open(path, mode="r") as archivo:
    leer = csv.reader(archivo, delimiter=',')
    cabecera = next(archivo)
    for row in leer:
        valores.append(int(row[1]))
        fechas.append(row[0])
    antes = int(valores[0])
    for cambio in valores:
        listanueva =  int(cambio) - int(antes)
        antes = cambio
        neto = neto + [listanueva]

conteo2 = 0
conteo2 = (sum(1 for elemento in neto))-1
suma = 0
for elementos in neto:
    suma = elementos + suma
promedio = suma / conteo2

valmax = max(neto)
valmin = min(neto)
bvalmax = neto.index(valmax)
bvalmin = neto.index(valmin)
fechamax = fechas[bvalmax]
fechamin = fechas[bvalmin]

escribir = open("Analisis.txt","a")
escribir.write('Financial Analysis\n----------------------------\nTotal Months: '+str(conteo)+'\nTotal: '+str(tprofit)+'\nAverage  Change: '+str(promedio)+'\nGreatest Increase in Profits: '+str(fechamax)+' ('+str(valmax)+')'+'\nGreatest Decrease in Profits: '+str(fechamin)+' ('+str(valmin)+')')
escribir.close()