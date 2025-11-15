# chess/square/builder.py

"""
Module: chess.square.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""


from chess.coord import Coord, CoordService
from chess.square import Square, SquareBuildFailedException
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter



class SquareBuilder(Builder[Square]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Square instances whose integrity is always guaranteed. If any attributes do not pass their integrity
    checks, send an exception instead.

    # PROVIDES:
    BuildResult[Square] containing either:
        - On success: Coord in payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            id: int,
            name: str,
            coord: Coord,
            coord_service: type[CoordService] = CoordService,
            identity_service: type[IdentityService] = IdentityService
    ) -> BuildResult[Square]:
        """
        # ACTION:
        1.  Run identity-integrity checks with identity_service.
        2.  Ron coord-integrity checks with coord_service.
        3.  If any checks fail, send their exception to the caller in a BuildResult.
        4.  When all checks pass, create a new Square object then send to the caller in a BuildResult.
    
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   coord (coord)
            *   coord_service (type[CoordService]): validates coord.
            *   identity_service (type[IdentityService]): validates id and name.
    
        # Returns:
        ValidationResult[Square] containing either:
            - On success: Square in payload.
            - On failure: Exception.
    
        # Raises:
            *   SquareBuildFailedException
        """
        method = "SquareBuilder.build"
        
        try:
            identity_validation = identity_service.validate_identity(
                id_candidate=id,
                name_candidate=name
            )
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            coord_validation = coord_service.validate_as_coord(coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            return BuildResult(payload=Square(id=id, name=name, coord=coord))
        
        except Exception as ex:
            return BuildResult(
                SquareBuildFailedException(
                    f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )