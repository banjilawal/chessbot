class Rank(ABC):
    @property
    @abstractmethod
    def movement_strategy(self) -> 'PieceStrategy':
        """Return the movement strategy associated with this rank."""
        pass