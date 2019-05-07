import sys              #IMPORTA EL MODULO SYS, PARA UTILIZAR SYS.EXIT 


# -------------BLOQUE DE DEFINICIÓN------------

#DEFINICION FUNCIONES

#FUNCION QUE CREA UNA MATRIZ A PARTIR DE LA INFORMACION CONTENIDA EN UN FICHERO
def laberintoMatriz(laberinto):
                 
    L=[]                                #LISTA VACIA DONDE SE ALMACENARA EL LABERINTO EN FORMATO DE MATRIZ              
    col=0                               #VARIABLE QUE ALMACENARÁ LA CANTIDAD DE COLUMNAS DE LA MATRIZ              
    fil=0                               #VARIABLE QUE ALMACENARÁ LA CANTIDAD DE FILAS DE LA MATRIZ

    #CREACIÓN DE LA MATRIZ
    for lineas in laberinto:            #CICLO FOR QUE RECORRE CADA UNA DE LAS LINEAS CONTENIDAS EN LA VARIABLE LABERINTO (LABERINTO TIPO LISTA DE STRINGS)     
        fil=fil+1                       #AUMENTA EN 1 LA CANTIDAD DE LA VARIABLE FIL POR CADA LINEA DE TEXTO
       
    for x in lineas[:-1]:               #CICLO FOR QUE RECCORE CADA POSICIÓN (MENOS LA ULTIMA POSICIÓN[:-1]) DE LA ULTIMA LINEA DE VARIABLE LABERINTO                  
        col=col+1                       #AUMENTA EN 1 LA CANTIDAD DE LA VARIABLE COL POR CADA POSICIÓN EN LA LINEA           

        
    for i in range(fil):                #CICLO FOR QUE SE REPITIRÁ SEGUN LA CANTIDAD QUE TENGA LA VARIABLE FIL           
	    L.append([0] * col)         #AGREGA UNA LISTA EN LA ULTIMA POSICIÓN DE LA LISTA L        

    #LLENADO DE LA MATRIZ    
    laberinto=open("laberinto.txt","r") #ALMACENA EN LA VARIABLE LABERINTO LA INFORMACIÓN CONTENIDA EN EL FICHERO, PUESTO QUE ESTA SE VACIÓ ANTERIORMENTE
    j=0
    k=0                                 #VARIABLES J Y K CORRESPONDEN A LA POSICIÓN DENTRO DE LA MATRIZ, SUS VALORES IRÁN AUMENTANDO EN EL CICLO FOR
    
    for lineas in laberinto:            #CICLO FOR QUE RECORRE LINEA POR LINEA DE LA VARIABLE LABERINTO                 
        k=0                             #ASIGNA EL VALOR 0 A K, CADA VEZ QUE SE INICIA EL CICLO  
        for x in lineas[:-1]:           #CICLO FOR DENTRO DEL CICLO MENCIONADO ANTERIORMENTE QUE RECORRE CADA POSICIÓN ( X ) DE LA LINEA
            L[j][k]=x                   #ALMACENA EN LA POSICIÓN (J,K) DE LA MATRIZ L EL VALOR DEL ELEMENTO X
            k=k+1                       #AUMENTA EN 1 EL VALOR DE K POR CADA ELEMENTO RECORRIDO 
        j=j+1                           #AUMENTA EN 1 EL VALOR DE J CADA VEZ QUE TERMINE UN CICLO DE LINEA DE LABERINTO
        
    #SALIDA DE LA FUNCIÓN MATRIZ()
    return (L)                          #RETORNA LA MATRIZ CREADA Y LLENADA


