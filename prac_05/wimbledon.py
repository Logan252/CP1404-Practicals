in_file = open('wimbledon.csv')
lines = [line.strip() for line in in_file.readlines()]
print(lines)
in_file.close()