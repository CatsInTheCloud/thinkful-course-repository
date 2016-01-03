# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 08:30:25 2016

@author: Cat
"""

import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#clean data

loansData.dropna(inplace=True)

#generate and save box plot

loansData.boxplot(column='Amount.Requested')
plt.show()
plt.savefig("lendingclubamountrequestedbxplt.png")

#generate and save histogram

loansData.hist(column='Amount.Requested')
plt.show()
plt.savefig("lendingclubamountrequestedhist.png")

#generate and save QQ plot

import scipy.stats as stats
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
plt.savefig("lendingclubamountrequestedQQplt.png")

# Cheif observations compared to the amount funded by investors: 
# 1) far more small loans are applied for than approved.
# 2) surprisingly many of the largest loans applied for are also approved. 
# 3) the amount funded is slightly more nromally distribtued than the amount applied for. 
# Is 0.002 statistically significant at all? I doubt it?
