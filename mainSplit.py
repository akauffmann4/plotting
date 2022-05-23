import matplotlib.pyplot as plt
import pandas as pd

def plot():
    mean = pd.read_csv("testSplitmean.csv")
    variance = pd.read_csv("testSplitvariance.csv")
    observations = pd.read_csv("testSplitobservations.csv")

    errorfill(mean.domain, mean.value, variance.value)
    plt.scatter(observations.domain, observations.value, color='red', label='observations')
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()

    mean2 = pd.read_csv("testSplit2mean.csv")
    variance2 = pd.read_csv("testSplit2variance.csv")
    observations2 = pd.read_csv("testSplit2observations.csv")
    errorfill(mean2.domain, mean2.value, variance2.value)
    plt.scatter(observations2.domain, observations2.value, color='red', label='observations')
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