# src/chess/team/context/builder/builder.py

"""
Module: chess.team.context.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.arena import Arena, ArenaService
from chess.player import Player, PlayerService
from chess.system import Builder, BuildResult,  GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
from chess.team import (
    TeamContext, TeamContextBuildFailedException, ExcessiveTeamContextFlagsException, TeamContextBuildRouteException,
    ZeroTeamContextFlagsException
)


class TeamContextBuilder(Builder[TeamContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

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
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            arena: Optional[Arena] = None,
            player: Optional[Player] = None,
            color: Optional[GameColor] = None,
            arena_service: ArenaService = ArenaService(),
            player_service: PlayerService = PlayerService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[TeamContext]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the BuildResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the BuildResult. Else, create the TeamContext with attribute-value tuple to send in the BuildResult.
        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[int])
                8   arena (Optional[Arena])
                *   owner (Optional[Player])
                *   color (Optional[ArenaColor])
            These Parameters must be provided:
                *   arena_service (ArenaService)
                *   player_certifier (PlayerService)
                *   identity_service (IdentityService)
                *   schema_validator (TeamSchemaValidator)
        # RETURNS:
            *   BuildResult[TeamContext] containing either:
                    - On failure: Exception.
                    - On success: TeamContext in the payload.
        # RAISES:
            *   ZeroTeamContextFlagsException
            *   TeamContextBuildFailedException
            *   ExcessiveTeamContextFlagsException
        """
        method = "PieceSearchContextBuilder.builder"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, arena, player, color]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                    ex=ZeroTeamContextFlagsException(f"{method}: {ZeroTeamContextFlagsException.ERROR_CODE}")
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                    ex=ExcessiveTeamContextFlagsException(f"{method}: {ExcessiveTeamContextFlagsException}")
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id TeamContext if its flag is set.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuildFailedException(
                        message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(id=id))
        
        # Build the owner TeamContext if its flag is enabled.
        if player is not None:
            validation = player_service.validator.validate(candidate=player)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuildFailedException(
                        message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a player_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(player=player))
        
        # Build the arena TeamContext if its flag is enabled.
        if arena is not None:
            validation = arena_service.item_validator.validate(candidate=arena)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuildFailedException(
                        message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an arena_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(arena=arena))
        
        # Build the color TeamContext if its flag is enabled.
        if color is not None:
            validation = color_validator.validate(candidate=color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuildFailedException(
                        message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a color_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(color=color))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            TeamContextBuildFailedException(
                message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                ex=TeamContextBuildRouteException(f"{method}: {TeamContextBuildRouteException.ERROR_CODE}")
            )
        )