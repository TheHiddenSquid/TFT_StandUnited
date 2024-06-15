import trait_tools
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    unit_trait_dict = trait_tools.create_unit_trait_dict("units.csv")
    trait_threshold_dict = trait_tools.create_trait_threshold_dict("traits.csv")

    all_units = list(unit_trait_dict.keys())


    no_units = []
    no_traits = []
    for i in range(1,11):
        tmp = []
        for _ in range(100_000):
            units = [random.choice(all_units) for _ in range(i)]
            trait_freq = trait_tools.get_traits_frequencies(units, unit_trait_dict)
            active_traits = trait_tools.get_active_traits(trait_freq, trait_threshold_dict)
            tmp.append(len(active_traits))
        no_units.append(i)
        no_traits.append(np.max(tmp))   #Change between max/min/mean

    plt.bar(no_units, no_traits)
    plt.title("Number of active traits given random board")
    plt.xlabel("Units")
    plt.ylabel("Traits")
    plt.show()



if __name__ == "__main__":
    main()
