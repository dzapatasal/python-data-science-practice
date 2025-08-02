import numpy as np

# URL del archivo raw de un Gist
github_path = 'https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv'

# Lectura de dataframe
df = np.loadtxt(github_path, delimiter=',',skiprows=1, usecols=np.arange(1,6))

# Verificacion de cantidad de dimensiones
print(df.shape)