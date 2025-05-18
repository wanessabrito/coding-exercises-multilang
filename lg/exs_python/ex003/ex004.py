import math

def volume_esfera(raio):
  v =  ((4*math.pi)/3) * (raio**3)
  return v

raio = float(input('Digite o raio da esfera: '))

volume = volume_esfera(raio)
print('O volume da esfera é',round(volume))



