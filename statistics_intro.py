# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:35:23 2015

@author: Cat
"""
#### Probability and Statistics

import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

#### Convert Alochol and Tobacco columns to float

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alc_mean = df['Alcohol'].mean()
print"The mean of the Alcohol dataset is %f" % (alc_mean)

alc_median = df['Alcohol'].median()
print"The median of the Alcohol dataset is %f" % (alc_median)

tobacco_mean = df['Tobacco'].mean() 
print"The mean of the Tobacco dataset is %f" % (tobacco_mean)

tobacco_median = df['Tobacco'].median() 
print"The median of the Tobacco dataset is %f" % (tobacco_median)

alc_range = max(df['Alcohol']) - min(df['Alcohol'])
print"The range of the Alcohol dataset is %f" % (alc_range)

alc_std = df['Alcohol'].std() 
print"The standard deviation of the Alcohol dataset is %f" % (alc_std)

alc_var = df['Alcohol'].var() 
print"The varaince of the Alcohol dataset is %f" % (alc_var)

tobacco_range = max(df['Tobacco']) - min(df['Tobacco'])
print"The range of the Tobacco dataset is %f" % (tobacco_range)

tobacco_std = df['Tobacco'].std() 
print"The standard deviation of the Tobacco dataset is %f" % (tobacco_std)

tobacco_var = df['Tobacco'].var() 
print"The variance of the Tobacco dataset is %f" % (tobacco_var) 

# Mode is not cooperating. I recognize it is different, slash there. stats.mode isn't a think that works.... help. 
tobacco_mode = df['Tobacco'].mode()
print"The mode of the Tobacco dataset is %f" % (tobacco_mode)

alc_mode = df['Alcohol'].mode()
print"The mode of the Alcohol dataset is %f" % (alc_mode)
