from pysat.formula import CNF
from pysat.solvers import Glucose4

import reader
import util


def check_cell(board, row, column):
    width = len(board)
    height = len(board[0])
    cnf = CNF()

    for c in range(width + 2):
        cnf.append([-util.coords_to_var(0, c, width)])
        cnf.append([-util.coords_to_var(height + 1, c, width)])
    for r in range(height + 2):
        cnf.append([-util.coords_to_var(r, 0, width)])
        cnf.append([-util.coords_to_var(r, width + 1, width)])

    for x in range(1, width + 1):
        for y in range(1, height + 1):
            cell = board[x - 1][y - 1]
            if cell != '?':
                cnf.append([-util.coords_to_var(x, y, width)])
                neighbours = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
                              [x, y - 1], [x, y], [x, y + 1],
                              [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
                neighbours_ids = util.neighbours_str_to_num(neighbours, width)
                clauses = util.get_cell_constraints(int(cell), neighbours_ids)
                cnf.extend(clauses)

    cnf.append([util.coords_to_var(row, column, width)])

    g = Glucose4()
    g.append_formula(cnf.clauses)

    if not g.solve():
        print('row{} column{} has mine'.format(row, column))


board = reader.get_board_from_csv('data/board1.csv')
for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y] == '?':
            check_cell(board, x + 1, y + 1)
