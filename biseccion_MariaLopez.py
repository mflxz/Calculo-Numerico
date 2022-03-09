"""        Universidad de Oriente
	        Nucleo Nueva Esparta
	Escuela de Ingenieria y Ciencias Aplicadas
        Licenciatura en Informática
		    Cálculo Numérico 

        Proyecto: Algoritmo de Bisección

        Alumna: María López V- 27.182.207
"""


from math import *

def f(x):
    return 4-x**2-x**3 #Definición de la función 

def biseccion(a, b, Er, Ni):

    """ a: Límite inferior
	b: Límite superior
	Er: Error relativo
	Ni: Número de iteraciones
    """

    Ea=100 #Error aproximado relativo
    i=0    #Iteraciones
    MA=0
    MP=0
    
    print ('Método de Bisección')

    if (f(a)*f(b) > 0):
        print("La funcion no cambia de signo")
         
    while ((i<Ni) and (Ea>Er)): 
        MP = MA
        MA = (a+b)/2
        if (f(MA)*f(b)<0): #cambia de signo en el intervalo
            a= MA
        else:
            b= MA
        if (i>0):
            Ea= abs((MA-MP)/MA)*100

        print ('El intérvalo es [',a,',',b,']') #Se encarga de mostrar los intervalos
        i = i+1

    print ('Numero de iteraciones:',i,'\nAproximación =',MA, '\nError de:' ,Ea)

biseccion(1,4,1,100) #Aquí se colocan los parámetros de la función ( Límite Inferior , Limite Superior , Error relativo , Número de iteraciones )
