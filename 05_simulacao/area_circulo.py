# %%
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def dist(x, y, raio):
    dist = np.sqrt((x - raio) ** 2 + (y - raio)**2)
    return dist

# %%

r = float(input("Entre com um tamanho de raio: "))
size = int(input("Entre com o tamanho da amostra: "))

# %%




x = np.random.uniform(0, 2*r, size=size)
y = np.random.uniform(0, 2*r, size=size)

df = pd.DataFrame({"x": x, "y":y})
df['dist'] = df.apply(lambda row: dist(row['x'], row['y'], r), axis=1)
df['flIN'] = df['dist'] < r

df_in = df[df["flIN"]]
df_out = df[~df["flIN"]]


area_quadrado = (2 * r) ** 2
print("Área Quadrado:", area_quadrado)

area_circulo = area_quadrado * df['flIN'].mean()
print("Área do Cículo:",area_circulo)

print("Área real do Cículo:", np.pi * (r **2))


fig, ax = plt.subplots()
plt.hlines(0, xmax=2*r, xmin=0)
plt.hlines(2*r, xmax=2*r, xmin=0)
plt.vlines(0, ymax=2*r, ymin=0)
plt.vlines(2*r, ymax=2*r, ymin=0)

c = Circle([r,r],radius=r)
ax.add_patch(c)

plt.plot(df_in['x'], df_in['y'], 'o', color='green')
plt.plot(df_out['x'], df_out['y'], 'o', color='tomato')
plt.title(f"Área estimada: {area_circulo:.2f} | Área real: {np.pi * (r **2):.2f}")
plt.show()