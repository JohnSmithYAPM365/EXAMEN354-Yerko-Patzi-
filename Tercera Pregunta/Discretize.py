# -*- coding: utf-8 -*-

import numpy as np
import pandas
from sklearn.preprocessing import KBinsDiscretizer
filename = 'diabetes.csv'
data = pandas.read_csv(filename, header=0)
x1=np.array(data)
prepro = KBinsDiscretizer(n_bins=3, encode= 'ordinal', strategy = 'uniform')
x2 = prepro.fit_transform(x1)
print(x2)
