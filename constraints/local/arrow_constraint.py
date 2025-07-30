from typing import List

from constraints.constraint import Constraint
from structure.defs import Cell
from structure.domain_grid import DomainGrid


class ArrowConstraint(Constraint):
    def __init__(self, circle: Cell, arrow: List[Cell]):
        self._circle = circle
        self._arrow = arrow

    def propagate(self, domain_grid: DomainGrid) -> bool:
        changed = False
        for value in domain_grid.get(*self._circle):
            if not self._can_make_sum(value, domain_grid):
                domain_grid.set(self._circle[0], self._circle[1], domain_grid.get(*self._circle) - {value})
                changed = True
        for cell in self._arrow:
            for value in domain_grid.get(*cell):
                curr_domain = domain_grid.get(*cell)
                # Temporarily set the cell to only have the current value
                domain_grid.set(cell[0], cell[1], {value})
                if not any([self._can_make_sum(circle_value, domain_grid) for circle_value in domain_grid.get(*self._circle)]):
                    domain_grid.set(cell[0], cell[1], curr_domain - {value})
                    changed = True
                else:
                    domain_grid.set(cell[0], cell[1], curr_domain)
        return changed


    def _can_make_sum(self, target: int, domain_grid: DomainGrid) -> bool:
        def _can_make_sum_recursive(curr_target: int, curr_arrow_idx: int):
            if curr_target < 0:
                return False
            if curr_arrow_idx == len(self._arrow):
                return curr_target == 0
            for value in domain_grid.get(*self._arrow[curr_arrow_idx]):
                if _can_make_sum_recursive(curr_target - value, curr_arrow_idx + 1):
                    return True
            return False

        return _can_make_sum_recursive(target, 0)
