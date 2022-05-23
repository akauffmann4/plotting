import matplotlib.pyplot as plt
import pandas as pd

def plot():
    before = pd.read_csv("female.csv")
    #after = pd.read_csv("afterFemale.csv")
    plt.scatter(before.number, before.value, color='red', label='before deformations F')
    #plt.scatter(after.number, after.value, color='red', label='after deformations F')


    before = pd.read_csv("male.csv")
    #after = pd.read_csv("afterMale.csv")
    plt.scatter(before.number, before.value, color='blue', label='before deformations M')
    #plt.scatter(after.number, after.value, color='blue', label='after deformations M')

    before = pd.read_csv("average.csv")
    #after = pd.read_csv("afterAverage.csv")
    #plt.scatter(before.number, before.value, color='green', label='before deformations A')
    #plt.scatter(after.number, after.value, color='green', label='after deformations A')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot()