class Sandwich:

    def __init__(self):
        self._bread_type = None
        self._fillings = None
        self._butter = None

    def __str__(self):
        return f"{self._fillings} on {self._bread_type} bread with butter [{self._butter}]"

    class SandwichBuilder:
        def __init__(self, bread_type):
            self.bread_type = bread_type
            self.fillings = []
            self.butter = False

        def add_filling(self, filling):
            self.fillings.append(filling)
            return self

        def with_butter(self):
            self.butter = True
            return self

        def build(self):
            sandwich = Sandwich()
            sandwich._bread_type = self.bread_type
            sandwich._fillings = self.fillings
            sandwich._butter = self.butter
            return sandwich
