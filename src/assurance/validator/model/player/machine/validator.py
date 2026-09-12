# src/assurance/validator/model/player/machine/validator.py

"""
Module: assurance.validator.model.player.machine.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import PlayerValidatorToolkit
from domain import (
    Formation, MachineReadiness, MachinePlayer, HomeSquare, MachinePlayerBlueprint, Name, NameValidationRequest, PlayerDeployment,
    PlayerReadiness
)
from err import (
    FormationNullException, MachinePlayerValidatorException, NullException, NameCarrierEmptyException,
    PlayerCarrierEmptyException
)
from transit import MachineCarrier, NameCarrier
from util import IdFactory, LoggingLevelRouter


class MachinePlayerValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: PlayerValidationToolkit

    Provides:
        -   def execute(validated_carrier: MachineCarrier) -> ValidationResult[MachineCarrier]

    Super Class:
    """
    _toolkit: PlayerValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[PlayerValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerValidationToolkit]
        """
        self._toolkit=toolkit or PlayerValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(self, validated_carrier: MachineCarrier) -> ValidationResult[MachineCarrier]:
        """
        Send a validated MachinePlayer or Blueprint which inside the validated
        MachineCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The carrier is empty.
                    - The id check fails.
                    - The name check fails.
                    - The formation is null or the wrong type.
                    - The readiness is null or the wrong type.
                    - the deployment is null or the wrong type.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            validated_carrier: MachineCarrier
        Returns:
            ValidationResult[MachineCarrier]
        Raises:
            MachinePlayerValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachinePlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachinePlayerValidatorException.MSG,
                    err_code=MachinePlayerValidatorException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self._toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self._toolkit.metadata.types.blueprint,
            blueprint_null_exception=self._toolkit.metadata.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachinePlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachinePlayerValidatorException.MSG,
                    err_code=MachinePlayerValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the name does not pass a validation check.
        name_validation = self._toolkit.helper.identity_service.validate_name(
            blueprint.name
        )
        if name_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachinePlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachinePlayerValidatorException.MSG,
                    err_code=MachinePlayerValidatorException.ERR_CODE,
                    ex=name_validation.exception,
                )
            )
        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        name = cast(str, name_validation.payload)
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case.
        if validated_carrier.is_carrying_model:
            model = MachinePlayer(
                id=id,
                name=name,
            )
            model.adviser = blueprint.adviser
            return ValidationResult.success(MachineCarrier(model=model))
        # Else the blueprint case
        return ValidationResult.success(
            MachineCarrier(
                blueprint=MachinePlayerBlueprint(
                    id=id,
                    name=name,
                    adviser=blueprint.adviser,
            )
        )
    )
    
    