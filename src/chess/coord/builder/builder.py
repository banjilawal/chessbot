# src/chess/coord/builder/builder.py

"""
Module: chess.coord.builder.builder
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""


from chess.system import Builder, BuildResult, LoggingLevelRouter, NumberInBoundsValidator
from chess.coord import Coord, CoordValidator,  CoordBuildFailedException



class CoordBuilder(Builder[Coord]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor
     
     # RESPONSIBILITIES:
     1.  Produce Coord instances whose integrity is always guaranteed.
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
            number_bonds_validator: NumberInBoundsValidator = NumberInBoundsValidator(),
    ) -> BuildResult[Coord]:
        """
        # ACTION:
        1.  Use the validator to verify the row and column are within the bounds of the Board's 2D array.
        3.  If any check fails snd the exception in the BuildResult. Else, Create a Coord object and send in the
            BuildResult.

        # PARAMETERS:
            *   row (int)
            *   column (int)
            *   number_bonds_validator (NumberInBoundsValidator)

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        # RAISES:
            *   CoordBuildFailedException
        """
        method = "CoordBuilder.builder"
        try:
            # Test the row parameter is between 0 and BOARD_DIMENSION - 1 inclusive.
            row_validation = number_bonds_validator.validate(candidate=row)
            if row_validation.is_failure:
                return BuildResult.failure(row_validation.exception)
            # Test the column parameter is between 0 and BOARD_DIMENSION - 1 inclusive.
            column_validation = number_bonds_validator.validate(candidat=column)
            if column_validation.is_failure:
                return BuildResult.failure(column_validation.exception)
            # If both checks are passed create a Coord and return in the BuildResult.
            return BuildResult.success(payload=Coord(row=row, column=column))
        
        # Finally, if there is an unhandled exception Wrap an CoordBuildFailedException around it then return the
        # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordBuildFailedException(ex=ex, message=f"{method}: {CoordBuildFailedException.DEFAULT_MESSAGE}")
            )