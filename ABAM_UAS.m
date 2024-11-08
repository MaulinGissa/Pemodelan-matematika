clc;
clear;

% Parameter Lotka-Volterra
alpha = 0.505594;
beta = 0.209412;
myu = 0.319288;
delta = 0.411330;
k1 = 3600;  % Kapasitas maksimum Calya
k2 = 2800;  % Kapasitas maksimum Sigra

% Parameter simulasi
t0 = 0;        % Waktu awal (bulan)
tf = 100;      % Waktu akhir (bulan)
h = 0.01;      % Langkah waktu
t = t0:h:tf;   % Vektor waktu
x = zeros(size(t)); % Penjualan Calya
y = zeros(size(t)); % Penjualan Sigra

% Kondisi awal
x(1) = 1318;   % Penjualan awal Calya
y(1) = 823;    % Penjualan awal Sigra

% Fungsi untuk sistem persamaan Lotka-Volterra
f1 = @(x,y) alpha*x*(1-(x/k1)+((myu*y)/k2));
f2 = @(x,y) beta*x*(1-(y/k2)+((delta*x)/k1));

% Runge-Kutta 4 untuk tiga langkah awal
for i = 1:3
    k1_x = h * f1(x(i), y(i));
    k1_y = h * f2(x(i), y(i));
    
    k2_x = h * f1(x(i) + h/2, y(i) + k1_x/2);
    k2_y = h * f2(x(i) + h/2, y(i) + k1_y/2);
    
    k3_x = h * f1(x(i) + h/2, y(i) + k2_x/2);
    k3_y = h * f2(x(i) + h/2, y(i) + k2_y/2);
    
    k4_x = h * f1(x(i) + h, y(i) + k3_x);
    k4_y = h * f2(x(i) + h, y(i) + k3_y);
    
    x(i+1) = x(i) + (1/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x);
    y(i+1) = y(i) + (1/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y);
end

% Adams-Bashforth-Moulton (ABM) untuk langkah selanjutnya
for i = 4:length(t)-1
    % Adams-Bashforth (Prediksi)
    x_pred = x(i) + (h/24) * (55*f1(x(i), y(i)) - 59*f1(x(i-1), y(i-1)) + 37*f1(x(i-2), y(i-2)) - 9*f1(x(i-3), y(i-3)));
    y_pred = y(i) + (h/24) * (55*f2(x(i), y(i)) - 59*f2(x(i-1), y(i-1)) + 37*f2(x(i-2), y(i-2)) - 9*f2(x(i-3), y(i-3)));
    
    % Adams-Moulton (Koreksi)
    x(i+1) = x(i) + (h/24) * (9*f1(x(i), x_pred) + 19*f1(x(i), y(i)) - 5*f1(x(i-1), y(i-1)) + f1(x(i-2), y(i-2)));
    y(i+1) = y(i) + (h/24) * (9*f2(x(i), y_pred) + 19*f2(x(i), y(i)) - 5*f2(x(i-1), y(i-1)) + f2(x(i-2), y(i-2)));
end

% Tampilkan hasil dalam bentuk tabel
disp('--------------------------------------------------------')
fprintf('\tt\t\tApproximate x\t\tApproximate y\n')
disp('--------------------------------------------------------')
fprintf('\t%.1f\t\t%.6f\t\t%.6f\n',[t',x',y'])
disp('--------------------------------------------------------')

% Plot Hasil
figure;
plot(t, x, 'linewidth', 2); hold on;
plot(t, y, 'r-', 'linewidth', 2);
grid on;
xlabel('Waktu (bulan)');
ylabel('Jumlah Penjualan');
title('Simulasi Penjualan Calya dan Sigra (Metode Adams-Bashforth-Moulton)');
legend('Calya', 'Sigra');


% Cari waktu stabilisasi (perbedaan penjualan kecil)
threshold = 1e-4;  % Toleransi perubahan kecil
stable_time = NaN; % Inisialisasi variabel waktu stabil

for i = 2:length(t)
    if abs(x(i) - x(i-1)) < threshold && abs(y(i) - y(i-1)) < threshold
        stable_time = t(i);
        break;
    end
end

% Tampilkan waktu stabilisasi
if ~isnan(stable_time)
    fprintf('\nWaktu stabilisasi ditemukan pada t = %.2f bulan\n', stable_time);
    index = round(stable_time / h) + 1; % Konversi waktu ke indeks
    fprintf('Jumlah penjualan pada waktu stabilisasi:\n');
    fprintf('Calya: %.2f\n', x(index));
    fprintf('Sigra: %.2f\n', y(index));
else
    disp('Tidak ditemukan waktu stabilisasi dalam interval waktu simulasi.');
end