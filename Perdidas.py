# Code made for Sergio Andrés Díaz Ariza
# 11 November 2021
# License MIT
# Operaciones Movimiento: Straight line Lost Friction

import numpy as np

Q = 2.777778e-4 #[m^3/s] Caudal
D = 0.1022604 # [m] Diametro interno
D_in = 4.026 #[inch]
Area = (np.pi*(D**2))/4
miu_cin = 1e-5 #[m^2/s]
e = 4.5e-5 #micrometros Rugosidad abssoluta e/D

v = Q/Area
Re = D*v/miu_cin

#f_d = (-2 * np.log(((e / D) / 3.71) - (5.02 / Re) * np.log(((e / D) / 3.71) + (14.05 / Re)))) ** (-2)
f_d = 64/Re

#f = 1.375e-3*(1+(20000*(e/D))+(10e6/Re))**(1/3)

f = f_d/4

## Perdidas por Friccion en Tuberia
l = 11 #[m]
g = 9.81 #[m/s^2]

h_f = (l*(v**2)*f_d)/(D*2*g)

## Perdidas locales
# Valvula 100% Abierta K1 = 1500 K_inf =
K1_val = 1500
Kinf_val = 4.0

K_val = (K1_val/Re) + (Kinf_val*(1+(1/D_in)))
h_val = K_val*((v**2)/(2*g))

# T de flujo
K1_T = 200
Kinf_T = 0.10

K_T = (K1_T/Re) + (Kinf_T*(1+(1/D_in)))
h_T = K_T*((v**2)/(2*g))

# Codo
K1_elb = 800
Kinf_elb = 0.40

K_elb = K1_elb/Re + Kinf_elb*(1+(1/D_in))
h_elb = K_elb*((v**2)/(2*g))

# Check in
K1_chek = 2000
Kinf_chek = 10.00

K_chek = K1_chek/Re + Kinf_chek*(1+(1/D_in))
h_chek = K_chek*((v**2)/(2*g))


###################### PERDIDAS EN FILTRO ############################
Vol = Q*3600 #Volumen hallado a partir del caudal
A_filtro = 3 #[m^2]
uW_2K = 4.5 #[atm*h/m^2]

Delta_P = ((Vol/A_filtro)**2) * uW_2K
h_fil = Delta_P*10.2
h_atm = 10.33


print("Reynolds:",Re)
print("Velocity",v)
print("friction Darcy:",f_d)
print("perdidas tuberia:",h_f*100)
print("K valvula abierta:",K_val)
print("perdidas valvula:",h_val)
print("K division T:",K_T)
print("Perdidas divisioin T:",h_T)
print("K codo 90:",K_elb)
print("Perdidas codo 90:",h_elb)
print("K check:",K_chek)
print("Perdidas chek:",h_chek)

print('Perdidas Filtro:', Delta_P)
print(h_fil)
print("Perdidas totales :",(h_chek+h_val+2*h_elb+h_f+h_fil+h_atm))