#FUNCIÓN QUE ENCUENTRA LA ENTRADA AL LABERINTO, RECIBE EL LABERINTO COMO MATRIZ Y RETORNA UNA LISTA CON LA DIRECCIÓN DE LA ENTRADA
def entrada(L):                         
    ent=[0,0]                           #CREA LA LISTA ENT, QUE TIENE DOS ELEMENTOS
    fil = len(L)                        #ALMACENA EN LA VARIABLE FIL, LA CANTIDAD DE ELEMENTOS(LISTAS) DENTRO DE LA LISTA L
    col = len(L[0])                     #ALMACENA EN LA ARIABLE COL, LA CANTIDAD DE ELEMENTOS DENTRO LA PRIMERA LISTA DE LA LISTA L

    for j in range(fil):                #CICLO FOR QUE SE REPITE SEGÚN CANTIDAD QUE ESTE ALMACENADA EN LA VARIABLE FIL, AUMENTA EN 1 LA VARIABLE J
         for k in range(col):           #CICLO FOR QUE SE REPITE SEGUN LA CANTIDAD QUE ESTÉ ALMACENADA EN LA VARIABLE COL, AUMENTA EN 1 LA VARIABLE K
             if L[j][k]=="E":           #SI LA POSICIÓN (J,K) DE LA MATRIZ L ES EL CARACTER E,EJECUTA LO SIGUIENTE...
                ent[0]=j                #ALMACENA EN LA POSICIÓN 0 DE LA LISTA, EL VALOR DE J
                ent[1]=k                #ALMACENA EN LA POSICIÓN 1 DE LA LISTA  EL VALOR DE K
    return ent                          #RETORNA LA LISTA QUE CONTIENE LA POSICIÓN DE LA ENTRADA AL LABERINTO

#FUNCION QUE ENCUENTRA LA POSICIÓN DE SALIDA DEL LABERINTO, RETORNA UNA LISTA CON LA DIRECCION DE ESTA
def salida(L):
    fil = len(L)                        #ALMACENA EN LA VARIABLE FIL, LA CANTIDAD DE ELEMENTOS(LISTAS) DENTRO DE LA LISTA L
    col = len(L[0])                     #ALMACENA EN LA ARIABLE COL, LA CANTIDAD DE ELEMENTOS DENTRO LA PRIMERA LISTA DE LA LISTA L
    sal=[0,0]                           #CREA LA LISTA ENT, QUE TIENE DOS ELEMENTOS
    for j in range(fil):                #CICLO FOR QUE SE REPITE SEGÚN CANTIDAD QUE ESTE ALMACENADA EN LA VARIABLE FIL, AUMENTA EN 1 LA VARIABLE J
         for k in range(col):           #CICLO FOR QUE SE REPITE SEGUN LA CANTIDAD QUE ESTÉ ALMACENADA EN LA VARIABLE COL, AUMENTA EN 1 LA VARIABLE K
             if L[j][k]=="S":           #SI LA POSICIÓN (J,K) DE LA MATRIZ L ES EL CARACTER S,EJECUTA LO SIGUIENTE...
                sal[0]=j                #ALMACENA EN LA POSICIÓN 0 DE LA LISTA, EL VALOR DE J
                sal[1]=k                #ALMACENA EN LA POSICIÓN 1 DE LA LISTA  EL VALOR DE K
        
    return sal                          #RETORNA LA LISTA QUE CONTIENE LA POSICIÓN DE LA ENTRADA AL LABERINTO



#FUNCION RECURSIVA QUE ENCUENTRA EL CAMINO DE LA ENTRADA A LA SALIDA DEL LABERINTO
#ENTRA LA MATRIZ LABERINTO, UNA LISTA CON LA POSICIÓN DE ENTRADA(POSICIÓN ACTUAL), Y UNA LISTA CON LA POSICIÓN DE SALIDA
#RETORNA UNA MATRIZ CON EL LABERINTO Y EL CAMINO DE ENTRADA A SALIDA(SI ESQUE HAY), SI ESQUE NO HAY, IMPRIME EL MENSAJE "NO HAY SOLUCIÓN" Y SALE DE LA FUNCIÓN

def  resolverLaberinto(L,ent,sal):

    #PASO 1, BUSCA SI A LA DERECHA, IZQUIERDA, ABAJO O ARRIBA DE LA POSICIÓN ACTUAL(ent[0][1]) SE ENCUENTRA LA SALIDA,SI ES ASI, RETORNA LA MATRIZ CREADA
    if(ent[0]+1==sal[0] and ent[1] ==sal[1]):  #SI AL SUMAR UNO A LA POSICIÓN ENT[O](ES DECIR A LA DERECHA), ESTA LA SALIDA, REALIZA LO SIGUIENTE... 
        print ("Algoritmo finalizado, se ha encontrado el camino")   #IMPRIME UN MENSAJE DE AVISO QUE SE ENCONTRÓ EL CAMINO
        ImprimirMatriz(SolucionFinal(L))                             #MUESTRA POR PANTALLA LA MATRIZ CON LA SOLUCIÓN DEL LABERINTO
        llenarfichero(SolucionFinal(L))
        sys.exit()                                                   #SALE DE LA FUNCIÓN
    if(ent[0]-1==sal[0] and ent[1] ==sal[1]):  #SI AL RESTAR UNO A LA POSICIÓN ENT[O](ES DECIR A LA IZQUIERDA), ESTA LA SALIDA, REALIZA LO SIGUIENTE... 
        print ("Algoritmo finalizado, se ha encontrado el camino")   #IMPRIME UN MENSAJE DE AVISO QUE SE ENCONTRÓ EL CAMINO
        ImprimirMatriz(SolucionFinal(L))                             #MUESTRA POR PANTALLA LA MATRIZ CON LA SOLUCIÓN DEL LABERINTO
        llenarfichero(SolucionFinal(L))
        sys.exit()                                                   #SALE DE LA FUNCIÓN                                                   #SALE DE LA FUNCIÓN
    if(ent[0]==sal[0] and ent[1]+1 ==sal[1]):  #SI AL SUMAR UNO A LA POSICIÓN ENT[1](ES DECIR HACIA ABAJO) ESTA LA SALIDA, REALIZA LO SIGUIENTE
        print ("Algoritmo finalizado, se ha encontrado el camino")   #IMPRIME UN MENSAJE DE AVISO QUE SE ENCONTRÓ EL CAMINO
        ImprimirMatriz(SolucionFinal(L))                             #MUESTRA POR PANTALLA LA MATRIZ CON LA SOLUCIÓN DEL LABERINTO
        llenarfichero(SolucionFinal(L))
        sys.exit()                                                   #SALE DE LA FUNCIÓN 
        
    if(ent[0]==sal[0] and ent[1]-1 ==sal[1]):   #SI AL RESTAR UNO A LA POSICIÓN ENT[1](ES DECIR HACIA ARRIBA) ESTA LA SALIDA, REALIZA LO SIGUIENTE
        print ("Algoritmo finalizado, se ha encontrado el camino")   #IMPRIME UN MENSAJE DE AVISO QUE SE ENCONTRÓ EL CAMINO
        ImprimirMatriz(SolucionFinal(L))                             #MUESTRA POR PANTALLA LA MATRIZ CON LA SOLUCIÓN DEL LABERINTO
        llenarfichero(SolucionFinal(L))
        sys.exit()                                                   #SALE DE LA FUNCIÓN
        
    #PASO 2, EN EL CASO DE QUE NO SE CUMPLA NINGUNA DE LOS OPERADORES ANTERIORES, PASA A ESTE PASO EN EL CUAL SE REALIZA UN MOVIMIENTO A UN ESPACIO VACÍO
    if(L[ent[0]+1][ent[1]]==" "):    #SI A LA DERECHA DE LA POSICIÓN ACTUAL HAY UN ESPACIO VACÍO, REALIZA LO SIGUIENTE...
        L[ent[0]+1][ent[1]]="+"      #ALMACENA EN LA POSICIÓN DE LA DERECHA, EL SIGNO "+"
        ent[0]=ent[0]+1              #SE POSICIONA EN LA DERECHA, SUMANDO 1 EL VALOR DE LA POSICIÓN ent[0]
        resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION RESOLVERLABERINTO, PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO ,ESTO SE LLAMA RECURSIVIDAD
                
    if(L[ent[0]-1][ent[1]]==" "):    #SI A LA IZQUIERDA DE LA POSICIÓN ACTUAL HAY UN ESPACIO VACÍO, REALIZA LO SIGUIENTE...
        L[ent[0]-1][ent[1]]="+"      #ALMACENA EN LA POSICIÓN DE LA IZQUIERDA, EL SIGNO "+"
        ent[0]=ent[0]-1              #SE POSICIONA EN LA IZQUIERDA, RESTANDO 1 AL VALOR DE LA POSICIÓN ent[0]
        resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION RESOLVERLABERINTO, PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO,ESTO SE LLAMA RECURSIVIDAD
                
    if(L[ent[0]][ent[1]+1]==" "):    #SI ABAJO DE LA POSICIÓN ACTUAL HAY UN ESPACIO VACÍO, REALIZA LO SIGUIENTE...
        L[ent[0]][ent[1]+1]="+"      #ALMACENA EN LA POSICIÓN DE ABAJO EL SIGNO "+"
        ent[1]=ent[1]+1              #SE POSICIONA ABAJO, SUMANDO 1 AL VALOR DE LA POSICIÓN ent[1]
        resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION RESOLVERLABERINTO, PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO,ESTO SE LLAMA RECURSIVIDAD
                
    if(L[ent[0]][ent[1]-1]==" "):    #SI ARRIBA DE LA POSICIÓN ACTUAL HAY UN ESPACIO VACÍO, REALIZA LO SIGUIENTE...
        L[ent[0]][ent[1]-1]="+"      #ALMACENA EN LA POSICIÓN DE ARRIBA EL SIGNO "+"
        ent[1]=ent[1]-1              #SE POSICIONA ARRIBA, RESTANDO 1 AL VALOR DE LA POSICIÓN ent[1]
        resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION RESOLVERLABERINTO, PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO,ESTO SE LLAMA RECURSIVIDAD

   #PASO 3(BACKTRACKING), EN EL CASO DE QUE NO SE CUMPLA LO ANTERIOR(ES DECIR, SE QUEDA SIN CAMINO Y SIN LA SALIDA A SU ALREDEDOR, MARCA LA POSICIÓN Y SE DEVUELVE
    
    else:
        L[ent[0]][ent[1]]="-"       # MARCA LA POSICIÓN CON EL SIGNO "-"

        #BUSCA A SUS ALREDEDORES UNA POSICIÓN POR LA CUAL PASÓ ANTERIORMENTE
        if(L[ent[0]-1][ent[1]]=="+"):            #BUSCA A LA IZQUIERDA SI HAY UN SIGNO + REGISTRADO, SI LO HAY REALIZA LO SIGUIENTE
                    ent[0]=ent[0]-1              #SE POSICIONA A LA IZQUIERDA RESTANDO 1 A LA POSICIÓN ent[0] 
                    resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION , PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO       (RECURSIVIDAD)
        if(L[ent[0]+1][ent[1]]=="+"):            #BUSCA A LA DERECHA SI HAY UN SIGNO + REGISTRADO, SI LO HAY REALIZA LO SIGUIENTE...
                    ent[0]=ent[0]+1              #SE POSICIONA A LA IZQUIERDA SUMANDO 1 A LA POSICIÓN ent[0]
                    resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION, PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO        (RECURSIVIDAD)
        if(L[ent[0]][ent[1]+1]=="+"):            #BUSCA ABAJO SI HAY UN SIGNO + REGISTRADO, SI LO HAY REALIZA LO SIGUIENTE...
                    ent[1]=ent[1]+1              #SE POSICIONA ABAJO SUMAND 1 A LA POSICIÓN ent[1]
                    resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE LA FUNCION, PERO CON EL VALOR DE POSICIÓN (ENT) ASIGNADO        (RECURSIVIDAD)
        if(L[ent[0]][ent[1]-1]=="+"):            #BUSCA ARRIBA SI HAY UN SIGNO + REGISTRADO, SI LO HAY REALIZA LO SIGUIENTE...
                    ent[1]=ent[1]-1              #SE POSICIONA ARRIBA SUMANDO 1 A LA POSICIÓN ent[1]
                    resolverLaberinto(L,ent,sal) #EJECUTA NUEVAMENTE L AFUNCION, PERO CON EL VALOR DE POSICION (ENT) ASIGNADO        (RECURSIVIDAD)
                    
    #EN EL CASO DE QUE NO SE CUMPLA NADA DE LO ANTERIOR, EL PROGRAMA REALIZA LO SIGUIENTE
        print ("Laberinto sin salida")        #IMPRIME EL MENSAJE "LABERINTO SIN SALIDA
        sys.exit()                              #SALE DE LA FUNCIÓN
        
#FUNCION QUE RECIBE UNA MATRIZ Y LA IMPRIME POR PANTALLA
def ImprimirMatriz(L):
    fil = len(L)                                #CREA LA VARIABLE FIL, LA CUAL CONTIENE EL NUMERO DE ELEMENTOS QUE TENGA LA LISTA L 
    col = len(L[0])                             #CREA LA VARIABLE COL,LA CUAL CONTIENE EL NUMERO DE ELEMENTOS DE LA PRIMERA LISTA DE LA LISTA L
                                                #OPERADOR LEN(LISTA) CUENTA LA CANTIDAD DE ELEMENTOS QUE HAY EN UNA LISTA
    for j in range(col):                        #CICLO FOR QUE SE EJECUTA SEGUN EL VALOR DE LA VARIABLE COL
        print("")                               #IMPRIME UN SALTO DE LINEA AL INGRESAR AL CICLO
        for k in range(col):                    #CICLO FOR DENTRO DEL CICLO ANTERIOR SE REPITE DE SEGUN EL VALOR DE LA VARIABLE COL
            print (L[j][k]),                    #MUESTRA POR PANTALLA EL ELEMENTO L[J][K] SIN SALTO DE LINEA (VALORES J-K AUMENTAN EN 1 CADA VEZ QUE SE REPITE EL FOR)
            
    print("")                                   #IMPRIME UN SALTO DE LINEA, ANTES DE SALIR DE FINALIZAR LA FUNCION
    
#FUNCION QUE RECIBE UNA MATRIZ, Y LA ALMACENA EN UN FICHERO
def llenarfichero(L):
    manejador=open("solucion.txt","w")
    row = len(L)
    col = len(L[0])
    for j in range(row):
        manejador.write("\n")
        for k in range(col):
             a=L[j][k]
             manejador.write("-")
             manejador.write(a)
def SolucionFinal(L):
    row = len(L)
    col = len(L[0])
    for j in range(row):
        for k in range(col):
            if(L[j][k]=="-"):
                L[j][k]=" "
    return L
    


                    #BLOQUE PRINCIPAL
#-----------------------------------------------------------

             
print("--PROGRAMA SOLUCIÓN A UN LABERINTO PREDETERMINADO DE CUALQUIER DIMENSIÓN--")
print(" ")
print(" ")

#ENTRADA
             
laberinto=open("laberinto.txt","r")
laberintoMatriz=laberintoMatriz(laberinto)
print("Laberinto Original")
ImprimirMatriz(laberintoMatriz)

print("")
print("")
#ARGUMENTOS DE LAS FUNCIONES

salida=salida(laberintoMatriz)                    #POSICION EN LA QUE SE ENCUENTRA LA SALIDA(POSICIÓN EN MATRIZ)

entrada=entrada(laberintoMatriz)                  #POSICIÓN EN LA QUE SE ENCUENTRA LA ENTRADA(POSICIÓN EN MATRIZ)


resolverLaberinto(laberintoMatriz,entrada,salida) #EJECUTA LA FUNCION QUE ENCUENTRA LA SALIDA CON LOS ARGUMENTOS OBTENIDOS ANTERIORMENTE






                
