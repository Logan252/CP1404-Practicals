FILENAME = 'wimbledon.csv'
data = []


def main():
    records = get_records(FILENAME)
    champions_count, countries = process_records(records)
    display_records(champions_count, countries)


def process_records(records):
    """the champions and how many times they have won.
    the countries of the champions in alphabetical order"""
    champions_count = {}
    countries = set()

    for record in records:
        champion = record[2]
        country = record[1]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1

        countries.add(country)

    return champions_count, countries


def get_records(filename):
    """get records from csv file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    # print(records)      Test line
    return records


def display_records(champions_count, countries):
    print("Champions and how many times they've won")
    for champion, count in champions_count.items():
        print(f"{champion}: {count} time(s)")
    print(f" These {count} countries have won wimbledon: \n{countries}")


main()
