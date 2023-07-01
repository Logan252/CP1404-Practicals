FILENAME = 'wimbledon.csv'


def main():
    read_file()


def read_file():
    data = []
    in_file = open('FILENAME', encoding='utf-8')
    lines = [line.strip() for line in in_file.readlines()]
    data.append(lines)
    winners = set(lines)
    print(data)
    print(winners)
    print(len(winners))
    in_file.close()


main()
