from typing import Optional, List


class Board:
    def __init__(self, initial_values: List[List[int]]):
        self._size = len(initial_values) # We assume a square board
        self._cells = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for row_idx, row in enumerate(initial_values):
            if len(row) != self._size:
                raise ValueError("All rows must have the same length as the board size.")
            for value_idx, value in enumerate(row):
                if not (0 <= value <= self._size):
                    raise ValueError(f"Cell values must be between 0 and {self._size}.")
                self._cells[row_idx][value_idx] = value

    @property
    def size(self):
        return self._size

    def get_cell(self, x: int, y: int):
        if 0 <= x < self._size and 0 <= y < self._size:
            return self._cells[y][x]
        return None

    def set_cell(self, x: int, y: int, value):
        if 0 <= x < self._size and 0 <= y < self._size:
            self._cells[y][x] = value

    def __str__(self):
        return '\n'.join([' '.join(str(cell) for cell in row) for row in self._cells])

    def get_cells_str(self):
        return f"[\n\t[{'],\n\t['.join([', '.join(str(cell) for cell in row) for row in self._cells])}]\n]"
