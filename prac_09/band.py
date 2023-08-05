
class Band:
    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            instrument = musician.get_instruments()
            if not instrument:
                print(f"{musician.name} needs an instrument!")
            else:
                for inst in instrument:
                    print(f"{musician.name} is playing: {inst}")

    def __str__(self):
        result = f"{self.band_name} (str)\n"
        for musician in self.musicians:
            result += str(musician) + "\n"
        return result


if __name__ == "__main__":
    from musician import Musician
    from guitar import Guitar
