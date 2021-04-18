# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:31:27 2021

@author: User
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
#%%
# Generate semua variabel
# * Kualitas dan layanan pada rentang subjektif [0, 10]
# * Tip memiliki rentang [0, 25] dalam satuan poin persentase
x_wawancara = np.arange(0, 5, 1)
x_psikotes = np.arange(350, 630, 1)
x_tpa  = np.arange(0, 750, 1)
#%%
# Generate fuzzy membership functions
wawancara_rendah = fuzz.trapmf(x_wawancara,[0, 0.5, 1, 2])
wawancara_sedang = fuzz.trapmf(x_wawancara,[1, 2, 3, 4])
wawancara_tinggi = fuzz.trapmf(x_wawancara,[3, 4, 4, 4.5])

psikotes_rendah = fuzz.trapmf(x_psikotes,[0, 350, 400, 480])
psikotes_sedang = fuzz.trimf(x_psikotes,[400, 480, 530])
psikotes_tinggi = fuzz.trapmf(x_psikotes,[480, 530, 600, 630])

tpa_rendah = fuzz.trapmf(x_tpa,[0, 0, 300, 450])
tpa_sedang = fuzz.trapmf(x_tpa,[300, 350, 650, 750])
tpa_tinggi = fuzz.trapmf(x_tpa,[650, 680, 700, 750])

R = 20
S = 50
T = 100
#%%
# Visualize these universes and membership functions//membuat visualisasi grafik
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 10))

ax0.plot(x_wawancara, wawancara_rendah, 'b', linewidth=1.5, label='Rendah')
ax0.plot(x_wawancara, wawancara_sedang, 'g', linewidth=1.5, label='Sedang')
ax0.plot(x_wawancara, wawancara_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax0.set_title('Index Nilai wawancara')
ax0.legend()

ax1.plot(x_psikotes, psikotes_rendah, 'b', linewidth=1.5, label='Rendah')
ax1.plot(x_psikotes, psikotes_sedang, 'g', linewidth=1.5, label='Sedang')
ax1.plot(x_psikotes, psikotes_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax1.set_title('Index Nilai psikotes')
ax1.legend()

ax2.plot(x_tpa, tpa_rendah, 'b', linewidth=1.5, label='Rendah')
ax2.plot(x_tpa, tpa_sedang, 'g', linewidth=1.5, label='Sedang')
ax2.plot(x_tpa, tpa_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax2.set_title('Index Nilai tpa')
ax2.legend()

ax3.plot([3, 3],[0, T], 'b', linewidth=1.5, label= 'Tinggi')
ax3.plot([2, 2],[0, S], 'g', linewidth=1.5, label= 'Sedang')
ax3.plot([1, 1],[0, R], 'r', linewidth=1.5, label= 'Rendah')
ax3.set_title('Singleton Sugeno')
ax3.legend()
#%%
##Family
R=20
S=50
T=100
M=[(R,R,R,R,S,T,R,T,T),(R,S,S,S,S,T,T,T,T),(R,T,S,T,S,T,T,T,T)]
#%%
# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes…
# This is what fuzz.interp_membership exists for!
##input crisp
in_wawancara = 3.3
in_psikotes = 490
in_tpa = 320
#%%
#fuzzification
in_1 =[]
in_1.append(fuzz.interp_membership(x_wawancara, wawancara_rendah, in_wawancara))
in_1.append(fuzz.interp_membership(x_wawancara, wawancara_sedang, in_wawancara))
in_1.append(fuzz.interp_membership(x_wawancara, wawancara_tinggi, in_wawancara))

in_2 =[]
in_2.append(fuzz.interp_membership(x_psikotes, psikotes_rendah, in_psikotes))
in_2.append(fuzz.interp_membership(x_psikotes, psikotes_sedang, in_psikotes))
in_2.append(fuzz.interp_membership(x_psikotes, psikotes_tinggi, in_psikotes))

in_3 =[]
in_3.append(fuzz.interp_membership(x_tpa, tpa_rendah, in_tpa))
in_3.append(fuzz.interp_membership(x_tpa, tpa_sedang, in_tpa))
in_3.append(fuzz.interp_membership(x_tpa, tpa_tinggi, in_tpa))

print("Derajat Keanggotaan Nilai wawancara")  
if in_1[0]>0:  
    print("Rendah : "+ str(in_1[0]))  
if in_1[1]>0:  
    print("Sedang : "+ str(in_1[1]))  
if in_1[2]>0:  
    print("Tinggi : "+ str(in_1[2]))  
    
print("")  
print("Derajat Keanggotaan Nilai psikotes")  
if in_2[0]>0:  
    print("Rendah : "+ str(in_2[0]))  
if in_2[1]>0:  
    print("Sedang : "+ str(in_2[1]))  
if in_2[2]>0:  
    print("Tinggi : "+ str(in_2[2]))

print("")  
print("Derajat Keanggotaan Nilai tpa")  
if in_3[0]>0:  
    print("Rendah : "+ str(in_3[0]))  
if in_3[1]>0:  
    print("Sedang : "+ str(in_3[1]))  
if in_3[2]>0:  
    print("Rendah : "+ str(in_3[2]))  
#%%
print("Matriks Nilai wawancara")  
print(in_1)  
print("")  
print("Matriks Nilai psikotes")  
print(in_2)  
print("Matriks Nilai tpa")  
print(in_3)  
#%%
#Inferensi dan Defazzifikasi dengan Metode Sugeno  
#Penyebut  
rul =[]  
for i in range(3) :  
    for j in range (3) :  
        rule = fuzz.relation_min(in_1[i], in_2[j])  
        rul.append(rule)  
penyebut=np.sum(rul)  
  
#Pembilang  
rul =[]  
for i in range(3) :  
    for j in range(3) :  
        rule=fuzz.relation_min(in_1[i], in_2[j])  
        rulxx=rule*M[i][j]  
        rul.append(rulxx)  
pembilang=np.sum(rul)  
hasil = pembilang/penyebut  
  
print ("Index Kelayakan Diterima  : "+ str(hasil))  
if hasil >=0 and hasil <=20 :  
    za = (abs(hasil - 0)/(20-0))*100  
    zb = (abs(hasil - 20)/(20-0))*100  
    print("Tidak Lulus : "+ '{:2.2f}'.format(zb)+" %")  
    print("Tidak Lulus : "+ '{:2.2f}'.format(za)+" %")  
if hasil >=20 and hasil <=50 :  
    za = (abs(hasil - 20)/(50-20))*100  
    zb = (abs(hasil - 50)/(50-20))*100  
    print("Tidak Lulus : "+ '{:2.2f}'.format(zb)+" %")  
    print("Waiting List : "+ '{:2.2f}'.format(za)+" %")  
if hasil >=50 and hasil <=100 :  
    za = (abs(hasil - 50)/(100-50))*100  
    zb = (abs(hasil - 100)/(100-50))*100  
    print("Waiting List : "+ '{:2.2f}'.format(zb)+" %")  
    print("Lulus : "+ '{:2.2f}'.format(za)+" %") 