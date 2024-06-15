import pandas as pd
import numpy as np
import time

def get_traits_frequencies(units, unit_trait_dict):
    trait_frequencies = {}
    units = set(units)
    for unit in units:
        traits = unit_trait_dict[unit]
        for trait in traits:
            if trait in trait_frequencies:
                trait_frequencies[trait] += 1
            else:
                trait_frequencies[trait] = 1
   
    del trait_frequencies[np.NaN]

    return trait_frequencies


def get_active_traits(freqs, threshold_dict):
    active_traits = []
    for trait, count in freqs.items():
        trait_data = threshold_dict[trait]
        best = 0
        for val in trait_data:
            if count >= val:
                best = val
            else:
                break
        if best != 0:
            active_traits.append((trait,int(best)))

    return active_traits


def create_unit_trait_dict():
    units_df = pd.read_csv("units.csv")

    unit_trait_dict = {}
    for _, row in units_df.iterrows():
        unit_trait_dict[row["Name"]] = row[["Trait1","Trait2","Trait3"]].tolist()
   
    return unit_trait_dict

def create_trait_threshold_dict():
    trait_df = pd.read_csv("traits.csv")

    threshold_dict = {}
    for _, row in trait_df.iterrows():
        threshold_dict[row["Trait"]] = row[["Threshold1","Threshold2","Threshold3","Threshold4","Threshold5","Threshold6"]].tolist()
   
    return threshold_dict

def main():
    # Gen 1: 600 runs / second          initial
    # Gen 2: 1000 runs / second         dont read file every time
    # Gen 3: 1070 runs / second         better get trait frequencies
    # Gen 4: 16_000 runs / second       dict instead of df
    # Gen 5: 320_000 runs / second      dict instead of df


    unit_trait_dict = create_unit_trait_dict()
    trait_threshold_dict = create_trait_threshold_dict()


    units = ["Zoe", "Zyra", "Riven", "Morgana", "Shen", "Aatrox", "Illaoi", "Kayn", "Caitlyn"]

    
    runs = 1_000_000
    t = time.perf_counter()
    for _ in range(runs):
        trait_freq = get_traits_frequencies(units, unit_trait_dict)
        active_traits = get_active_traits(trait_freq, trait_threshold_dict)
        
    print(trait_freq)
    print(active_traits)

    t = time.perf_counter()-t
    print("Runs per scond:", runs/t)



if __name__ == "__main__":
    main()
