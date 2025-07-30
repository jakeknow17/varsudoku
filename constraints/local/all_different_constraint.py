from typing import List

from constraints.constraint import Constraint
from structure.defs import Cell
from structure.domain_grid import DomainGrid


class AllDifferentConstraint(Constraint):
    def __init__(self, cells: List[Cell]):
        self._cells = cells

    def propagate(self, domain_grid: DomainGrid) -> bool:
        changed = False
        for cell in self._cells:
            if len(domain_grid.get(*cell)) == 1:
                for other in self._cells:
                    if cell == other:
                        continue
                    singleton_val: int = next(iter(domain_grid.get(*cell)))
                    other_len: int = len(domain_grid.get(*other))
                    domain_grid.set(other[0], other[1], domain_grid.get(*other) - {singleton_val})
                    # If the size of the set changed, we mark it as changed
                    changed = changed or len(domain_grid.get(*other)) < other_len
        return changed
