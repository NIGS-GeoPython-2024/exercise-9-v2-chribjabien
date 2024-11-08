import pandas as pd
import numpy as np
"""
This scriptfile contains function that calculates:
    lineregress
    >slope of regression line(B)
    >y-intercept of regression line(A)
    pearson
    >correlation coefficient
    chi-squared
    >goodness of fit
"""

#problem 1 slopes and y-intercepts
def linregress(x,y):
    x = np.array(x)
    y = np.array(y)

    delta = (len(x) * (x**2).sum()) - (x.sum() ** 2)
    A = (((x**2).sum() * y.sum()) - (x.sum() * (x*y).sum())) / delta
    B = ((len(x) * (x*y).sum()) - (x.sum() * y.sum())) / delta
    return (A,B)


#problem 2 calculating r
def pearson(x,y):
    x = np.array(x)
    y = np.array(y)

    top_eq = ((x-x.mean()) * (y-y.mean())).sum()
    bot_eq = np.sqrt((((x-x.mean())**2).sum() * ((y-y.mean())**2).sum()))
    r = top_eq/bot_eq
    return r


#problem 3 chi squared
def chi_squared(obs, exp, std):
    N = len(obs)
    chi_sqrd_sum = 0

    for i in range(N):
      obs_val = obs[i]
      exp_val = exp[i]
      std_val = std[i]
      chi_sqrd_sum += ((obs_val - exp_val) ** 2) / (std_val ** 2)

    return chi_sqrd_sum/N





