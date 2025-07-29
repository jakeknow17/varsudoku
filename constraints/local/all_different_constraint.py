from typing import List

from constraints.constraint import Constraint
from structure.defs import Cell
from structure.domain_grid import DomainGrid


class AllDifferentConstraint(Constraint):
    def __init__(self, cells: List[Cell]):
        self._cells = cells

    def propagate(self, domain_grid: DomainGrid) -> bool:
        changed = False
        for r, c in self._cells:
            if len(domain_grid.get(r, c)) == 1:
                for other_r, other_c in self._cells:
                    if (r, c) == (other_r, other_c):
                        continue
                    singleton_val: int = next(iter(domain_grid.get(r, c)))
                    other_len: int = len(domain_grid.get(other_r, other_c))
                    domain_grid.set(other_r, other_c, domain_grid.get(other_r, other_c) - {singleton_val})
                    # If the size of the set changed, we mark it as changed
                    changed = changed or len(domain_grid.get(other_r, other_c)) < other_len
        return changed
