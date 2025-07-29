from typing import Optional

from structure.board import Board
from structure.defs import Domain, Cell


class DomainGrid:
    def __init__(self, starting_board: Board):
        self._size = starting_board.size
        self._grid = [
            [set(range(1, self._size + 1)) for _ in range(self._size)]
            for _ in range(self._size)
        ]
        for row in range(self._size):
            for col in range(self._size):
                value = starting_board.get_cell(col, row)
                if value > 0:
                    self._grid[row][col] = {value}

    def get(self, row: int, col: int) -> Domain:
        return self._grid[row][col]

    def set(self, row: int, col: int, domain: Domain):
        if not all(x in range(1, self._size + 1) for x in domain):
            raise ValueError(f"Domain values must be within range {1}-{self._size}.")
        self._grid[row][col] = domain

    def clone(self) -> 'DomainGrid':
        new = self.__class__.__new__(self.__class__)
        new._size = self._size
        new._grid = [[domain.copy() for domain in row] for row in self._grid]
        return new

    def any_empty(self) -> bool:
        return any(len(self._grid[row][col]) == 0 for row in range(self._size) for col in range(self._size))

    def all_singleton(self) -> bool:
        return all(len(self._grid[row][col]) == 1 for row in range(self._size) for col in range(self._size))

    def produce_sure_board(self) -> Board:
        cells = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for row in range(self._size):
            for col in range(self._size):
                if len(self._grid[row][col]) == 1:
                    cells[row][col] = next(iter(self._grid[row][col]))
        return Board(cells)

    def find_most_constrained_unsure_cell(self) -> Optional[Cell]:
        min_domain_size = self._size + 1 # Start with a size larger than any possible domain
        most_constrained_cell = None
        for row in range(self._size):
            for col in range(self._size):
                if len(self._grid[row][col]) > 1:
                    if len(self._grid[row][col]) < min_domain_size:
                        min_domain_size = len(self._grid[row][col])
                        most_constrained_cell = (row, col)
        return most_constrained_cell
