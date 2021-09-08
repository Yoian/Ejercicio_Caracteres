from Datos_Entrenamiento import *
Generacion=0
brk=1
while brk:
    Generacion+=1
    for Letra in range(len(Letras)):  #Cada iteracion cambia las entradas de las letras
    #for it in range(iteraciones): len(Letras)
        y1=0  #Declaracion de Sinapsis Neurona1
        y2=0  #Declaracion de Sinapsis Neurona2
        y3=0  #Declaracion de Sinapsis Neurona3
        y4=0  #Declaracion de Sinapsis Neurona4

        for i in range(len(Letras[Letra])):
            for j in range(len(Letras[Letra][i])):
                y1+=WN1[i][j]*Letras[Letra][i][j]  #Sinapsis Neurona1
                y2+=WN2[i][j]*Letras[Letra][i][j]  #Sinapsis Neurona2
                y3+=WN3[i][j]*Letras[Letra][i][j]  #Sinapsis Neurona3
                y4+=WN4[i][j]*Letras[Letra][i][j]  #Sinapsis Neurona4
                
        ys1=1/(1+e**(-y1))  #Salida de Función de activación Neurona1
        ys2=1/(1+e**(-y2))  #Salida de Función de activación Neurona2
        ys3=1/(1+e**(-y3))  #Salida de Función de activación Neurona3
        ys4=1/(1+e**(-y4))  #Salida de Función de activación Neurona4
        ysvh=[ys1,ys2,ys3,ys4]  #Vector con salidas de Neuronas

        yf=0  #Declaracion de Sinapsis NeuronaFinal
        for i in range(len(WNF)):
            yf+=ysvh[i]*WNF[i]  #Sinapsis NeuronaFinal

        ysf=1/(1+e**(-yf))  #Salida de Función de activación NeuronaFinal

        DC=ysf*(1-ysf)*(Tk1[Letra]-ysf)  #Calcular el error de salida con respecto al esperado 

        for Nh in range(len(ysvh)):  #Cada iteracion cambia cada neurona oculta que vamos a ocupar
            DH=ysvh[Nh]*(1-ysvh[Nh])*(WNF[Nh]*DC)#Calcular el error de salida de la neurona oculta a analizar
            for i in range(len(Letras[Letra])):
                for j in range(len(Letras[Letra][i])):
                    WNH[Nh][i][j]=WNH[Nh][i][j]+(alpha*Letras[Letra][i][j]*DH)  #Se reajustan los pesos de las dentritas a la capa oculta

        for i in range(len(WNF)):
            WNF[i]=WNF[i]+(alpha*ysvh[i]*DC)  #Se reajustan los pesos de los axones entre las neuronas ocultas y la neurona final

        cde[Letra]=(((Tk1[Letra]-ysf)**2)/2)  #Se calcula el error con la función de coste 
        
    for i in range(len(Letras)):
        if cde[i]<0.00005:  #condición para comprobar el error de cada letra
            brk=0
        else:
            brk=1
            break


print("F")