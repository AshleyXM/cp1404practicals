class Band:
    """Represents band"""
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Play band"""
        for musician in self.musicians:
            print(musician.play())


    def __str__(self):
        """String representation of band"""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"