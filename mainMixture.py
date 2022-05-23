import matplotlib.pyplot as plt
import pandas as pd


def plot():
    mean = pd.read_csv("mean1.csv")
    variance = pd.read_csv("variance1.csv")
    observations = pd.read_csv("observations.csv")
    errorfill(mean.domain, mean.value, variance.value)
    mean2 = pd.read_csv("mean2.csv")
    variance2 = pd.read_csv("variance2.csv")
    errorfill2(mean2.domain, mean2.value, variance2.value)
    plt.scatter(observations.domain, observations.value, color='red', label='observations')
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()


def errorfill(x, y, yerr, color='black', alpha_fill=0.3, ax=None):
    # ax = ax if ax is not None else plt.gca()
    # ax = plt
    ymin = y - yerr
    ymax = y + yerr
    test = plt.plot(x, y, color=color, label='meanChild1')
    plt.fill_between(x, ymax, ymin, color='blue', alpha=alpha_fill, label='varianceChild1')


def errorfill2(x, y, yerr, color='black', alpha_fill=0.3, ax=None):
    # ax = ax if ax is not None else plt.gca()
    # ax = plt
    ymin = y - yerr
    ymax = y + yerr
    test = plt.plot(x, y, color=color, label='meanChild2')
    plt.fill_between(x, ymax, ymin, color='blue', alpha=alpha_fill, label='varianceChild2')


if __name__ == '__main__':
    plot()
