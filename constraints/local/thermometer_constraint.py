from typing import List

from constraints.constraint import Constraint
from structure.defs import Cell
from structure.domain_grid import DomainGrid


class ThermometerConstraint(Constraint):
    def __init__(self, cells: List[Cell]):
        self._cells = cells

    def propagate(self, domain_grid: DomainGrid) -> bool:
        changed = False
        curr_min = 0
        for r, c in self._cells:
            cell_len = len(domain_grid.get(r, c))
            domain_grid.set(r, c, {x for x in domain_grid.get(r, c) if x > curr_min})
            if len(domain_grid.get(r, c)) > 0:
                curr_min = min(domain_grid.get(r, c))
            changed = changed or len(domain_grid.get(r, c)) < cell_len
        return changed
