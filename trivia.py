puntos=0
nombre=input("ingrese nombre ")
print(f" HOLA ,{nombre} vamos a jugar una trivia")
primera=input("Cual es el valor mas proximo de pi? A: 3     B: 3,14     C: 3,141592      D: 2,7")
if (primera=="C" or primera=="c"):
    puntos+=1
segunda=input("Cual es una palabra reservada en Python? A: scanf     B: print     C: pinMode      D: noTone")
if (segunda=="B" or segunda=="b"):
    puntos+=1
tercero=input("Que estructura sirve para repetir ciclos indefinidamente? A: while   B: for      C:if    D: input")
if (tercero=="A" or tercero=="a"):
    puntos+=1