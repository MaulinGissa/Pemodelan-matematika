import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definisikan parameter untuk model matematika
r = 0.13243  # Laju pertumbuhan keuntungan Indekos Tanjungsari
s = 0.19901   # Laju pertumbuhan keuntungan Indekos BPI
a = 5.619*10**(-8)  # Laju laju kompetisi indekos Tanjungsari 
b = 2.804*10**(-8)  # Laju laju kompetisi indekos BPI 
alpha = 15  #juta # keuntungan maksimum indekos Tanjungsari
beta = 11   #juta # keuntungan maksimum indekos BPI

# Definisikan fungsi yang mendeskripsikan sistem ODE
def lotka_volterra(y, t, r, a, s, b, alpha, beta):
    X, Y = y
    dydt = [r * X * (1 - (X/alpha)) - a * X * Y,
            s * Y * (1 - (Y/beta)) - b * Y * X]
    return dydt

# Kondisi awal
y0 = [10, 9] #juta

# Waktu di mana solusi harus dihitung
t = np.linspace(0, 10, 500)

# Panggil odeint untuk menyelesaikan sistem ODE
sol = odeint(lotka_volterra, y0, t, args=(r, a, s, b, alpha, beta))

# Ekstrak solusi untuk X dan Y
X = sol[:, 0]
Y = sol[:, 1]

# Cetak hasil angkanya
print("Waktu\tKeuntungan TS\t\tKeuntungan BPI")
for i in range(len(t)):
    print(f"{t[i]:.2f}\t{X[i]:.2f}\t{Y[i]:.2f}")

# Plot hasilnya
plt.figure(figsize=(10, 5))
plt.plot(t, X, label='Indekos Tanjung Sari')
plt.plot(t, Y, label='Indekos BPI')
plt.xlabel('Waktu')
plt.ylabel('Keuntungan')
plt.title('Grafik Keuntungan Terhadap Persaingan Usaha Indekos Tanjungsari dengan BPI')
plt.legend()
plt.grid()
plt.show()
