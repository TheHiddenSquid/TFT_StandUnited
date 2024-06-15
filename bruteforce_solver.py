import trait_tools

def main():
    unit_trait_dict = trait_tools.create_unit_trait_dict()
    trait_threshold_dict = trait_tools.create_trait_threshold_dict()

    print(unit_trait_dict)


if __name__ == "__main__":
    main()