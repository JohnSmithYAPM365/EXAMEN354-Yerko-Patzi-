# -*- coding: utf-8 -*-


import numpy as np
import pandas
from sklearn.impute import SimpleImputer
prepro = SimpleImputer(missing_values=np.nan, strategy = "mean")
filename = 'diabetes.csv'
data = pandas.read_csv(filename, header=0)
x1=np.array(data)
x1[1,0]=np.nan
x2=prepro.fit_transform(x1)
print(x2)