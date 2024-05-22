print("Hello, World")
import math
rkruznice=input("R kružnice:")
hema=int(rkruznice)
pi=math.pi
def obsahkruhu(hema):
    vysledek=(math.pi*hema*hema)
    return vysledek
print("Obvod kružnice je",obsahkruhu(hema),"cm")