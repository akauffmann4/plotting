import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def plot():
    df = pd.read_csv('test.csv')
    g = sns.pairplot(df, hue="type")
    plt.show()

if __name__ == '__main__':
    plot()