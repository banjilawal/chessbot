# src/validator/model/maneuver/validator.py

"""
Module: validator.model.maneuver.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import ManeuverValidatorToolkit, ModelValidator
from domain import ManeuverValidationRequest
from err import EmptyManeuverCarrierException, ManeuverValidationRequestNullException, ManeuverValidatorException
from domain.model import Maneuver
from artifcat import ValidationResult
from operation.toolkit import ManeuverToolkit
from transit import ManeuverCarrier
from util import LoggingLevelRouter


class ManeuverValidator(ModelValidator[Maneuver]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ManeuverCarrier and its contents are safe before use.

    Attributes:
        toolkit: ManeuverValidatorToolkit

    Provides:
        *   def execute(candidate: Any) -> ValidationResult[ManeuverCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[ManeuverValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ManeuverValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ManeuverValidatorToolkit())
    
    @property
    def toolkit(self) -> ManeuverValidatorToolkit:
        return cast(ManeuverValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ManeuverCarrier]:
        """
        Certify a ManeuverCarrier's payload is either a Maneuver or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a ManeuverValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a ManeuverCarrier
                            an empty ManeuverCarrier.
                    *   Either the id, board, or owner attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ManeuverCarrier]
        Raises:
            ManeuverValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            target_model=ManeuverValidationRequest,
            null_exception=ManeuverValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        request = cast(ManeuverValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Extract the blueprint from the validated carrier. ---#
        carrier = cast(ManeuverCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        # Handle the case that the carrier does not produce a Blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=EmptyManeuverCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyManeuverCarrierException.MSG,
                        err_code=EmptyManeuverCarrierException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the archetype does not pass a validation check.
        archetype_validation = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.archetype,
            target_model=Archetype,
            null_exception=ArchetypeNullException(),
        )
        if archetype_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=archetype_validation.exception,
                )
            )
        # --- Run the board validation checks. ---#
        board_validation = self.toolkit.helper.board_validator.execute(
            candidate=BoardValidationRequest(
                id=IdFactory.next_id(class_name="BoardValidationRequest"),
                item=BoardCarrier(model=blueprint.board),
            )
        )
        # Handle the case that the board is flagged.
        if board_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # --- Extract the board validation payload. ---#
        board_carrier = cast(
            BoardCarrier,
            board_validation.payload
        )
        # Handle the case that the board_carrier does not contain a model.
        if not board_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=EmptyBoardCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyBoardCarrierException.MSG,
                        err_code=EmptyBoardCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Run the owner validation checks. ---#
        owner_validation = self.toolkit.helper.owner_validator.execute(
            candidate=PlayerValidationRequest(
                id=IdFactory.next_id(class_name="PlayerValidationRequest"),
                item=PlayerCarrier(model=blueprint.owner)
            )
        )
        # Handle the case that the owner is flagged.
        if owner_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=owner_validation.exception,
                )
            )
        # --- Extract the owner validation payload. ---#
        owner_carrier = cast(
            PlayerCarrier,
            owner_validation.payload
        )
        # Handle the case that the owner_carrier does not contain a model.
        if not owner_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=EmptyPlayerCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyPlayerCarrierException.MSG,
                        err_code=EmptyPlayerCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        board = cast(Board, board_carrier.entity)
        owner = cast(Player, owner_carrier.entity)
        archetype = cast(Archetype, archetype_validation.payload)
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.is_carrying_model:
            payload = Maneuver(
                id=id,
                board=board,
                owner=owner,
                archetype=archetype,
            )
            return ValidationResult.success(ManeuverCarrier(model=payload))
        # The blueprint case
        payload = ManeuverBlueprint(
            id=id,
            board=board,
            owner=owner,
            archetype=archetype,
        )
        return ValidationResult.success(ManeuverCarrier(blueprint=payload))
        
        
