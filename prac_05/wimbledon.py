FILENAME = 'wimbledon.csv'


def main():
    get_records()
    champions_count, countries = process_records(records)


def process_records(records):
    """the champions and how many times they have won.
    the countries of the champions in alphabetical order"""
    champions_count = {}
    countries = set()

    for record in records:
        champion = record[0]
        country = record[1]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
        countries.add(country)
    return champions_count, countries


def get_records():
    """get records from csv file"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    # print(records)
    return records


# def display_records():


main()
