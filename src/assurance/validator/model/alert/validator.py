# src/assurance/validator/model/alert/validator.py

"""
Module: assurance.validator.model.alert.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from artifcat import ValidationResult
from assurance import AlertValidationLoader, AlertLayerToolkit, ModelValidator
from domain import CheckmateEncounter, Encounter, Alert, AlertBlueprint, AlertPrimeExtract, EncounterWarning
from err import AlertCarrierEmptyException, AlertValidatorException
from exchange import EncounterValidationRequest
from transit import CheckmateEncounterCarrier, EncounterCarrier, AlertCarrier, EncounterWarningCarrier
from util import IdFactory, LoggingLevelRouter


class AlertValidator(ModelValidator[Alert]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a AlertCarrier and its contents are safe to use.

    Attributes:
        loader: AlertLoader

    Provides:
        -   def execute(candidate: Ant) -> ValidationResult[AlertCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[AlertValidationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[AlertLoader]
        """
        super().__init__(loader=loader or AlertValidationLoader())
        
    @property
    def loader(self) -> AlertValidationLoader:
        return cast(AlertValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> AlertLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[AlertCarrier]:
        """
        Assure a candidate is a safe AlertCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a AlertValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a AlertCarrier
                            an empty AlertCarrier.
                    -   Either the encounter, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AlertCarrier]
        Raises:
            AlertValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the loader fails.
        bootstrap = self.loader.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidatorException.MSG,
                    err_code=AlertValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(AlertPrimeExtract, bootstrap.payload)
        carrier = extract.reference
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidatorException.MSG,
                    err_code=AlertValidatorException.ERR_CODE,
                    ex=AlertCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AlertCarrierEmptyException.MSG,
                        err_code=AlertCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_THREAT_ATTRIBUTE. ---#
        threat = blueprint.threat
        if threat is not None:
            threat_validation = self.toolkit.dependency.encounter.extract_model(
                request=EncounterValidationRequest(
                    item=EncounterWarningCarrier(model=blueprint.threat),
                    id=IdFactory.next_id(class_name="EncounterValidationRequest"),
                )
            )
            # Handle the case that the threat is flagged.
            if threat_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    AlertValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AlertValidatorException.MSG,
                        err_code=AlertValidatorException.ERR_CODE,
                        ex=threat_validation.exception,
                    )
                )
            threat = cast(EncounterWarning, threat_validation.payload)
        # --- PROCESS_THE_CHECKMATE_ATTRIBUTE. ---#
        checkmate = blueprint.checkmate
        if checkmate is not None:
            checkmate_validation = self.toolkit.dependency.encounter.extract_model(
                request=EncounterValidationRequest(
                    item=CheckmateEncounterCarrier(model=blueprint.checkmate),
                    id=IdFactory.next_id(class_name="EncounterValidationRequest"),
                )
            )
            # Handle the case that the threat is flagged.
            if checkmate_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    AlertValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AlertValidatorException.MSG,
                        err_code=AlertValidatorException.ERR_CODE,
                        ex=checkmate_validation.exception,
                    )
                )
            checkmate = cast(CheckmateEncounter, checkmate_validation.payload)
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Alert.
        if extract.recipient_wants_model:
            payload = AlertCarrier(
                model=Alert(
                    threat=threat,
                    checkmate=checkmate,
                )
            )
            return ValidationResult.success(payload)
        # Otherwise, the client is a AlertBuilder that needs a Blueprint.
        payload = AlertCarrier(
            blueprint=AlertBlueprint(
                threat=threat,
                checkmate=checkmate,
            )
        )
        return ValidationResult.success(payload)



