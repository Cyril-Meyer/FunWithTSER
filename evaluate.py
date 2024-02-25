import math
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics


def view(y, pred, figsize=(18, 4)):
    pred, y = np.array(pred), np.array(y)
    sort = y.argsort(axis=None).reshape(y.shape)
    pred = pred.ravel()[sort]
    y = y.ravel()[sort]

    plt.figure(figsize=figsize)
    plt.scatter(x=[i for i in range(len(y))], y=y,    color='#00ff00ff')
    plt.scatter(x=[i for i in range(len(y))], y=pred, color='#ff000030')
    plt.show()
    
def mse(y, pred):
    return sklearn.metrics.mean_squared_error(y, pred)
    
def rmse(y, pred):
    return math.sqrt(mse(y, pred))
