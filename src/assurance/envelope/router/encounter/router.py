# src/assurance/envelope/router/encounterr.py

"""
Module: assurance.envelope.router.encounterr
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import EncounterValidatorToolkit, KillEncounterValidator, EnvelopeRouter
from domain import Encounter
from err import NullException
from transit import EncounterCarrier, RootEncounterEnvelope
from util import LoggingLevelRouter


class EncounterValidationRouter(EnvelopeRouter[Encounter]):
    """
    Role
        - Router

    Responsibilities:
        1.  Select the validator which matches Encounter type.

    Attributes:
        toolkit: EncounterValidatorToolkit
        kill_validator: KillEncounterValidator
        checkmate_validator: CheckmateEncounterValidator
        stalemate_validator: StalemateEncounterValidator

    Provides:
        -   def execute(
                    id: int,
                    team: Team,
                    formation: Formation,
                    home_square: HomeSquare,
                    deployment: EncounterDeployment,
                    prime_extract: EncounterPrimeExtract,
            ) -> ValidationResult[EncounterCarrier]:

    Super Class:
    """
    
    _toolkit: EncounterValidatorToolkit
    _kill_validator: KillEncounterValidator
    _warning_validator: EncounterWarningValidator
    _checkmate_validator: CheckmateEncounterValidator
    _stalemate_validator: StalemateEncounterValidator

    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
            kill_validator: Optional[KillEncounterValidator] | None = None,
            warning_validator: Optional[EncounterWarningValidator] | None = None,
            checkmate_validator: Optional[CheckmateEncounterValidator] | None = None,
            stalemate_validator: Optional[StalemateEncounterValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
            kill_validator: Optional[KillEncounterValidator]
            warning_validator: Optional[EncounterWarningValidator]
            checkmate_validator: Optional[CheckmateEncounterValidator]
            stalemate_validator: Optional[StalemateEncounterValidator]
        """
        self._toolkit=toolkit or EncounterValidatorToolkit()
        self._kill_validator = kill_validator or KillEncounterValidator()
        self._checkmate_validator = checkmate_validator or CheckmateEncounterValidator()
        self._stalemate_validator = stalemate_validator or StalemateEncounterValidator()
    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult no route exists
                for the Encounter type.
            2.  Otherwise, send a EncounterCarrier in the success result.
        Args:
            envelope: RootEncounterEnvelope            
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
            EncounterValidationRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        prime_extract = envelope.prime_extract
        carrier = prime_extract.reference
        
        if carrier.is_empty:
            return ValidationResult.failure(
                EncounterValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationRouterException.MSG,
                    err_code=EncounterValidationRouterException.ERR_CODE,
                    ex=EncounterValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterValidationRouterException.MSG,
                        err_code=EncounterValidationRouterException.ERR_CODE,
                    )
                )
            )
        if carrier.is_not_consistent:
            return ValidationResult.failure(
                EncounterValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationRouterException.MSG,
                    err_code=EncounterValidationRouterException.ERR_CODE,
                    ex=EncounterValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterValidationRouterException.MSG,
                        err_code=EncounterValidationRouterException.ERR_CODE,
                    )
                )
            )
        validation_result = ValidationResult.failure(NullException())
        
        if carrier.is_kill_encounter_carrier:
            validation_result = self._kill_validator.execute(candidate=envelope)
            
        reference = validation_reference.prime_extract.reference
        
        result = ValidationResult.failure(EncounterValidationRouterException())
        # --- Select the appropriate validation route. ---#
        # KillEncounter validation route.
        if reference.is_kill_encounter_carrier:
            raw = cast(KillEncounterBlueprint, encounter_blueprint)
            kill_blueprint = KillEncounterBlueprint(
                id=id,
                team=team,
                formation=formation,
                deployment=deployment,
                home_square=home_square,
                position=position,
                previous_position=previous_position,
                readiness=raw.readiness,
                checkmate=raw.checkmate,
                check_warning=raw.check_warning,
            )
            kill_carrier = cast(KillEncounterCarrier, reference)
            kill_prime_extract = KillEncounterPrimeExtract(
                carrier=kill_carrier,
                blueprint=kill_blueprint
            )
            return self._kill_validator.execute(
                prime_extract=kill_prime_extract
            )

        # CheckmateEncounter validation route.
        if reference.is_checkmate_encounter_carrier:
            return self._checkmate_validator.execute(
                validation_reference=validation_reference
            )
        # StalemateEncounter validation route.
        if reference.is_stalemate_encounter_carrier:
            return  self._stalemate_validator.execute(
                reference=validation_reference
            )
        # Handle the case that the carrier is not consistent.
        return ValidationResult.failure(
            EncounterValidationRouterException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=EncounterValidationRouterException.MSG,
                err_code=EncounterValidationRouterException.ERR_CODE,
                ex=EncounterValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationRouterException.MSG,
                    err_code=EncounterValidationRouterException.ERR_CODE,
                )
            )
        )


    