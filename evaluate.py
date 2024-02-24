import math
import matplotlib.pyplot as plt
import sklearn.metrics


def view(y, pred, figsize=(18, 4)):
    plt.figure(figsize=figsize)
    y, pred = zip(*sorted(list(zip(y, pred))))
    plt.scatter(x=[i for i in range(len(y))], y=y)
    plt.scatter(x=[i for i in range(len(y))], y=pred)
    plt.show()
    
def mse(y, pred):
    return sklearn.metrics.mean_squared_error(y, pred)
    
def rmse(y, pred):
    return math.sqrt(mse(y, pred))
