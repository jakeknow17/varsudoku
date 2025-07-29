from typing import List, Optional

from constraints.constraint import Constraint
from structure.board import Board
from structure.domain_grid import DomainGrid


class SudokuSolver:
    def __init__(self, board: Board, constraints: List[Constraint]):
        self._size: int = board.size
        self._domain = DomainGrid(board)
        self._constraints: List[Constraint] = constraints

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