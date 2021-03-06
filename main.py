import matplotlib.pyplot as plt
import pandas as pd

def plot():
    mean = pd.read_csv("test.csv")
    variance = pd.read_csv("variance.csv")
    observations = pd.read_csv("observations.csv")
    errorfill(mean.domain, mean.value, variance.value)
    plt.scatter(observations.domain, observations.value, color='red', label='observations')
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()

def errorfill(x, y, yerr, color='black', alpha_fill=0.3, ax=None):
    #ax = ax if ax is not None else plt.gca()
    #ax = plt
    ymin = y - yerr
    ymax = y + yerr
    test = plt.plot(x, y, color=color, label='mean')
    plt.fill_between(x, ymax, ymin, color='blue', alpha=alpha_fill, label='variance')

if __name__ == '__main__':
    plot()