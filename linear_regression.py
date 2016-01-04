# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:46:30 2016

@author: Cat
"""

################################m Clean and Plot Data ########################
 # find the linear equation that fits the trend between FICO scores and interest rates

import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'][0:5]

loansData['Loan.Length'][0:5]

loansData['FICO.Range'][0:5]

# WHY DID I HAVE TO PRINT THESE ONE AT A TIME? WHY CAN'T YOU RUN THE CODE AS ONE GO?

################################### Lambda Functions #############################
#Lamda functions are anonymous functions, so not bound to a name
#Doesn't need to be assigned to a variable
#always contain an expression that is returned, no assignation to a variable

import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate'][0:5]

x = loansData['Interest.Rate'][0:5].values[1]
x

x = x.rstrip('%')
x


x = float(x)

type(x)

x = x / 100 # because this is a percentage
x

x = round(x, 4)
x

type(x)

y = lambda x: round(float(x.rstrip('%')) / 100, 4)
y

y(x)
# when I run y(x) it generates an Attribute Error in that "Float" object has no attribute "ristrip" - 
# is this becuase it's already a float? 


help(map)

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/ 100,4))
type(cleanInterestRate)

cleanInterestRate[0:5]

# clean the months out of the loan length

loansData['Loan.Length'][0:5]

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip('months')))

cleanLoanLength[0:5]

loansData['Loan.Length'] = cleanLoanLength
loansData['Loan.Length'][0:5]


# Cleaning FICO Range

loansData['FICO.Range'][0:5]

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange[0:5]

cleanFICORange[0:5].values[0]

type(cleanFICORange[0:5].values[0])

cleanFICORange[0:5].values[0][0]

type(cleanFICORange[0:5].values[0][0])

cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
cleanFICORange[0:5]

type(cleanFICORange[0:5].values[0][0])

loansData['FICO.Range'] = cleanFICORange
loansData['FICO.Range'][0:5]

loansData['FICO.Range'][0:5].values[0][0]
type(loansData['FICO.Range'][0:5].values[0][0])

loansData.rename(columns = {'FICO.Range':'FICO.Score'}, inplace = True)

type(loansData['FICO.Score'][0:5].values[0][0])

loansData['FICO.Score'][0:5]
loansData['FICO.Score'][0:5].values[0][0]
loansData['FICO.Score'][0:5].values[0]

cleanFICOScore = loansData['FICO.Score'].map(lambda x: int(x[:3]))
cleanFICOScore[0:5]

# Is the column value now a single integer? 
# I feel like I still have to do a lot. I don't think it dropped the last numbers.....

################################# Roy's Method #####################################


import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#print the first 5 rows of each of the column to see what needs to be cleaned
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]

#cleaning up the columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))
#loansData[‘FICO.Score’] = [str(x) for x in loansData[‘FICO.Range’]] # another way
#loansData[‘FICO.Score’]   =    loansData[‘FICO.Score’].map(lambda x: x[:3])

#printing again to see if cleaning took place or not
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]

'''convert the data in FICO.Range into string and split the string and take the lowest value'''
loansData['FICO.Score'] = loansData['FICO.Range']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()
#print (A)
# loandata['FICO.Score'] = loandata['FICO.Range'].map(lambda x: (x.split('-')))
# loansData['FICO.Score'] = loansData['FICO.Score'].map(lambda x: int(x[0]))
FICO=[] #declare an empty array
#loansData.columns()
for j in range(len(A)):   #for j in between 0 to len(A)
  B = A[j].split("-")     #split each sub-array on - and save it to B
  #C = int(B[0], B[1])    #convert the str to int
  #C = np.mean(C)         #finding the mean of B[0] and B[1]
  C = float(B[0])           #convert the string to int, using only the first value
  FICO.append(C)          #append each C to the empty array, using first value
loansData['FICO.Score']=FICO

# Why does FICO.Score still look like a range?

#plot histogram
plt.figure()
p=loansData['FICO.Score'].hist()
plt.show()

# create a scatterplot matrix

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.savefig("LendingClubScatterMatrix).png")
### WHY DID THESE TWO THINGS PRINT THE SAME? I DON'T UNDERSTAND THE LESSON?
# HOW DO I PRINT WITH LARGER LABELS? It squishes mine...


####################################Plot Histogram of FICO Score###################
import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


plt.figure()
p = loansData(['FICO.Score'][0:5].values[0][0]).hist()
plt.show()

################### Linear Regression Analysis of FICO Score + Interest Rate ######################

# InterestRate = b + a1(FICOScore) + a2(LoanAmount)

import numpy as np
import pandas as pd
import statsmodels.api as sm

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()

# The independent variables shaped as columns 
x1 = np.matrix(fico).transpose
x2 = np.matrix(loanamt).transpose

# put the columns together to create an input matrix (with one column for each independent variable)

x = np.column_stack([x1,x2])

# create the linear model

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# output the results summary
f.summary()

# WHY YOU NO WORK?!?!

###################### Roy's Version #################################################

#regression analysis of the cleaned up columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
intrate = loansData['Interest.Rate']
intrate = [int(x) for x in intrate]
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#the columns are returned as Series, so reshape required.
#the matrix transpose takes the column and return them as 1d-array 
y = np.matrix(intrate).transpose()  #dependent variable
print (y)
x1 = np.matrix(fico).transpose()    #independent variable
x2 = np.matrix(loanamt).transpose() #independent variable
print(x1)
print(x2)

#take the independent matrix and create an input matrix, 1 col for each variable
x = np.column_stack([x1,x2])

#creating the linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
f.summary()