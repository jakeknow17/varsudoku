
from abc import ABC, abstractmethod

from structure.domain_grid import DomainGrid


class Constraint(ABC):

    @abstractmethod
    def propagate(self, domain_grid: DomainGrid) -> bool:
        pass