import numpy as np
import math

#Input: the lists of prior probabilities, likelihood, and test data
#Output: list of corresponding posterior probabilities

def posteriorFunc (priorProb, likhd, data):
   posProb = []
   alpha = 0
   limes = 0
   cherries = 0

   #count number of limes and cherries
   for i in range (len(data)):
      if data[i] == 1:
         limes += 1
      else:
         cherries += 1

   #push probabilities w/o alpha
   for i in range (len(priorProb)):
      posProb.append(likhd[i]**limes * (1 - likhd[i])**cherries * priorProb[i])
      alpha += + posProb[i]
   
   alpha = 1 / alpha
   
   for i in range (len(priorProb)):
      posProb[i] *= alpha
   return posProb

#Input the lists of prior probabilites, likhd/likelihood, training data, and one test datapoint
#Output: probability that the test datapoint happens
#Note: this function will call posteriorFunc to calculate the posterior probabilites 

def predictionFunc (priorProb, likhd, data, fPoint):
   posProb = posteriorFunc(priorProb, likhd, data)
   predictProb = 0
   if fPoint == 1:
      for i in range(len(posProb)):
         predictProb += likhd[i] * posProb[i]
   else:
      for i in range(len(posProb)):
         predictProb += (1 - likhd[i]) * posProb[i]
   return predictProb