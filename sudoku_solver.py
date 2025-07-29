from typing import List, Optional

from constraints.constraint import Constraint
from constraints.local.all_different_constraint import AllDifferentConstraint
from structure.board import Board
from structure.domain_grid import DomainGrid


class SudokuSolver:
    def __init__(self, board: Board, constraints: List[Constraint], enable_normal_sudoku_rules: bool = True):
        self._size: int = board.size
        self._domain = DomainGrid(board)
        self._constraints: List[Constraint] = constraints
        if enable_normal_sudoku_rules:
            self._add_normal_sudoku_constraints()

    def solve(self) -> Optional[Board]:
        if not self.propagate_all():
            return None
        if self._domain.all_singleton(): # All cells have one value
            return self._domain.produce_sure_board()
        r, c = self._domain.find_most_constrained_unsure_cell()
        for possibility in list(self._domain.get(r, c)): # Create a new list to avoid modifying the set during iteration
            curr_domain = self._domain.clone()
            self._domain.set(r, c, {possibility})
            result: Optional[Board] = self.solve()
            if result is not None:
                return result
            self._domain = curr_domain
        return None


    def propagate_all(self) -> bool:
        changed = True
        while changed:
            changed = False
            for constraint in self._constraints:
                if constraint.propagate(self._domain):
                    changed = True
            # Check for any contradictions
            if self._domain.any_empty():
                return False
        return True

    def _add_normal_sudoku_constraints(self) -> None:
        if self._size != 9:
            return
        # Add row constraints
        for r in range(self._size):
            self._constraints.append(AllDifferentConstraint([(r, c) for c in range(self._size)]))
        # Add column constraints
        for c in range(self._size):
            self._constraints.append(AllDifferentConstraint([(r, c) for r in range(self._size)]))
        # Add box constraints (assuming 3x3 boxes for standard Sudoku)
        box_size = int(self._size ** 0.5)
        for box_r in range(box_size):
            for box_c in range(box_size):
                cells = [(box_r * box_size + r, box_c * box_size + c) for r in range(box_size) for c in range(box_size)]
                self._constraints.append(AllDifferentConstraint(cells))