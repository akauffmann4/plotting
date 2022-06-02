import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def plot():
    df = pd.read_csv('gapminder_data.csv')
    df.head()
    sns.pairplot(df)
    plt.show()



if __name__ == '__main__':
    plot()