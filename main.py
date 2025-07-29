from constraints.local.thermometer_constraint import ThermometerConstraint
from structure.board import Board
from sudoku_solver import SudokuSolver

if __name__ == "__main__":
    # initial_board = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]
    initial_board = [
        [0, 1, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 0, 2, 0, 5, 8, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 3, 0, 7]
    ]
    board = Board(initial_board)
    constraints = [
        ThermometerConstraint([(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]),
        ThermometerConstraint([(1, 7), (1, 6), (1, 5), (1, 4), (2, 4), (3, 4)]),
        ThermometerConstraint([(7, 4), (6, 4), (5, 4), (4, 4)]),
    ]
    solver = SudokuSolver(board, constraints)
    print(solver.solve())
