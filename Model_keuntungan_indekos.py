import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definisikan parameter untuk model matematika
r = 0.13243  # Laju pertumbuhan keuntungan Indekos Tanjungsari
s = 0.19901   # Laju pertumbuhan keuntungan Indekos BPI
a = 5.619*10**(-8)  # Laju laju kompetisi indekos Tanjungsari 
b = 2.804*10**(-8)  # Laju laju kompetisi indekos BPI 
alpha = 70  #juta # keuntungan maksimum indekos Tanjungsari
beta = 102   #juta # keuntungan maksimum indekos BPI

# Definisikan fungsi yang mendeskripsikan sistem ODE
def indekos(y, t, r, a, s, b, alpha, beta):
    X, Y = y
    dydt = [r * X * (1 - (X/alpha)) - a * X * Y,
            s * Y * (1 - (Y/beta)) - b * Y * X]
    return dydt

# Kondisi awal
y0 = [40, 70] #juta

# Waktu di mana solusi harus dihitung
t = np.linspace(0, 50, 500)

# Panggil odeint untuk menyelesaikan sistem ODE
sol = odeint(indekos, y0, t, args=(r, a, s, b, alpha, beta))

# Ekstrak solusi untuk X dan Y
X = sol[:, 0]
Y = sol[:, 1]

# Cetak hasil angkanya
print("Waktu\tKeuntungan TS\tKeuntungan BPI")
for i in range(len(t)):
    print(f"{t[i]:.2f}\t{X[i]:.2f}\t\t{Y[i]:.2f}")

# Plot hasilnya
plt.figure(figsize=(10, 5))
plt.plot(t, X, label='Indekos Tanjungsari')
plt.plot(t, Y, label='Indekos BPI')
plt.xlabel('Waktu dalam satuan tahun')
plt.ylabel('Keuntungan dalam satuan juta')
plt.title('Grafik Keuntungan Terhadap Persaingan Usaha Indekos Tanjungsari dengan BPI')
plt.legend()
plt.grid(True)
plt.show()
