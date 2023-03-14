#punto 10

#d es distancia en metros 
d : float
d = float(input("Inserte la distancia que quiere estudiar en metros: " ))
#Tiempo que tarda la luz en recorrer la distancia 
td = float
#Tiempo que tarda el sonido en recorrer la distancia 
ts = float
#Tiempo que tarda Usain Bolt en recorrer la distancia 
tb = float
#Tiempo que tarda el auto en recorrer la distancia 
ta = float
#constantes expresadas en metros por segundo 
VEL_LUZ = 299792458
VEL_SONIDO = 343 
VEL_BOLT = 11.6666
VEL_AUTO = 126.466
td = d/VEL_LUZ
print("El tiempo que tarda la luz en reccorrer " + str(d) + " m es de " + str(td) + " segundos")

ts = d/VEL_SONIDO
print("El tiempo que tarda el sonido en reccorrer " + str(d) + " m es de " + str(td) + " segundos")

tb = d/VEL_BOLT
print("El tiempo que tarda Usain Bolt en reccorrer " + str(d) + " m es de " + str(td) + " segundos")

ta = d/VEL_AUTO
print("El tiempo que tarda el auto en reccorrer " + str(d) + " m es de " + str(td) + " segundos")