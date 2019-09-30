def get_cell_constraints(cell_num, neighbours):
    if cell_num == 0:
        return [[-neighbours[i]] for i in range(len(neighbours))]

    most = at_most(cell_num, neighbours)
    least = at_least(cell_num, neighbours)
    return most + least


def at_most(n, neighbours):
    clauses = []

    rows_count = 2 ** len(neighbours)
    for row in range(rows_count):
        bin_representation = '{0:0{len}b}'.format(row, len=len(neighbours))
        bit_count = bin_representation.count("1")
        if bit_count == n + 1:
            clauses.append([-neighbours[i] for i in range(len(neighbours)) if (bin_representation[i] == '1')])

    return clauses


def at_least(n, neighbours):
    clauses = []

    rows_count = 2 ** len(neighbours)
    for row in range(rows_count):
        bin_representation = '{0:0{len}b}'.format(row, len=len(neighbours))
        bit_count = bin_representation.count("1")
        if bit_count == (len(neighbours) - (n - 1)):
            clauses.append([neighbours[i] for i in range(len(neighbours)) if (bin_representation[i] == '1')])

    return clauses


def neighbours_str_to_num(neighbours, width):
    num_neighbours = []
    for (x, y) in neighbours:
        num_neighbours.append(coords_to_var(x, y, width))
    return num_neighbours


def coords_to_var(row, col, width):
    return row * (width + 2) + col + 1
