from DatosPruebaA import *
# Letra=B
for i in range(len(Letra)):
        for j in range(len(Letra[i])):
            print("Introduzca el valor de la casilla ",i+1,j+1)
            Letra[i][j]=input()
            
for k in range(4):
    y1=0  #Declaracion de Sinapsis Neurona1
    y2=0  #Declaracion de Sinapsis Neurona2
    y3=0  #Declaracion de Sinapsis Neurona3
    y4=0  #Declaracion de Sinapsis Neurona4

    for i in range(len(Letra)):
        for j in range(len(Letra[i])):
            y1+=WN1[k][i][j]*Letra[i][j]  #Sinapsis Neurona1
            y2+=WN2[k][i][j]*Letra[i][j]  #Sinapsis Neurona2
            y3+=WN3[k][i][j]*[i][j]  #Sinapsis Neurona3
            y4+=WN4[k][i][j]*Letra[i][j]  #Sinapsis Neurona4
            
    ys1=1/(1+e**(-y1))  #Salida de Función de activación Neurona1
    ys2=1/(1+e**(-y2))  #Salida de Función de activación Neurona2
    ys3=1/(1+e**(-y3))  #Salida de Función de activación Neurona3
    ys4=1/(1+e**(-y4))  #Salida de Función de activación Neurona4
    ysvh=[ys1,ys2,ys3,ys4]  #Vector con salidas de Neuronas

    yf=0  #Declaracion de Sinapsis NeuronaFinal
    for i in range(len(WNF[k])):
        yf+=ysvh[i]*WNF[k][i]  #Sinapsis NeuronaFinal

    ysf[3-k]=1/(1+e**(-yf))  #Salida de Función de activación NeuronaFinal

print(ysf)
print("F")