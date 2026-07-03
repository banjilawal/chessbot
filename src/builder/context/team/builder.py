# src/builder/context/team/builder.py

"""
Module: builder.context.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class TeamContextBuilder(Builder[TeamContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
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
        Raises:
            *   ZeroTeamContextFlagsException
            *   TeamContextBuilderException
            *   ArenaTeamContextFlagsException
        """
        method = "PieceSearchContextBuilder.build"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, arena, player, color]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamContextBuilderException(
                    msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                    ex=ZeroTeamContextFlagsException(f"{method}: {ZeroTeamContextFlagsException.ERR_CODE}")
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamContextBuilderException(
                    msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                    ex=ArenaTeamContextFlagsException(f"{method}: {ArenaTeamContextFlagsException}")
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id TeamContext if its flag is set.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuilderException(
                        msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(id=id))
        
        # Build the owner TeamContext if its flag is enabled.
        if player is not None:
            validation = player_service.validator.execute(candidate=player)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuilderException(
                        msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a player_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(player=player))
        
        # Build the arena TeamContext if its flag is enabled.
        if arena is not None:
            validation = arena_service.item_validator.search_service(candidate=arena)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuilderException(
                        msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an arena_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(arena=arena))
        
        # Build the color TeamContext if its flag is enabled.
        if color is not None:
            validation = color_validator.execute(candidate=color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TeamContextBuilderException(
                        msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a color_TeamContext in the BuildResult.
            return BuildResult.success(payload=TeamContext(color=color))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            TeamContextBuilderException(
                msg=f"{method}: {TeamContextBuilderException.ERR_CODE}",
                ex=TeamContextBuildRouteException(f"{method}: {TeamContextBuildRouteException.ERR_CODE}")
            )
        )