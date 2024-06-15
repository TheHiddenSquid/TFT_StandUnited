import trait_tools
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    unit_trait_dict = trait_tools.create_unit_trait_dict("units.csv")
    trait_threshold_dict = trait_tools.create_trait_threshold_dict("traits.csv")

    all_units = list(unit_trait_dict.keys())


    board_size = 10
    best_boards = []
    most_traits = 0
    for _ in range(10_000_000):
        units = [random.choice(all_units) for _ in range(board_size)]
        trait_freq = trait_tools.get_traits_frequencies(units, unit_trait_dict)
        active_traits = trait_tools.get_active_traits(trait_freq, trait_threshold_dict)
        if len(active_traits) > most_traits:
            most_traits = len(active_traits)
            best_boards.append(units)
        elif len(active_traits) == most_traits:
            best_boards.append(units)
        
    
    print("Most traits was:", most_traits)
    print("Some of the best boards were:")
    for board in best_boards[-5:]:
        print(board)
        trait_freq = trait_tools.get_traits_frequencies(board, unit_trait_dict)
        active_traits = trait_tools.get_active_traits(trait_freq, trait_threshold_dict)
        print("Traits:",len(active_traits), "They were:", active_traits)
        print()



if __name__ == "__main__":
    main()
