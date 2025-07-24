from typing import Optional

from chess.common.geometry import Coordinate
from chess.motion.definition.definition import Definition
from chess.motion.definition.definition_category import DefinitionCategory
from chess.team.home import TeamHome


class PawnDefintion(Definition):
    def __init__(self, definition_category: DefinitionCategory.PAWN, team: TeamHome):
        if not definition_category == DefinitionCategory.PAWN:
            raise ValueError("definition_category must be pawn")
        super.__init__(self, id=definition_category.id, title=definition_category.value)
    def line_fits_definition(self, origin: Coordinate, destination: Coordinate, team: Optional[TeamHome] ) -> bool:
        return origin.column = destination.column and origin.row + 1 == destination.row
