
class Band:
    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            instrument = musician.get_instrument()
            if instrument is None:
                print(f"{musician.name} needs an instrument!")
            else:
                print(f"{musician.name} is playing: {instrument}")

    def __str__(self):
        result = f"{self.band_name} (str)\n"
        for musician in self.musicians:
            result += str(musician) + "\n"
        return result


if __name__ == "__main__":


