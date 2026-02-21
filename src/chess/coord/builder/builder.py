# src/chess/coord/builder/builder.py

"""
Module: chess.coord.builder.builder
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""


from chess.system import BOARD_DIMENSION, Builder, BuildResult, LoggingLevelRouter, NumberValidator
from chess.coord import Coord, CoordBuildException



class CoordBuilder(Builder[Coord]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor
     
     # RESPONSIBILITIES:
     1.  Produce Coord instances whose integrity is guaranteed at creation.
     2.  Ensure params for Coord creation have met the application's safety contract.
     3.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
     None

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: int,
            column: int,
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[Coord]:
        """
        # ACTION:
            1.  Use the validator to verify the row and column are within the bounds of the Board's 2D array.
            2.  If any check fails snd the exception in the BuildResult. Else, create a Coord object and send in the
                BuildResult.
        # PARAMETERS:
            *   row (int)
            *   column (int)
            *   number_bonds_validator (NumberValidator)
        # RETURNS:
            *   BuildResult[Coord] containing either:
                    - On success: Coord in the payload.
                    - On failure: Exception.
        # RAISES:
            *   CoordBuildException
        """
        method = "CoordBuilder.builder"
        
        # Handle the case that the row param is not certified safe
        row_validation = number_validator.validate(candidate=row, floor=0, ceiling=BOARD_DIMENSION-1)
        if row_validation.is_failure:
            # Return the validation chain on failure.
            return BuildResult.failure(
                CoordBuildException(
                    message=f"{method}: {CoordBuildException.DEFAULT_MESSAGE}",
                    ex=row_validation.exception
                )
            )
        # Handle the case that the row param is not certified safe
        column_validation = number_validator.validate(candidate=column, floor=0, ceiling=BOARD_DIMENSION-1)
        if column_validation.is_failure:
            # Return the validation chain on failure.
            return BuildResult.failure(
                CoordBuildException(
                    message=f"{method}: {CoordBuildException.DEFAULT_MESSAGE}",
                    ex=column_validation.exception
                )
            )
        # If both checks are passed create a Coord and return in the BuildResult.
        return BuildResult.success(payload=Coord(row=row, column=column))
