import matplotlib.pyplot as plt
import pandas as pd

def plot():
    female = pd.read_csv("female.csv")

    for i in range(1,100):
        test = female["sample"+str(i)]
        plt.scatter(female.x, test, color="red")

    plt.legend()
    plt.show()

    male = pd.read_csv("male.csv")
    for i in range(1, 100):
        test = male["sample" + str(i)]
        plt.scatter(male.x, test, color="blue")

    plt.legend()
    plt.show()

    average = pd.read_csv("average.csv")
    for i in range(1, 100):
        test = average["sample" + str(i)]
        plt.scatter(average.x, test, color="green")

    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot()