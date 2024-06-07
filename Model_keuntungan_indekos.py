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
def keuntungan(y, t, r, a, s, b, alpha, beta):
    X, Y = y
    dydt = [r * X * (1 - (X/alpha)) - a * X * Y,
            s * Y * (1 - (Y/beta)) - b * Y * X]
    return dydt

# Kondisi awal
y0 = [40, 70] #juta

# Waktu di mana solusi harus dihitung
t = np.linspace(0, 30, 500)

# Panggil odeint untuk menyelesaikan sistem ODE
sol = odeint(keuntungan, y0, t, args=(r, a, s, b, alpha, beta))

# Ekstrak solusi untuk X dan Y
X = sol[:, 0] # mengambil semua baris dari kolom pertama
Y = sol[:, 1] # mengambil semua baris dari kolom kedua

# Plot hasilnya
plt.figure(figsize=(10, 5))
plt.plot(t, X, label='Indekos Tanjung Sari')
plt.plot(t, Y, label='Indekos BPI')
plt.xlabel('Waktu dalam satuan tahun')
plt.ylabel('Keuntungan dalam satuan juta')
plt.title('Grafik Keuntungan Terhadap Persaingan Usaha Indekos Tanjungsari dengan BPI')
plt.legend()
plt.grid(True)
plt.show()

print(50*"=")
# Temukan indeks yang paling dekat dengan t disekitar n
t_target = 00
index1 = (np.abs(t - t_target)).argmin()
t_target = 10
index2 = (np.abs(t - t_target)).argmin()
t_target = 15
index3 = (np.abs(t - t_target)).argmin()
t_target = 20
index4 = (np.abs(t - t_target)).argmin()
t_target = 25
index5 = (np.abs(t - t_target)).argmin()
t_target6 = 30
index6 = (np.abs(t - t_target6)).argmin()


# Dapatkan hasil keuntungan ketika t = n
keuntungan_TS1 = X[index1]
keuntungan_BPI1 = Y[index1]
keuntungan_TS2 = X[index2]
keuntungan_BPI2 = Y[index2]
keuntungan_TS3 = X[index3]
keuntungan_BPI3= Y[index3]
keuntungan_TS4 = X[index4]
keuntungan_BPI4= Y[index4]
keuntungan_TS5 = X[index5]
keuntungan_BPI5= Y[index5]
keuntungan_TS6 = X[index6]
keuntungan_BPI6= Y[index6]

# Cetak hasilnya
print("Waktu\tKeuntungan TS\tKeuntungan BPI")
print(f"{t[index1]:.0f}\t{keuntungan_TS1:.2f}\t\t{keuntungan_BPI1:.2f} ")
print(f"{t[index2]:.0f}\t{keuntungan_TS2:.2f}\t\t{keuntungan_BPI2:.2f} ")
print(f"{t[index3]:.0f}\t{keuntungan_TS3:.2f}\t\t{keuntungan_BPI3:.2f} ")
print(f"{t[index4]:.0f}\t{keuntungan_TS4:.2f}\t\t{keuntungan_BPI4:.2f} ")
print(f"{t[index5]:.0f}\t{keuntungan_TS5:.2f}\t\t{keuntungan_BPI5:.2f} ")
print(f"{t[index6]:.0f}\t{keuntungan_TS6:.2f}\t\t{keuntungan_BPI6:.2f} ")

# kasus nomor 3
print(50*"=")
t_target7 = 4
index7 = (np.abs(t - t_target7)).argmin()
keuntungan_BPI7= Y[index7]
keuntungan_TS7 = X[index7]
print(f"{t[index7]:.0f}\t{keuntungan_TS7:.2f}\t\t{keuntungan_BPI7:.2f} ")
