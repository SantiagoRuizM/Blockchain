# python conditionals 

import numpy as np

def plc_sensor():
    print("¡Evacuen!")
    
volumen_represa = np.random.randint(10,600)

if volumen_represa>=0 and volumen_represa<=250:
    print(f'el nivel de agua es muy bajo: {volumen_represa}')
elif volumen_represa>250 and volumen_represa<=450:
    print(f'el nivel del agua es optimo: {volumen_represa}')    
elif volumen_represa>450:
    print(f'el nivel del agua es muy alto: {volumen_represa}')    
    plc_sensor()   

