def get_cell_constraints(cell_num, neighbours):
    clauses = []
    rows_count = 2 ** cell_num
    for i in range(rows_count):
        bin_representation = bin(i)
        bit_count = bin_representation.count("1")
        if bit_count == cell_num:
            clause = []
            current_bit = 0
            for neighbour in neighbours:
                sign = -1 if bin_representation[current_bit] == 0 else 1
                clause.append(neighbour * sign)
            clauses.append(clause)


def get_neighbours(array, row, column):
    neighbours = []
    for x in range(row - 1, row + 2):
        for y in range(column - 1, column + 2):
            if 0 <= x <= len(array) and 0 <= y <= len(array[x]) and x != row and y != column:
                neighbours.append(array[x][y])
