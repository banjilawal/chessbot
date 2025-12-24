# src/chess/square/builder/builder.py

"""
Module: chess.square.builder.builder
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import Optional

from chess.board import Board
from chess.coord import Coord, CoordService
from chess.system import Builder, BuildResult, UnhandledRouteException, IdentityService
from chess.square import (
    ZeroSquareContextFlagsException, SquareContext, SquareContextBuildFailedException,
    ExcessiveSquareContextFlagsException
)


class SquareContextBuilder(Builder[SquareContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce TeamContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of TeamContext instances that can be used safely by the client.
    3.  Ensure params for TeamContext creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            board: Optional[Board] = None,
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[SquareContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, name, coord, board) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a SnapshotContext and send in a BuildResult. Else, return an exception
                in the BuildResult.


        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   null Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
                
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   identity_service (IdentityService)

        # Returns:
        ValidationResult[Square] containing either:
            - On success: Square in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroSnapshotContextFlagsException
            *   SnapshotContextBuildFailedException
            *   ExcessiveSnapshotContextFlagsException
        """
        method = "SquareContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, coord]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Squares match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroSquareContextFlagsException(f"{method}: {ZeroSquareContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveSquareContextFlagsException(
                        f"{method}: {ExcessiveSquareContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # After verifying only one Square attribute-value-tuple is enabled, validate it.
            
            # Build the id SquareContext if its flag is enabled.
            if id is not None:
                id_validation = identity_service.validate_id(candidate=id)
                if id_validation.is_failure:
                    return BuildResult.failure(id_validation.exception)
                # On validation success return an id_SquareContext in the BuildResult.
                return BuildResult.success(SquareContext(id=id))
            
            # Build the name SquareContext if its flag is enabled.
            if name is not None:
                name_validation = identity_service.validate_name(candidate=name)
                if name_validation.is_failure:
                    return BuildResult.failure(name_validation.exception)
                # On validation success return a name_SquareContext in the BuildResult.
                return BuildResult.success(SquareContext(name=name))
            
            # Build the coord SquareContext if its flag is enabled.
            if coord is not None:
                coord_validation = coord_service.validator.validate(coord)
                if coord_validation.is_failure:
                    return BuildResult.failure(coord_validation.exception)
                # On validation success return a coord_SquareContext in the BuildResult.
                return BuildResult.success(SquareContext(coord=coord))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception and wrap A SquareContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                SquareContextBuildFailedException(
                    ex=ex, message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )