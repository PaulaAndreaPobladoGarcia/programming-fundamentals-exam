voltaje1 = float (input(" ingrese el primer voltaje: "))
voltaje2 =float (input(" ingrese el segundo voltaje: "))
voltaje3 =float (input(" ingrese el tercer voltaje: "))
VoltajeTotal = (voltaje1 + voltaje2+ voltaje3) /3
 
if VoltajeTotal > 220:
     print(F"!PELIGRO¡") 
elif VoltajeTotal >= 116:
     print(F"alto voltaje")
     print(f"{VoltajeTotal}")
else: 
      print(F"Voltaje corecto")
      print(f"{VoltajeTotal}")