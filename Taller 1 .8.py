#punto 8
s : float
s = float(input(" Insertar la frecuencia deseada: ")) 

if s < 3e9:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de radio" )
elif s < 3e12:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de microondas" )
elif s  < 4.3e14:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de infrrarrojo" )
elif s < 7.5e14:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de luz visible" )

elif s < 3e17:
    print("La frecuencia " + str(s) + " esta ubicada en ondas ultravioletas" )

elif s < 3e19:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de Rayos X" )
        
else:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de rayos gamma" )