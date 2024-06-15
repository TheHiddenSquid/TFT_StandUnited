import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read file
    df = pd.read_csv("units.csv")


    # Take all traits and make frequency plot
    traits = []
    for coll in df.columns[1:]:
        traits.append(df[coll].to_numpy())
    traits = np.concatenate(traits)

    mydict = {}
    for trait in traits:
        if trait in mydict:
            mydict[trait] += 1
        else:
            mydict[trait] = 1
    del mydict[np.NaN]

    mydict = dict(sorted(mydict.items(), key=lambda item: item[1]))

    names = list(mydict.keys())
    freqs = list(mydict.values())

    plt.barh(names, freqs)
    plt.title("Trait frequency")
    plt.xlabel("Frequency")
    plt.ylabel("Trait")
    plt.show()



if __name__ == "__main__":
    main()
