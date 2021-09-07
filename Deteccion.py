from DatosPruebaA import *

y1=0  #Declaracion de Sinapsis Neurona1
y2=0  #Declaracion de Sinapsis Neurona2
y3=0  #Declaracion de Sinapsis Neurona3
y4=0  #Declaracion de Sinapsis Neurona4

for i in range(len(E)):
    for j in range(len(E[i])):
        y1+=WN1[i][j]*E[i][j]  #Sinapsis Neurona1
        y2+=WN2[i][j]*E[i][j]  #Sinapsis Neurona2
        y3+=WN3[i][j]*E[i][j]  #Sinapsis Neurona3
        y4+=WN4[i][j]*E[i][j]  #Sinapsis Neurona4
        
ys1=1/(1+e**(-y1))  #Salida de Función de activación Neurona1
ys2=1/(1+e**(-y2))  #Salida de Función de activación Neurona2
ys3=1/(1+e**(-y3))  #Salida de Función de activación Neurona3
ys4=1/(1+e**(-y4))  #Salida de Función de activación Neurona4
ysvh=[ys1,ys2,ys3,ys4]  #Vector con salidas de Neuronas

yf=0  #Declaracion de Sinapsis NeuronaFinal
for i in range(len(WNF)):
    yf+=ysvh[i]*WNF[i]  #Sinapsis NeuronaFinal

ysf=1/(1+e**(-yf))  #Salida de Función de activación NeuronaFinal


print("F")