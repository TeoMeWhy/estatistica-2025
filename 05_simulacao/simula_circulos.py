import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dist(x, y, raio):
    dist = np.sqrt((x - raio) ** 2 + (y - raio)**2)
    return dist


def calc_area(r, size=100):
    x = np.random.uniform(0, 2*r, size=size)
    y = np.random.uniform(0, 2*r, size=size)
    
    df = pd.DataFrame({"x": x, "y":y})
    df['dist'] = df.apply(lambda row: dist(row['x'], row['y'], r), axis=1)
    df['flIN'] = df['dist'] < r
    
    area_quadrado = (2 * r) ** 2
    return area_quadrado * df['flIN'].mean()

r = float(input("Entre com o tamanho do raio: "))

sizes = [
    10, 20, 30, 50, 70, 80, 90, 100,
    150, 200, 250,400, 500, 1000,
    1500, 2000, 3000,5000,
    10000,15000, 30000, 50000,
    ]

dfs = []
for s in sizes:
    results = [calc_area(r=r, size=s) for i in range(20)]
    df = pd.DataFrame({"result":results})
    df["size"] = s
    dfs.append(df)

# %%
 
df_consolidado = pd.concat(dfs)
df_groupby = df_consolidado.groupby('size').agg({"result":["mean", "std"]}).reset_index()
df_groupby.columns = ["size", "mean", "std"]
df_groupby
# %%

plt.plot(df_groupby['size'], df_groupby['mean'])

plt.fill_between(df_groupby['size'],
                 df_groupby['mean']+df_groupby['std'],
                 df_groupby['mean']-df_groupby['std'],
                 alpha=0.3)
plt.grid()
plt.show()
# %%
