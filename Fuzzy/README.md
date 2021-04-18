Nama : Nur Hanifah Amatullah
NPM  : 1184086
Kelas: D4 Teknik Informatika 3B

Program dibawah ini menggunakan algoritma fuzzy sugeno yang digunakan untuk merekrut karyawan baru pada suatu perusahaan. Logika fuzzy merupakan metodologi sistem kontrol untuk memecahan permasalahan.
Perekrutan ini didasarkan pada 3 hal yaitu nilai: wawancara, psikotes,dan tpa.
Apabila,ketiganya memenuhi kriteria maka output dari program ini yaitu lulus,menunggu panggilan atau tidak lulus.
sebelum program dijalankan terlebih dahulu kita melakukan import library numpy,skfuzzy,dan matplotlib.pyplot
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

outputnya:
Derajat Keanggotaan Nilai wawancara
Sedang : 0.7000000000000002
Tinggi : 0.2999999999999998

Derajat Keanggotaan Nilai psikotes
Sedang : 0.8
Tinggi : 0.2

Derajat Keanggotaan Nilai tpa
Rendah : 0.8666666666666667
Sedang : 0.4
Matriks Nilai wawancara
[0.0, 0.7000000000000002, 0.2999999999999998]

Matriks Nilai psikotes
[0.0, 0.8, 0.2]
Matriks Nilai tpa
[0.8666666666666667, 0.4, 0.0]
Index Kelayakan Diterima  : 60.71428571428571
Waiting List : 78.57 %
Lulus : 21.43 %

Kesimpulan:
Jadi,hasil dari program ini dengan algoritma fuzzy sugeno melalui index yaitu yang layak diterima baik itu menunggu ataupun lulus panggilan sebanyak 60.71428571428571
Jika di jabarkan lebih lanjut hasil yang lulus perekrutan sebanyak 21.43 %, sedangkan yang menunggu panggilang sebanyak 78.57 %

