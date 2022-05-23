import matplotlib.pyplot as plt
import pandas as pd

def plot():
    before = pd.read_csv("femaleBefore.csv")
    after = pd.read_csv("femaleAfter.csv")
    plt.scatter(before.x, before.value, color='red', label='before deformations F')
    plt.scatter(after.x, after.value, color='blue', label='after deformations F')

    #before = pd.read_csv("maleBefore.csv")
    #after = pd.read_csv("maleAfter.csv")
    #plt.scatter(before.x, before.value, color='blue', label='before deformations M')
    #plt.scatter(after.x, after.value, color='blue', label='after deformations M')

    #before = pd.read_csv("before.csv")
    #after = pd.read_csv("after.csv")
    #plt.scatter(before.x, before.value, color='green', label='before deformations A')
    #plt.scatter(after.x, after.value, color='green', label='after deformations A')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot()