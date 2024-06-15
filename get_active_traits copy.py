import pandas as pd
import numpy as np
import collections
import time

def get_traits_frequencies(units, all_units_df):
    chosen_units_df = all_units_df[all_units_df["Name"].isin(units)]
    traits = chosen_units_df.to_numpy()[:,1:].flatten() 
    trait_frequencies = collections.Counter(traits)
    del trait_frequencies[np.NaN]
    return dict(trait_frequencies)


def get_active_traits(freqs, traits_df):
    used_traits = freqs.keys()
    used_traits_df = traits_df[traits_df["Trait"].isin(used_traits)]

    active_traits = []
    for trait, count in freqs.items(): 
        thresholds = used_traits_df[used_traits_df["Trait"] == trait].to_numpy()[0][1:]
        best = 0
        for val in thresholds:
            if count >= val:
                best = val
            else:
                break
        if best != 0:
            active_traits.append((trait,int(best)))

    return active_traits


def main():
    # Gen 1: 600 runs / second
    # Gen 2: 1000 runs / second        dont read file every time
    # Gen 3: 1070 runs / second        better get trait frequencies

    units_df = pd.read_csv("units.csv")
    traits_df = pd.read_csv("traits.csv")

    units = ["Zoe", "Zyra", "Riven", "Morgana", "Shen", "Aatrox", "Illaoi", "Kayn", "Caitlyn"]
    
    runs = 10000
    t = time.perf_counter()
    for i in range(runs):
        trait_freq = get_traits_frequencies(units, units_df)
        active_traits = get_active_traits(trait_freq, traits_df)
        
    print(trait_freq)
    print(active_traits)

    t = time.perf_counter()-t
    print("Runs per scond:", runs/t)



if __name__ == "__main__":
    main()
