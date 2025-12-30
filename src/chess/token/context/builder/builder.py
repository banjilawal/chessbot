# src/chess/token/builder/builder.py

"""
Module: chess.token.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.token import (
    ZeroTokenContextFlagsException, TokenContext, TokenContextBuildFailedException,
    ExcessiveTokenContextFlagsException
)
from chess.coord import Coord, CoordService
from chess.rank import Rank, RankValidator
from chess.system import Builder, BuildResult, UnhandledRouteException, IdentityService, LoggingLevelRouter
from chess.team import Team, TeamValidator


class TokenContextBuilder(Builder[TokenContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce TokenContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of TokenContext instances that can be used safely by the client.
    3.  Ensure params for TokenContext creation have met the application's safety contract.
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
            team_service: TeamValidator = TeamValidator(),
            rank_service: RankValidator = RankValidator(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[TokenContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (row, column, coord) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a TokenContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[int])
                *   team (Optional[Team])
                *   rank (Optional[Rank])
                *   ransom (Optional[int])
                *   coord (Optional[Coord])
                
            These Parameters must be provided:
                *   team_certifier (TeamValidator)
                *   rank_certifier (RankValidator)
                *   coord_service (CoordService)
                *   identity_service (IdentityService)

        # RETURNS:
          BuildResult[TokenContext] containing either:
                - On success: TokenContext in the payload.
                - On failure: Exception.

        # RAISES:
            *   ZeroTokenContextFlagsException
            *   TokenContextBuildFailedException
            *   ExcessiveTokenContextFlagsException
        """
        method = "TokenContextBuilder.builder"
        
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, rank, ransom, coord]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroTokenContextFlagsException(f"{method}: {ZeroTokenContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveTokenContextFlagsException(f"{method}: {ExcessiveTokenContextFlagsException}")
                )
            # After verifying only one PlayerAgent attribute-value-tuple is enabled, validate it.
            
            # Build the id TokenContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_TokenContext in the BuildResult.
                return BuildResult.success(TokenContext(id=id))
            
            # Build the name TokenContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_TokenContext in the BuildResult.
                return BuildResult.success(TokenContext(name=name))
            
            # Build the coord TokenContext if its flag is enabled.
            if coord is not None:
                validation = coord_service.validator.validate(coord)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a coord_TokenContext in the BuildResult.
                return BuildResult.success(TokenContext(coord=coord))
            
            # Build the rank TokenContext if its flag is enabled.
            if rank is not None:
                validation = rank_service.validator.validate(rank)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # On validation success return a rank_TokenContext in the BuildResult.
                return BuildResult.success(TokenContext(rank=rank))
            
            # Build the team TokenContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(team)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_TokenContext in the BuildResult.
                return BuildResult.success(TokenContext(team=team))
            
            # Build the ransom TokenContext if its flag is enabled.
            if ransom is not None:
                validation = rank_service.validator.validate_ransom_in_bounds(ransom)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # On validation success return a ransom_TokenContext in the BuildResult.
                return BuildResult.success(TokenContext(ransom=ransom))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception and wrap A TokenContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                TokenContextBuildFailedException(
                    ex=ex, message=f"{method}: {TokenContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )