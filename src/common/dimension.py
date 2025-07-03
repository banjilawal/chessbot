from dataclasses import dataclass

@dataclass(frozen=True)
class Dimension:

    MIN_LENGTH = 1
    MIN_HEIGHT = 1
    MIN_AREA = MIN_LENGTH * MIN_HEIGHT

    length: int
    height: int

    def area(self) -> int:
        return self.length * self.height