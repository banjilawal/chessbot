from abc import abstractmethod, ABC
from dataclasses import field, dataclass


@dataclass
class Rank(ABC):
    movement_strategy: 'MovementStrategy' = field(init=False, repr=False)

    def __post_init__(self):
        # Ensure subclass has set movement_strategy
        if not hasattr(self, 'movement_strategy') or self.movement_strategy is None:
            raise TypeError(f"{self.__class__.__name__} must initialize movement_strategy")