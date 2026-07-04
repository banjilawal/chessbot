# src/builder/player/builder.py

"""
Module: builder.player.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from typing import Optional

from logic.engine import EngineService
from model.state.game import UniqueGameDataService
from logic.team import UniqueTeamDataService
from system import Builder, BuildResult, IdentityService, LoggingLevelRouter, id_emitter

from logic.player import (
    Player, PlayerBuilderException, PlayerVariety, PlayerValidator, HumanPlayer, HumanPlayerBuilderException,
    MachinePlayer, MachinePlayerBuilderException
)


class PlayerFactory(Builder[Player]):
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
    def build(
            cls,
            name: str,
            id: id_emitter.player_id,
            player_variety: PlayerVariety,
            engine_service: Optional[EngineService] = None,
            player_validator: PlayerValidator = PlayerValidator(),
    ) -> BuildResult[HumanPlayer|MachinePlayer]:
        """
        # ACTION:
        1.  verify player_variety is a not-null PlayerVariety object.
        2.  Use player_variety to pick which build method will create the concrete Player object.

        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   player_variety (PlayerVariety)
            *   engine_service (Optional[EngineService])

        # RETURNS:
        ValidationResult[Player] containing either:
            - On success: Player in the payload.
            - On failure: Exception.

        Raises:
            *   PlayerBuilderException
        """
        method = "PlayerBuilder.build"
        try:
            # Ensure the player_variety is the correct type and not null.
            variety_validation = player_validator.certify_player_variety(candidate=player_variety)
            if variety_validation.failure():
                return BuildResult.failure(variety_validation.exception)
            # Use player_variety to decide which build method to call.
            
            if isinstance(player_variety, HumanPlayer):
                return cls.build_human_player(id=id, name=name,)
            
            # Machine owner requires an engine_service.
            if isinstance(player_variety, MachinePlayer):
                return cls.build_machine_player(id=id, name=name, engine_service=engine_service)
        
        # The flow should only get here if the logic did not route all the types of concrete Players.
        # In that case wrap the unhandled exception inside an PlayerBuilderException then, return
        # the exception chain inside a ValidationResult.
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                PlayerBuilderException(
                    ex=ex, msg=f"{method}: {PlayerBuilderException.MSG}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_human_player(
            cls,
            id: int,
            name: str,
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[HumanPlayer]:
        """
        # ACTION:
        1.  On successfully certifying the id and designation create HumanPlayer and return in BuildResult's
            payload. Otherwise, return a BuildResult containing an exception.

        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   identity_service (IdentityService)

        # RETURNS:
        ValidationResult[HumanPlayer] containing either:
            - On success: HumanPlayer in the payload.
            - On failure: Exception.

        Raises:
            *   HumanPlayerBuilderException
        """
        method = "PlayerBuilder.build_human_player"
        try:
            # Only need to certify the designation and id are correct.
            validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            # On success return the HumanPlayer in a BuildResult payload.
            return BuildResult.success(
                payload=HumanPlayer(
                    id=id,
                    name=name,
                    games=UniqueGameDataService(),
                    teams=UniqueTeamDataService(),
                )
            )
        
        # Finally, if some exception unrelated to identity verification is raised wrap it inside a
        # HumanPlayerBuilderException then, send the exception chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                HumanPlayerBuilderException(
                    ex=ex, msg=f"{method}: {HumanPlayerBuilderException.MSG}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_machine_player(
            cls,
            name: str,
            id: int = id_emitter.service_id,
            engine_service: EngineService = EngineService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[MachinePlayer]:
        """
        # ACTION:
        1.  Certifying the id and designation and designation are safe with identity_service.
        2.  Use engine_service_validator to ensure the engine_service has all the required components.

        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   engine_service (EngineService)
            *   identity_service (IdentityService)
            *   engine_service_validator (EngineServiceValidator)

        # RETURNS:
        ValidationResult[MachinePlayer] containing either:
            - On success: MachinePlayer in the payload.
            - On failure: Exception.

        Raises:
            *   MachinePlayerBuilderException
        """
        method = "PlayerBuilder.build_machine_player"
        try:
            # Certify the id and designation are safe.
            identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            # Certify the engine_service has all the required components
            engine_service_validation = engine_service.validate.search_service(candidate=engine_service)
            if engine_service_validation.is_failure():
                return BuildResult.failure(engine_service_validation.exception)
            # When all checks pass send a MachinePlayer back.
            return BuildResult.success(
                MachinePlayer(
                    id=id,
                    name=name,
                    engine_service=engine_service,
                    games=UniqueGameDataService(),
                    teams=UniqueTeamDataService(),
                )
            )
        
        # Finally, if some exception unrelated to identity verification is raised wrap it inside a
        # MachinePlayerBuilderException then, send the exception chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                MachinePlayerBuilderException(
                    ex=ex, msg=f"{method}: {MachinePlayerBuilderException.MSG}"
                )
            )
