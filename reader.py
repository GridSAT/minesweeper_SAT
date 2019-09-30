import csv


def get_board_from_csv(name):
    data = []
    with open(name) as csvfile:
        rows = csv.reader(csvfile, delimiter=' ')
        for row in rows:
            data.append(row)
    return data
