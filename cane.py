class Cane():
    def __init__(self, name="Fuffi"):
        self.name = name

    def abbaia(self):
        print(self.name + " sta abbaiando.")

    def __str__(self):
        return f"Cane {self.name}"

        