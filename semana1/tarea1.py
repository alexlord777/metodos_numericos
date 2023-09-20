import matplotlib.pyplot as plt

x=list()
y=list()
n=-10


for i in range(0,201):
    x.append(n+ 0.1*i)

for i in x:
    z= (3*(i)**4) - (2*(i)**3) + (18*(i)**2) - (11*i) + 4
    y.append(z)


# Crear el gráfico de líneas
plt.plot(x, y)

# Agregar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Líneas')

# Mostrar el gráfico
plt.show()