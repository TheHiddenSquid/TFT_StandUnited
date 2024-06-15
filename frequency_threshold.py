import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read file
    df = pd.read_csv("traits.csv")


    # Take all traits and make frequency plot
    mydict = {df[df.columns[0]][i]: df[df.columns[1]][i] for i in range(len(df[df.columns[0]]))}
    mydict = dict(sorted(mydict.items(), key=lambda item: item[1]))
    names = list(mydict.keys())
    thresholds = list(mydict.values())


    plt.barh(names,thresholds)
    plt.title("Trait activation threshold")
    plt.xlabel("Activation threshold")
    plt.ylabel("Trait")
    plt.show()



if __name__ == "__main__":
    main()
