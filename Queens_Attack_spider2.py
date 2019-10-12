# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:47:07 2019

@author: Jhon Garcia Garcia
"""

import numpy as np

#Leemos todas las entradas
n, k=input(">Length of the boards sides / Number of obstacles: ").split()
n=int(n); k=int(k)
#n=int(input("Length of the boards sides :"))  ;   k=int(input("Number of obstacles: "))
#r_q=int(input("Queen's row: "))            ;     c_q=int(input("Queen's column: "))
r_q, c_q=input(">Queen's row / Queen's column: ").split()
r_q=int(r_q) ; c_q=int(c_q)

r_i=np.zeros(k)
c_i=np.zeros(k)

for i in range(k): 
    r_i[i], c_i[i]= input(">Row and Column of Obstacle "+ str(i+1) + " :").split()
    
if n>0 and ((r_q and c_q) <= n) and k>= 0:
    
    #Entradas para las posiciones de cada uno de los obstaculos
    #  r_i[i] : vector de No. fila del obstaculo [i]
    #  c_i[i] : vector de No. columna del obstaculo [i]
    

    
    #Primero calculamos todas los posibles ataques de la reina y posteriormente se restan las posiciones bloqueadas
        
    # Se realiza el analisis del problema y se nota que los ataques horizontales y
    # verticales de la reina siempre tendra el mismo valor, sin importar la posicion de la reina 
    
    a_hv=(n-1)*2 #suma de ataques horizontales y verticales
    
    # CÁLCULO DE ATAQUES DIAGONALES SIN OBSTACULOS
       
       # los ataques diagonales poseen 4 direcciones : 
       # ↗ a_sd: ataque Superior derecho
       # ↖ a_si: ataque Superior izquierdo
       # ↘ a_id: ataque inferior derecho
       # ↙ a_ii: ataque inferior izquierdo
       
       # Por otro lado todos los ataques diagonales poseen dos componentes: horiz. y vertical,
       # y el numero de ataques diagonal en cada dirección sera igual a la componente menor.
    
    p1=n-r_q # componente Ver. superior 
    p2=n-c_q # componente Hor. derecho
    a_sd=min(p1,p2)
       
    
    p1= n-r_q # componente vertical superior
    p2= c_q-1 # componente horiz. izquierdo
    a_si=min(p1,p2)
    
    p1= n-c_q # componente horinzontal derecho
    p2= r_q-1 # componente vertical inferior
    a_id=min(p1,p2)
    
    p1=c_q-1 # componente horinzontal  izquierdo
    p2=r_q-1 # componente vertical izquierdo
    a_ii=min(p1,p2)
    
    # Hasta aqui ya conocemos la cantidad de ataques en todas las direcciones, sin obstaculos
    # Solo basta hacer una sumatoria de todos estos valores y así sabremos la cantidad total de ataques sin obstaculos.
    
    q_a= a_hv + a_sd + a_si + a_id + a_ii # cantidad de ataques libres
 #   print(q_a)
        
        
# RESTANDO LAS POSICIONES DE ATAQUE BLOQUEADAS
    #Obstaculos ubicados en la misma fila o columna de la reina
    # r_o : resta acumulativa de posiciones obstaculizadas en cada direccion, en total son 8 direcciones
    # state_i : vector que indica si un obstaculo fue procesado(1) o no(0). 
    resta=np.zeros(8) 
    state_i=np.zeros(k)
    #print("i="+str(i))
    for i in range(k) :       

        # para obstaculos ubicados a la izquierda de la reina
        if (r_i[i]==r_q) and (c_i[i]<c_q) :           
            aux=c_q - c_i[i]+1
            resta[0] = aux  if aux>resta[0] else resta[0]
         
            
        # para obstaculos ubicados a la Derecha de la reina    
        if (r_i[i]==r_q) and (c_i[i]>c_q) : 
            aux= n-c_i[i]+1
            resta[1] = aux if aux>resta[1] else resta[1]
        
        # para obstaculos ubicados en la parte superior de la reina
        if (c_i[i]==c_q) and (r_i[i]>r_q) : 
            aux= n-r_i[i]+1
            resta[2]= aux if aux>resta[2] else resta[2]
            
        # para obstaculos ubicados en la parte inferior de la reina    
        if (c_i[i]==c_q) and (r_i[i]<r_q) : 
            resta[3]= r_i[i] if aux >resta[3] else resta[3]
   
    # CÁLCULO PARA OBSTACULOS EN LAS DIAGONALES DE LA REINA
        
        # id: Para obstaculos en la diagonal inferior derecha
        if  (r_q - r_i[i]) > 0 and (c_q - c_i[i])<0 and (r_q - r_i[i])==(c_q-c_i[i])*-1: 
           p1=n-c_i[i]+1
           p2= r_i[i]
           #resta[4]= p1 + 1 if p1<p2 else p2 +1
           if (p1<p2) and p1>resta[4]:
               resta[4]=p1
           elif p2<p1 and p2>resta[4]:
               resta[4]=p2
           elif p1==p2 and p1>resta[4]:
               resta[4]=p1
          
           
        # sd: Para obstaculos en la diagonal superior derecha
        if (r_q - r_i[i])==(c_q-c_i[i]) and (c_q-c_i[i])<0 : 
           p1=n-r_i[i]+1
           p2=n-c_i[i]+1
           
           if(p1<p2) and p1>resta[5]:
               resta[5]=p1
           elif (p1>p2) and p2>resta[5]:
               resta[5]=p2
           elif p1==p2 and p1>resta[5]:
               resta[5]=p1
          
           
        # ii: Para obstaculos en la diagonal inferior izquierda
        if (r_q - r_i[i])==(c_q-c_i[i]) and (c_q-c_i[i])>0 : 
           p1=r_i[i]
           p2=c_i[i]
           
           if p1<p2 and p1>resta[6]:
              resta[6]=p1
           elif p2<p1 and p2>resta[6]:
              resta[6]=p2
           elif p1==p2 and p1>resta[6]:
              resta[6]=p1
              
        
        # si: Para obstaculos en la diagonal superior izquierda
        if (r_q - r_i[i])<0 and (c_q - c_i[i])>0 and (r_q-r_i[i] == (c_q-c_i[i])*-1):  
           p1=c_i[i]
           p2=n-r_i[i]+1
           
           if p1<p2 and p1>resta[7]:
              resta[7]=p1
           elif p2<p1 and p2>resta[7]:
              resta[7]=p2
           elif p1==p2 and p1>resta[7]:
              resta[7]=p1
                       
    print("The number of squares that the queen can attack from position (" + str(r_q)+", " + str(c_q)+" ) es: "+str(q_a-sum(resta)))
               
elif n<=0:
    print("Por favor, vuelva a ejecutar e ingrese un valor valido para el tablero")

elif n>0 and (r_q or c_q)>n:
    print("Posición invalida para la reina, vuelva a ejecutar con valores ")

elif k > (n*n)-1 :
    print("Demasiados obstaculos para la cantidad del tablero, vuelva a ejecutar")    

elif (type(n) or type(k) or type(r_q) or type(c_q)) != int:
    print("Ha ingresado uno o mas valores que no son enteros, vuelva a intentar")