# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:01:01 2022

@author: USUARIO
"""

import math


def percentile(N, percentaje, key=lambda x:x):
    """
    Encuentra el percentil de una lista de valores.

    @parámetro N - Es una de las columnas del dataset. N DEBE esta ya ordenado.
    @parámetro porcentaje - Es un valor flotante de 0,0 a 1,0.
    @parámetro clave - Función clave opcional para calcular el valor de cada elemento de N.

    @retorno - el percentil de los valores
    """
    k = (len(N)-1) * percentaje
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

import numpy as np
import pandas
filename = 'diabetes.csv'
data = pandas.read_csv(filename, header=0)

print("python - pandas - numpy")
x1=np.array(data['Pregnancies'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['Pregnancies'].median())
print(data['Pregnancies'].quantile(0.25))

print(np.percentile(data['Pregnancies'],50))
print(np.percentile(data['Pregnancies'],25))

print("python - pandas - numpy")
x1=np.array(data['Glucose'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['Glucose'].median())
print(data['Glucose'].quantile(0.25))

print(np.percentile(data['Glucose'],50))
print(np.percentile(data['Glucose'],25))

print("python - pandas - numpy")
x1=np.array(data['BloodPressure'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['BloodPressure'].median())
print(data['BloodPressure'].quantile(0.25))

print(np.percentile(data['BloodPressure'],50))
print(np.percentile(data['BloodPressure'],25))

print("python - pandas - numpy")
x1=np.array(data['SkinThickness'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['SkinThickness'].median())
print(data['SkinThickness'].quantile(0.25))

print(np.percentile(data['SkinThickness'],50))
print(np.percentile(data['SkinThickness'],25))

print("python - pandas - numpy")
x1=np.array(data['Insulin'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['Insulin'].median())
print(data['Insulin'].quantile(0.25))

print(np.percentile(data['Insulin'],50))
print(np.percentile(data['Insulin'],25))

print("python - pandas - numpy")
x1=np.array(data['BMI'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['BMI'].median())
print(data['BMI'].quantile(0.25))

print(np.percentile(data['BMI'],50))
print(np.percentile(data['BMI'],25))

print("python - pandas - numpy")
x1=np.array(data['DiabetesPedigreeFunction'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['DiabetesPedigreeFunction'].median())
print(data['DiabetesPedigreeFunction'].quantile(0.25))

print(np.percentile(data['DiabetesPedigreeFunction'],50))
print(np.percentile(data['DiabetesPedigreeFunction'],25))

print("python - pandas - numpy")
x1=np.array(data['Age'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['Age'].median())
print(data['Age'].quantile(0.25))

print(np.percentile(data['Age'],50))
print(np.percentile(data['Age'],25))

print("python - pandas - numpy")
x1=np.array(data['Outcome'])
x1.sort()
x11=percentile(x1,0.5)
x22=percentile(x1,0.25)
print(x11)
print(x22)

print(data['Outcome'].median())
print(data['Outcome'].quantile(0.25))

print(np.percentile(data['Outcome'],50))
print(np.percentile(data['Outcome'],25))




