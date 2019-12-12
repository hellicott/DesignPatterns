from builder.animal import AnimalWithoutBuilder, AnimalWithBuilder


def create_animal_without_builder():
    otter_without_builder = AnimalWithoutBuilder("Eurasian Otter",
                                                 "Hazel",
                                                 "10.11.2018",
                                                 "Otters and Butterflies Conservation",
                                                 "Otters and Butterflies, Dartmoor",
                                                 "fresh water",
                                                 "fresh water",
                                                 "Near Threatened")
    print("WITHOUT:")
    print(otter_without_builder)


def create_animal_with_builder():
    otter_with_builder = AnimalWithBuilder.AnimalBuilder("Eurasian Otter")\
        .name("Hazel")\
        .date_of_birth("10.11.2018")\
        .domestic_living_details("Otters and Butterflies Conservation", "Otters and Butterflies, Dartmoor", "fresh water")\
        .natural_habitat("fresh water")\
        .conservation_level("Near Threatened")\
        .build()
    print("WITH:")
    print(otter_with_builder)

def create_animal_with_builder_missing_parameters():
    pangolin_with_builder = AnimalWithBuilder.AnimalBuilder("Sunda Pangolin")\
        .natural_habitat("forest tree hollow")\
        .conservation_level("Critically Endangered")\
        .build()
    print("WITH + MISSING PARAMETERS:")
    print(pangolin_with_builder)


create_animal_without_builder()
create_animal_with_builder()
create_animal_with_builder_missing_parameters()
