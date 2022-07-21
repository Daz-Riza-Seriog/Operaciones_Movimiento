# Code made for Sergio Andrés Díaz Ariza
# 11 November 2021
# License MIT
# Operaciones Movimiento: Straight line Lost Friction

import numpy as np

# Parametros
l = 1780  # longitud de la linea [m]
D = 6  # Diametro de la linea [m]
v = 3  # Velocidad media del fluido [m^2/s^2]
g = 9.81  # Gravedad [m/s^2]

# Calculo de f-Regimen Laminar Re<2000
Rey = 0.7  # Numero de Reynolds

f = 16 / Rey
# f_d = 64/Rey

# Calculo de f-Regimen Turbulento Re>2000

f_d = (-2 * np.log(((e / D) / 3.71) - (5.02 / Rey) * np.log((e / D) / 3.71) - (14.05 / Rey))) ** (-2)

h_f = 4 * ((l * (v ** 2) * f) / (D * 2 * g))  # [J/Kg]
# h_f =  * (l * (v ** 2) * f_d) / (D * 2 * g)  # [J/Kg]

# En terminos de caida de presion
Deltha_P = 5.65
rho = 1.18
h_f_ = Deltha_P / rho
