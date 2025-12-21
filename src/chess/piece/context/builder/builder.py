# src/chess/piece/map/builder/builder.py

"""
Module: chess.piece.map.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.piece import (
    ZeroPieceContextFlagsException, PieceContext, PieceContextBuildFailedException,
    ExcessivePieceContextFlagsException
)
from chess.coord import Coord, CoordService
from chess.rank import Rank, RankCertifier
from chess.system import Builder, BuildResult, FailsafeBranchExitPointException, IdentityService, LoggingLevelRouter
from chess.team import Team, TeamCertifier


class PieceContextBuilder(Builder[PieceContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce PieceContext instances whose integrity is always guaranteed.
    2.  Manage construction of PieceContext instances that can be used safely by the client.
    3.  Ensure params for PieceContext creation have met the application's safety contract.
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
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
            team_service: TeamCertifier = TeamCertifier(),
            rank_service: RankCertifier = RankCertifier(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[PieceContext]:
        """
        # Action:
            1.  Confirm that only one in the (row, column, coord) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a PieceContext and send in a BuildResult. Else, send an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[int])
                *   team (Optional[Team])
                *   rank (Optional[Rank])
                *   ransom (Optional[int])
                *   coord (Optional[Coord])
                
            These Parameters must be provided:
                *   team_certifier (TeamCertifier)
                *   rank_certifier (RankCertifier)
                *   coord_service (CoordService)
                *   identity_service (IdentityService)

        # Returns:
          BuildResult[PieceContext] containing either:
                - On success: PieceContext in the payload.
                - On failure: Exception.

        # Raises:
            *   ZeroPieceContextFlagsException
            *   PieceContextBuildFailedException
            *   ExcessivePieceContextFlagsException
        """
        method = "PieceContextBuilder.builder"
        
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, rank, ransom, coord]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroPieceContextFlagsException(f"{method}: {ZeroPieceContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessivePieceContextFlagsException(f"{method}: {ExcessivePieceContextFlagsException}")
                )
            # After verifying only one PlayerAgent attribute-value-tuple is enabled, validate it.
            
            # Build the id PieceContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_PieceContext in the BuildResult.
                return BuildResult.success(PieceContext(id=id))
            
            # Build the name PieceContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_PieceContext in the BuildResult.
                return BuildResult.success(PieceContext(name=name))
            
            # Build the coord PieceContext if its flag is enabled.
            if coord is not None:
                validation = coord_service.validator.validate(coord)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a coord_PieceContext in the BuildResult.
                return BuildResult.success(PieceContext(coord=coord))
            
            # Build the rank PieceContext if its flag is enabled.
            if rank is not None:
                validation = rank_service.validator.validate(rank)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # On validation success return a rank_PieceContext in the BuildResult.
                return BuildResult.success(PieceContext(rank=rank))
            
            # Build the team PieceContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(team)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_PieceContext in the BuildResult.
                return BuildResult.success(PieceContext(team=team))
            
            # Build the ransom PieceContext if its flag is enabled.
            if ransom is not None:
                validation = rank_service.validator.validate_ransom_in_bounds(ransom)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # On validation success return a ransom_PieceContext in the BuildResult.
                return BuildResult.success(PieceContext(ransom=ransom))
            
            # As a failsafe send a buildResult failure if a map path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, if there is an unhandled exception Wrap a PieceContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                PieceContextBuildFailedException(
                    ex=ex, message=f"{method}: {PieceContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )