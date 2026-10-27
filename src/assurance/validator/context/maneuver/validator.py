# src/assurance/validator/context/maneuver/validator.py

"""
Module: assurance.validator.context.maneuver.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ManeuverValidationLoader, ManeuverLayerToolkit, ContextValidator
from domain import Path, Token, Maneuver, ManeuverBlueprint, ManeuverPrimeExtract
from err import ManeuverCarrierEmptyException, ManeuverValidatorException
from exchange import PathValidationRequest, TokenValidationRequest
from transit import PathCarrier, TokenCarrier, ManeuverCarrier
from util import IdFactory, LoggingLevelRouter


class ManeuverValidator(ContextValidator[Maneuver]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ManeuverCarrier and its contents are safe to use.

    Attributes:
        loader: ManeuverLoader

    Provides:
        -   def execute(candidate: Ant) -> ValidationResult[ManeuverCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            loader: Optional[ManeuverValidationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[ManeuverLoader]
        """
        super().__init__(loader=loader or ManeuverValidationLoader())
        
    @property
    def loader(self) -> ManeuverValidationLoader:
        return cast(ManeuverValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> ManeuverLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ManeuverCarrier]:
        """
        Assure a candidate is a safe ManeuverCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a ManeuverValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a ManeuverCarrier
                            an empty ManeuverCarrier.
                    -   Either the token, row, or column attributes are flagged unsafe.
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
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(ManeuverPrimeExtract, loading.payload)
        carrier = prime_extract.reference
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_TRAVELER_ATTRIBUTE. ---#
        traveler_validation = self.toolkit.dependency.token.extract_context(
            request=TokenValidationRequest(
                item=TokenCarrier(context=blueprint.traveler),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),

            )
        )
        # Handle the case that the traveler is flagged.
        if traveler_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=traveler_validation.exception,
                )
            )
        # --- PROCESS_THE_PATH_ATTRIBUTE. ---#
        path_validation = self.toolkit.dependency.path.extract_context(
            request=PathValidationRequest(
                item=PathCarrier(context=blueprint.path),
                id=IdFactory.next_id(class_name="PathValidationRequest"),
            )
        )
        # Handle the case that the path is flagged.
        if path_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=path_validation.exception,
                )
            )
        # --- PROCESS_THE_BENEFIT_ATTRIBUTE. ---#
        benefit_validation = self.toolkit.number_validator.execute(blueprint.benefit)
        if benefit_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=benefit_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        path = cast(Path, path_validation.payload)
        benefit = cast(int, benefit_validation.payload)
        traveler = cast(Token, traveler_validation.payload)
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Maneuver.
        if prime_extract.recipient_wants_context:
            context = Maneuver(path=path, benefit=benefit, traveler=traveler)
            payload = ManeuverCarrier(context=context)
            return ValidationResult.success(payload)
        # Otherwise, the client is a ManeuverBuilder that needs a Blueprint.
        payload = ManeuverCarrier(
            blueprint=ManeuverBlueprint(
                path=path,
                benefit=benefit,
                traveler=traveler,
            )
        )
        return ValidationResult.success(payload)



