# src/chess/square/dto/builder.py

"""
Module: chess.square.dto.builder
Author: Banji Lawal
Created: 2025-10-21
"""

from chess.coord import CoordDTOBuilder
from chess.square import Square, SquareDTO, SquareValidator
from chess.system import Builder, BuildResult, LoggingLevelRouter


class SquareDTOBuilder(Builder[SquareDTO]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(cls, square: Square) -> BuildResult[SquareDTO]:
        """"""
        method = "SquareDTOBuilder.build"
        
        try:
            validation = SquareValidator.validate(square)
            if validation.is_failure():
                return BuildResult(exception=validation.exception)
            
            return BuildResult(
                payload=SquareDTO(
                    id=square.id,
                    name=square.name,
                    coord_dto=CoordDTOBuilder.build(square.coord)
                )
            )
        
        except Exception as e:
            return BuildResult(exception=e)
