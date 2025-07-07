from math import cos, sin, tan, radians

angulo = float(input('digite o valor de um angulo qualquer: '))
angulo = radians(angulo)
cos = cos(angulo)
sen = sin(angulo)
tan = tan(angulo)

print('Dado o angulo {:.2f}, seu seno é {:.2f}, seu coseno e {:.2f} e sua tangente é {:.2f}'.format(angulo, sen, cos, tan))