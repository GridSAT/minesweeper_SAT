from pysat.formula import CNF
from pysat.solvers import Glucose4

import reader
import util


def check_cell(board, row, column, known_free_cells=[]):
    width = len(board)
    height = len(board[0])
    cnf = CNF()

    for mine in known_free_cells:
        cnf.append([-util.coords_to_var(mine[0], mine[1], width)])

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
                              [x, y - 1], [x, y + 1],
                              [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
                neighbours_ids = util.neighbours_str_to_num(neighbours, width)
                clauses = util.get_cell_constraints(int(cell), neighbours_ids)
                cnf.extend(clauses)

    cnf.append([util.coords_to_var(row, column, width)])

    g = Glucose4()
    g.append_formula(cnf.clauses)

    #if not g.solve():
    #    print('row{} column{} hasn\'t mine'.format(row, column))
    return g.solve()


board = reader.get_board_from_csv('data/board1.csv')
free_cells = []
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '?':
            if not check_cell(board, i + 1, j + 1):
                free_cells.append((i + 1, j + 1))

if check_cell(board, -1, -1, free_cells):
    print("Number combinations on the board is possible with free cells on: ")
    print(free_cells)
else:
    print("Number combination on the board is impossible")
