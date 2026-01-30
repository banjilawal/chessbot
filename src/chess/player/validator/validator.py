# src/chess/owner/validator/validator.py

"""
Module: chess.owner.validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from typing import Any, cast

from chess.team import UniqueTeamDataService
from chess.engine.service import EngineService
from chess.system import IdentityService, LoggingLevelRouter, ServiceValidator, ValidationResult, Validator



class PlayerValidator(Validator[Player]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure an Player instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        *   validate: -> ValidationResult[Player]

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
            service_validator: ServiceValidator = ServiceValidator(),
    ) -> ValidationResult[PlayerPlayer]:
        """
        # ACTION:
        1.  Verify the candidate is not null.
        2.  Verify the candidate is an Player. If so cast it to an Player instance.
        3.  Use the identity service to verify the owner's designation and id.
        4.  If the owner is a MachinePlayer, confirm owner.engine_service is not null and
            is an EngineService instance.
        5.  Confirm owner.teams is not null and is an TeamDatabase instance.
        6.  Confirm owner.games is not null and is an UniqueGameDataService instance.
        7.  If any check fails, return the exception inside a ValidationResult.
        8.  When all checks return the successfully validated Player instance inside a ValidationResult.
        
        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)
            *   service_validator (ServiceValidator)

        # RETURNS:
        ValidationResult[Player] containing either:
            - On success: Player in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullPlayerException
            *   InvalidPlayerException
        """
        method = "PlayerValidator.validate"
        try:
            # If candidate does not exist no point continuing
            if candidate is None:
                return ValidationResult.failure(
                    NullPlayerException(f"{method}: {NullPlayerException.DEFAULT_MESSAGE}")
                )
            # Handle the case, the candidate is not an Player object.
            if not isinstance(candidate, PlayerPlayer):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Player, {type(candidate).__name__} instead.")
                )
            # Cast to an Player for additional processing.
            player = cast(PlayerPlayer, candidate)
            
            # Verify the id and designation are safe.
            identity_validation = identity_service.validate_identity(player.id, player.name)
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            # Certify the owner's TeamStackService is correct.
            team_database_core_certification = service_validator.validate(candidate=player.teams)
            if team_database_core_certification.is_failure():
                return ValidationResult.failure(team_database_core_certification.exception)
            
            # Certify the owner's GameStackService is correct.
            game_database_core_certification = service_validator.validate(candidate=player.games)
            if game_database_core_certification.is_failure():
                return ValidationResult.failure(game_database_core_certification.exception)
            
            # If the owner is a MachinePlayer handoff control to certify_machine_player_engine
            # for the final check.
            if isinstance(player, MachinePlayer):
                return cls._certify_machine_player_engine(machine=cast(MachinePlayer, player))
            
            # If the owner is a HumanPlayer all the checks have been passed. Return the
            # owner in the ValidationResult payload.
            if isinstance(player, HumanPlayer):
                return ValidationResult.success(payload=cast(HumanPlayer, player))
            
            # Any unexpected boundary conditions are caught and wrapped in an InvalidPlayerException then,
            # the exception chain is returned inside a ValidationResult. The flow should only get here if
            # the logic does not handle each concrete Player subclass.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPlayerException(ex=ex, message=f"{method}: {InvalidPlayerException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def certify_player_variety(cls, candidate: Any) -> ValidationResult[PlayerVariety]:
        """
        # ACTION:
        This is just a decorator that encapsulates all the logic for making sure an object being
        passed as an PlayerVariety is not null and is actually an PlayerVariety object. The comments
        are almost as lomg as the code.
        
        1.  Verify the candidate is not null.
        2.  Verify the candidate is an PlayerVariety. cast into an PlayerVariety instance and return a success.
        3.  If any check fails, return the exception inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # RETURNS:
        ValidationResult[PlayerVariety] containing either:
            - On success: PlayerVariety in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullPlayerVarietyException
            *   InvalidPlayerVarietyException
        """
        method = "PlayerValidator.certify_variety"
        try:
            # Handle the null case.
            if candidate is None:
                return ValidationResult.failure(
                    PlayerVarietyNullException(f"{method}: {PlayerVarietyNullException.DEFAULT_MESSAGE}")
                )
            #Handle the incorrect type case
            if not isinstance(candidate, PlayerVariety):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected PlayerVariety,  {type(candidate).__name__} instead.")
                )
            # Cast and return.
            return ValidationResult.success(cast(PlayerVariety, candidate))
        
        # If there is unhandled error-raising boundary condition wrap it inside an
        # InvalidPlayerVarietyException then, send the exception chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPlayerVarietyException(
                    ex=ex, message=f"{method}: {InvalidPlayerVarietyException.DEFAULT_MESSAGE}"
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _certify_machine_player_engine(
            cls,
            machine_player: MachinePlayer,
            engine_service_validator: EngineService = EngineService(),
    ) -> ValidationResult[PlayerPlayer]:
        """
        # ACTION:
        1.  If machine.engine_service passes certification, return the machine inside a ValidationResult.
            Otherwise, send the exception in the ValidationResult..

        # PARAMETERS:
            *   machine (MachinePlayer)
            *   engine_service_validator (EngineService)

        # RETURNS:
        ValidationResult[Player] containing either:
            - On success: Player in the payload.
            - On failure: Exception.

        # RAISES:
            *   InvalidMachinePlayerException
        """
        method = "PlayerValidator.certify_machine_player_engine"
        try:
            engine_validation = engine_service_validator.validate_engine(machine_player.engine_service)
            if engine_validation.is_failure():
                return ValidationResult.failure(engine_validation.exception)
            # On success just return the machinePlayer
            return ValidationResult.success(payload=machine_player)
        
        # If there is unhandled error-raising boundary condition wrap it inside an
        # InvalidPlayerMachineException then, send the exception chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidMachinePlayerException(
                    ex=ex, message=f"{method}: {InvalidMachinePlayerException.DEFAULT_MESSAGE}"
                )
            )