# chess/point/old_occupation_validator.py

"""
Module: `chess.point.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

Contains: CoordBuilder
 Provides: Create `Coord` instances 
"""
from chess.coord.dto import CoordDTO
from chess.coord import Coord, CoordValidator
from chess.system import Builder, BuildResult, LoggingLevelRouter



class CoordDTOBuilder(Builder[CoordDTO]):

    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, coord: Coord) -> BuildResult[CoordDTO]:
        """"""
        method = "CoordDTOBuilder.build"
        
        try:
            validation = CoordValidator.validate(coord)
            if validation.is_failure():
                return BuildResult(exception=validation.exception)
        
            return BuildResult(payload=CoordDTO(row=coord.row, column=coord.column))
        
        except Exception as e:
            return BuildResult(exception=e)
