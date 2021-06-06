import math

x = math.pi/3
exp = 1
seno = 0
compara = 1
i = 1

while math.fabs(compara - seno) > 0.001:
    compara = seno
    if i % 2 == 0:
        seno -= (x ** exp) / math.factorial(exp)
    else:
        seno += (x ** exp) / math.factorial(exp)
    exp += 2
    i += 1

print("El seno de pi/3 es: ", seno)
