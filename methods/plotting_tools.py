import numpy as np
import matplotlib.pyplot as plt

def plot_hist(array,bin_num,label,default=True):
    n, bins = np.histogram(array,bins=bin_num,normed=default)
    plt.plot(bins[1:],n,label=label)
    return 
