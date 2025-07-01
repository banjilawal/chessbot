from dataclasses import dataclass, field

from common.game_default import GameDefault


@dataclass(frozen=True)
class Dimension:

    MIN_LENGTH = 1
    MIN_HEIGHT = 1
    MIN_AREA = MIN_LENGTH * MIN_HEIGHT

    length: int = field(default=GameDefault.OCCUPANT_LENGTH)
    height: int = field(default=GameDefault.OCCUPANT_HEIGHT)

    def area(self) -> int:
        return self.length * self.height