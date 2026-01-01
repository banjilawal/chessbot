# src/chess/token/builder/builder.py

"""
Module: chess.token.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.rank import Rank, RankService
from chess.team import Team, TeamService
from chess.coord import Coord, CoordService
from chess.system import (
    BoundNumberValidator, Builder, BuildResult, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
)
from chess.token import (
    ExcessiveTokenContextFlagsException, TokenContext, TokenContextBuildFailedException,
    TokenContextBuildRouteException, ZeroTokenContextFlagsException
)


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
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
            bound_number_validator: BoundNumberValidator = BoundNumberValidator(),
    ) -> BuildResult[TokenContext]:
        """
        # ACTION:
            1.  If only one, optional param is not null send an exception in the BuildResult.
            2.  If there is no build path for the TokenContext key send and exception in the BuildResult. Else,
                route to the appropriate build route.
            3.  If the key's value fails validation send the exception in the BuildResult. Else, build the TeamContext
                in the BuildResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[int])
                *   team (Optional[Team])
                *   rank (Optional[Rank])
                *   ransom (Optional[int])
                *   coord (Optional[Coord])
                *   color (Optional[GameColor])
            These Parameters must be provided:
                *   team_service (TeamService)
                *   rank_service (RankService)
                *   coord_service (CoordService)
                *   color_validator (GameColorValidator)
                *   identity_service (IdentityService)
        # RETURNS:
          *     BuildResult[TokenContext] containing either:
                    - On failure: Exception.
                    - On success: TokenContext in the payload.
        # RAISES:
            *   ZeroTokenContextFlagsException
            *   TokenContextBuildFailedException
            *   ExcessiveTokenContextFlagsException
            *   TokenContextBuildFailedException
            *   TokenContextBuildRouteException
        """
        method = "TokenContextBuilder.builder"
        
        # Count how many optional parameters are not-null. One param needs to be not-null.
        params = [id, designation, team, rank, ransom, coord, color]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuildFailedException(
                    message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                    ex=ZeroTokenContextFlagsException(f"{method}: {ZeroTokenContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuildFailedException(
                    message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                    ex=ExcessiveTokenContextFlagsException(f"{method}: {ExcessiveTokenContextFlagsException}")
                )
            )
        
        #--- Route to the appropriate validation/build branch. ---#
        
        # Build the id TokenContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(id=id))
        
        # Build the designation TokenContext if its flag is enabled.
        if designation is not None:
            validation = identity_service.validate_name(designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a designation_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(designation=designation))
        
        # Build the coord TokenContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.validator.validate(coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(coord=coord))
        
        # Build the rank TokenContext if its flag is enabled.
        if rank is not None:
            validation = rank_service.validator.validate(rank)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a rank_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(rank=rank))
        
        # Build the team TokenContext if its flag is enabled.
        if team is not None:
            validation = team_service.validator.validate(team)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a team_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(team=team))
        
        # Build the color TokenContext if its flag is enabled.
        if color is not None:
            validation = color_validator.validate(color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a team_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(color=color))
        
        # Build the ransom TokenContext if its flag is enabled.
        if ransom is not None:
            validation = bound_number_validator.validate(
                candidate=ransom,
                floor=rank_service.persona_service.min_ransom,
                ceiling=rank_service.persona_service.max_ransom
            )
            # Return the exception chain on failure.
            if validation.is_failure:
                return BuildResult.failure(
                    TokenContextBuildFailedException(
                        message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_TokenContext in the BuildResult.
            return BuildResult.success(TokenContext(ransom=ransom))
        
        # The default path returns failure
        return BuildResult.failure(
            TokenContextBuildFailedException(
                message=f"{method}: {TokenContextBuildFailedException.ERROR_CODE}",
                ex=TokenContextBuildRouteException(f"{method}: {TokenContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )
