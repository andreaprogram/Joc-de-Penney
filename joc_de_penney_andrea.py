# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:36:09 2023

@author: andre
"""

  
import random


#1º ESTRATEGIAS JUGADORES
#Definimos una estrategia para cada jugador y hacemos que imprima su estrategia
#no estudiaremos las estrategias iguales, solo las desiguales

estrategia_jugador_A=[0,0,0]
estrategia_jugador_B=[0,0,0]

for l in range(2):
  

    estrategia_jugador_A[0]=l
    for m in range(2):
        estrategia_jugador_A[1]=m
        for z in range(2):
            estrategia_jugador_A[2]=z
            
            for i in range(2):
                estrategia_jugador_B[0]=i
                for j in range(2):
                    estrategia_jugador_B[1]=j
                    for k in range(2):
                        estrategia_jugador_B[2]=k  
                        
                        if estrategia_jugador_A != estrategia_jugador_B:
                            secuenciaA=[]
                            secuenciaB=[]
                            
                            
                            
                            #print(estrategia_jugador_A, estrategia_jugador_B)
                            
                            for componente in estrategia_jugador_A:
                               
                                if componente==1:
                                    secuenciaA.append("C")
                                else:
                                    secuenciaA.append("X")
                                    
                            apuestaA = "-".join(secuenciaA)

                            for componente in estrategia_jugador_B:
                                if componente==1:
                                    secuenciaB.append("C")
                                else:
                                    secuenciaB.append("X")
                                    
                            apuestaB = "-".join(secuenciaB)
                            

                            #print("Estrategia jugador A "+ str(apuestaA)+ " // Estrategia jugador B "+ str(apuestaB))

                            # 2º ACUMULACION DE PUNTOS Y SISTEMA DEL JUEGO DE PENNEY

                            #Aqui hacemos que, para el numero de jugadas deseado, se imprima la secuencia obtenida del estilo C-C-X-...
                            #hay que tirar la moneda hasta que aparezca la secuencia de uno de los jugadores

                            #también definimos los puntos de cada uno, para que se haga un recuento tras unas cuantas jugadas 
                            #y diga el ganador total

                            #Inerpretamos la moneda como un num aleatorio, donde 1=CARA 0=CRUZ
                            victoriasA=0
                            victoriasB=0
                            num_partidas=10000

                            #Simulamos que se hacen 10000 juegos para ver cómo se acumulan los puntos
                            for partida in range(1,10001):
                               
                                while True:
                                    secuencia_tiradas=[]
                                
                            #Hacemos que el prgrama identifique el patron de una de las dos estrategias dentro de la secuencia de tiradas
                            #si se encuentra alguna de las dos apuestas, dejamos de tirar la moneda

                                    for i in range(0,1000000):
                                        moneda = random.randint(0,1)
                                        if moneda == 1:
                                            secuencia_tiradas.append("C")
                                        else:
                                            secuencia_tiradas.append("X")
                                        
                                        resultado = "-".join(secuencia_tiradas)

                                        if apuestaA in resultado or apuestaB in resultado:
                                            break
                                    #print("Secuencia de tiradas:", resultado) 
                                
                                    if apuestaA in resultado:
                                        #print("Jugador A gana la jugada",partida)
                                        victoriasA+=1
                                        break
                                    elif apuestaB in resultado:
                                        #print("Jugador B gana la jugada",partida)
                                        victoriasB+=1
                                        break
                                
                            #print("Las victorias de A en 10000 partidas son", victoriasA)
                            #print("Las victorias de B en 10000 partidas son", victoriasB)

                            #if victoriasA>victoriasB:
                                #print("A gana el juego")
                            #if victoriasB>victoriasA:
                               # print("B gana el juego")
                            #if victoriasA==victoriasB:
                                #print("Empate")

                            prob_victoriaB = victoriasB/num_partidas  
                            guany_estrategia = prob_victoriaB*(+1) + (1-prob_victoriaB)*(-1)
                            guany_estrategia_aprox="{:.2f}".format(guany_estrategia)  
                            #print("La probabilidad de que B con la estrategia", apuestaB, "gane a A con la estrategia", apuestaA, "es", prob_victoriaB_aprox)
                            print(apuestaA, apuestaB, guany_estrategia_aprox)















