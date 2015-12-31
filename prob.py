# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:45:23 2015

@author: Cat
"""

# -*- coding: utf-8 -*-

import collections

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(x)

print(c)

count_sum = sum(c.values())

for k,v in c.iteritems():
    print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
    
import matplotlib.pyplot as plt
# Box Plot
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()

# Save Box Plot
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.savefig("boxplotpractice.png")

# Histogram 
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.hist(x, histtype='bar')
plt.show()

# Histogram Save
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.hist(x, histtype='bar')
plt.savefig("histogrampractice.png")


## QQ Plots to test normal distribution. Data should form a strait line

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #first graph
plt.figure()
test_data2 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("qqplotpractice.png")
plt.show() #second graph

