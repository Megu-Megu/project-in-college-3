#libraries
import pandas as pd
import numpy as np

#baca file dataset
df = pd.read_csv("apartemen.csv")
print(df)

#cek ada missing value
df.isnull().values.any()
print(df.isnull().values.any())

#banyaknya missing value
df.isnull().sum().sum()
print(df.isnull().sum().sum())

#melihat kolom kodeapt
df["KodeApt"]
df['KodeApt'].isnull()
print(df["KodeApt"])
print(df['KodeApt'].isnull())

#melihat kolom jumlah kamar
df['Jum_kamar']
df['Jum_kamar']
print(df['Jum_kamar'])
print(df['Jum_kamar'])

#membuat daftar missing value
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("apartemen.csv", na_values = missing_values)
df['Jum_kamar']
df['Jum_kamar'].isnull()
df['St_milik']
df['St_milik'].isnull()
print(df['Jum_kamar'])
print(df['Jum_kamar'].isnull())
print(df['St_milik'])
print(df['St_milik'].isnull())

cnt = 0 
for row in df['St_milik']:
    try :
        df['St_milik'].isnull()
        int(row)
        df.loc[cnt, 'St_milik']=np.nan
    except ValueError:
        pass
    cnt+=1

df['St_milik'].isnull()
df.isnull().sum()
df.isnull().sum().sum()
print(df['St_milik'].isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())

#mengganti missing value dengan sebuah angka
df['KodeApt'].fillna(837, inplace=True)
print(df.KodeApt)

#mengganti pada lokasi spesifik
df.loc[2,'KodeApt'] = 8837
print(df.KodeApt)

#mengganti missing value dengan median
median = df['Jum_kamar'].median()
df['Jum_kamar'].fillna(median, inplace=True)

#melihat keseluruhan data
print(df)

#mengganti pada lokasi spesifik pada kolom St_milik
df.loc[3,'St_milik'] = 'N'
df.loc[6,'St_milik'] = 'Y'
print(df.St_milik)
print(df)

#simpan data
df.to_csv('Apartemen_ok.csv')

#mengubah data non numerik jadi numerik
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
import pandas as pd
import numpy as np

df = pd.read_csv('Apartemen_ok.csv')

print(df)
le=LabelEncoder()

for col in df.columns.values:
    #encoding pada variabel kategorical
    if df[col].dtypes=='object':
        data=df[col].append(df[col])
        le.fit(data.values)
        df[col]=le.transform(df[col])
df.head(10)
df.to_csv('apartemen_numerik.csv', header=True, index=False)
