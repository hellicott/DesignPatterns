class AnimalWithoutBuilder:

    def __init__(self, species, name, dob, owner, residence, natural_habitat, current_habitat, conservation_level):
        self.species = species
        self.name = name
        self.dob = dob
        self.owner = owner
        self.residence = residence
        self.natural_habitat = natural_habitat
        self.current_habitat = current_habitat
        self.conservation_level = conservation_level

    def __str__(self):
        return ", ".join([self.name, self.dob, self.owner, self.residence,
                          self.natural_habitat, self.current_habitat, self.conservation_level])




class AnimalWithBuilder:

    def __init__(self, builder):
        self.species = builder.species
        self.name = builder.name
        self.dob = builder.dob
        self.owner = builder.owner
        self.residence = builder.residence
        self.natural_habitat = builder.natural_habitat
        self.current_habitat = builder.current_habitat
        self.conservation_level = builder.conservation_level

    def __str__(self):
        return ", ".join([self.name, self.dob, self.owner, self.residence,
                          self.natural_habitat, self.current_habitat, self.conservation_level])

    class AnimalBuilder:

        def __init__(self, species):
            self.species = species
            self.name = None
            self.dob = None
            self.owner = None
            self.residence = None
            self.natural_habitat = None
            self.current_habitat = None
            self.conservation_level = None

        def name(self, name):
            self.name = name
            return self
            
        def date_of_birth(self, dob):
            self.dob = dob
            return self
            
        def domestic_living_details(self, owner, residence, current_habitat):
            self.owner = owner
            self.residence = residence
            self.current_habitat = current_habitat
            return self
        
        def conservation_level(self, level):
            self.conservation_level = level
            return self
            
        def natural_habitat(self, habitat):
            self.natural_habitat = habitat
            return self

        def build(self):
            animal = AnimalWithBuilder(self)
            return animal
