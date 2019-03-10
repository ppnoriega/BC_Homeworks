import os
import csv

conteo = 0
candidato, idv = [], []
path = 'D://OneDrive//Documentos//DataAnalitycs//Tareas//3//election_data.csv'
conteokhan = 0
conteocorrey = 0
conteoli = 0
conteoo = 0
porcentajekhan = 0
porcentajecorrey = 0
porcentajeli = 0
porcentajeo = 0

with open(path, mode="r") as archivo:
    cabecera = next(archivo)
    leer = csv.reader(archivo, delimiter=',')
    conteo = sum(1 for row in leer)
print(conteo)

with open(path, mode="r") as archivo:
    cabecera = next(archivo)
    leer = csv.reader(archivo, delimiter=',')
    for row in leer:
        candidato.append(row[2])
        idv.append(str(row[0]))

for element in candidato:
    if element == "Khan":
        conteokhan = conteokhan + 1
    if element == "Correy":
        conteocorrey = conteocorrey + 1
    if element == "Li":
        conteoli = conteoli + 1
    if element == "O'Tooley":
        conteoo = conteoo +1

porcentajekhan = conteokhan / conteo
porcentajecorrey = conteocorrey / conteo
porcentajeli = conteoli / conteo
porcentajeo = conteoo / conteo

if porcentajekhan>porcentajecorrey and porcentajekhan>porcentajeli and porcentajekhan>porcentajeo:
    ganador = "Khan"
if porcentajecorrey>porcentajekhan and porcentajecorrey>porcentajeli and porcentajecorrey>porcentajeo:
    ganador = "Correy"
if porcentajeli>porcentajekhan and porcentajeli>porcentajecorrey and porcentajeli>porcentajeo:
    ganador = "Eli"
if porcentajeo>porcentajekhan and porcentajeo>porcentajecorrey and porcentajeo>porcentajeli:
    ganador = "O'Tooley"

escribir = open("Election Results.txt","a")
escribir.write('Election Results\n----------------------------\nTotal Votes: '+str(conteo)+'\n----------------------------\nKhan: '+"{:.2%}".format(porcentajekhan)+' ('+str(conteokhan)+')\nCorrey: '+"{:.2%}".format(porcentajecorrey)+' ('+str(conteocorrey)+')\nEli: '+"{:.2%}".format(porcentajeli)+' ('+str(conteoli)+')\nOTooley: '+"{:.2%}".format(porcentajeo)+' ('+str(conteoo)+')\n----------------------------\nWinner: '+str(ganador)+'\n----------------------------')
escribir.close()