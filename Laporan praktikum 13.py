# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : Jumat,241221
@Judul : Laporan Praktikum 13
@Materi : Data Analisis
@author: Muhammad Danil Hidayat
@NIM : 06500210032
"""

import pandas as pd

def pertama(data):
   
  file = open("NegaraMean.csv","w")
  file.write(data)
  file.close()
  
def kedua(data):
 
  file=open("NegaraStandarDevisiasi.csv","w")
  file.write(data)
  file.close()
  
data={"Negara":["Indonesia","Jepang","India","China","Amerika Serikat","Brazil",
"Rusia"],
    "Ibu Kota":["Jakarta","Tokyo","New Delhi","Beijing","Washington DC","Brazilia",
"Moskow"],
    "Benua":["Asia","Asia","Asia","Asia","Amerika","Amerika","Asia"],
    "Luas":[1905,377,1252,1357,329,210,146]}

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Framenya:\n")
print(df)
print("\nBerikut Data Menan:")
print(mean)
print("\nBerikut Data Standar Devisiasi")
print(std)
pertama(str(mean))
kedua(str(std))
print("\nFile Berhasil dibuat")
    
