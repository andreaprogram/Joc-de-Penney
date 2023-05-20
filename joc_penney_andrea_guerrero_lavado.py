# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:32:00 2023

@author: andre
"""

import random

estrategia_jugador_A = [0, 0, 0]
estrategia_jugador_B = [0, 0, 0]

with open("guanys.txt", "w") as archivo:
    for l in range(2):
        estrategia_jugador_A[0] = l
        for m in range(2):
            estrategia_jugador_A[1] = m
            for z in range(2):
                estrategia_jugador_A[2] = z

                for i in range(2):
                    estrategia_jugador_B[0] = i
                    for j in range(2):
                        estrategia_jugador_B[1] = j
                        for k in range(2):
                            estrategia_jugador_B[2] = k

                            if estrategia_jugador_A != estrategia_jugador_B:
                                secuenciaA = []
                                secuenciaB = []

                                for componente in estrategia_jugador_A:
                                    if componente == 1:
                                        secuenciaA.append("C")
                                    else:
                                        secuenciaA.append("X")
                                        
                                apuestaA = "-".join(secuenciaA)

                                for componente in estrategia_jugador_B:
                                    if componente == 1:
                                        secuenciaB.append("C")
                                    else:
                                        secuenciaB.append("X")
                                        
                                apuestaB = "-".join(secuenciaB)

                                victoriasA = 0
                                victoriasB = 0
                                num_partidas = 10000

                                for partida in range(1, 10001):
                                    while True:
                                        secuencia_tiradas = []

                                        for i in range(0, 1000000):
                                            moneda = random.randint(0, 1)
                                            if moneda == 1:
                                                secuencia_tiradas.append("C")
                                            else:
                                                secuencia_tiradas.append("X")

                                            resultado = "-".join(secuencia_tiradas)

                                            if apuestaA in resultado or apuestaB in resultado:
                                                break

                                        if apuestaA in resultado:
                                            victoriasA += 1
                                            break
                                        elif apuestaB in resultado:
                                            victoriasB += 1
                                            break

                                prob_victoriaB = victoriasB / num_partidas
                                guany_estrategia = prob_victoriaB * (+1) + (1 - prob_victoriaB) * (-1)
                                guany_estrategia_aprox = "{:.2f}".format(guany_estrategia)
                                cadena = str(apuestaA) + " " + str(apuestaB) + " " + str(guany_estrategia_aprox)
                                archivo.write(cadena + "\n")