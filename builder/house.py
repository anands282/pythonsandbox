class House:
    def __init__(self):
        self.basement = None
        self.walls = None
        self.roof = None
        self.interior = None

    def __str__(self):
        return f"House with {self.basement},{self.walls},{self.roof},{self.interior}"