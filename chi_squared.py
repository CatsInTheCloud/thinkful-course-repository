# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:51:19 2016

@author: Cat
"""

from scipy import stats
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()


chi, p = stats.chisquare(freq.values())
print(chi, p)