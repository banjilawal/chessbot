# src/assurance/validator/model/scalar/validator.py

"""
Module: assurance.validator.model.scalar.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelValidator, ScalarValidatorToolkit
from domain import Scalar, ScalarBlueprint, ScalarValidationRequest
from err import (
    ScalarCarrierEmptyException, ScalarValidationRequestNullException, ScalarValidatorException
)
from transit import ScalarCarrier
from util import LoggingLevelRouter


class ScalarValidator(ModelValidator[Scalar]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ScalarCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: ScalarValidationToolkit

    Provides:
        -   def execute(request: ScalarValidationRequest) ->ValidationResult[ScalarCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[ScalarValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ScalarValidationToolkit]
        """
        super().__init__(toolkit=toolkit or ScalarValidatorToolkit())
    
    @property
    def toolkit(self) -> ScalarValidatorToolkit:
        return cast(
            ScalarValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ScalarValidationRequest) -> ValidationResult[ScalarCarrier]:
        """
        Certify a candidate is a ScalarCarrier whose payload is either a Scalar
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a ScalarCarrier or its null.
                    - The candidate is an empty ScalarCarrier.
                    - Any Scalar attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[ScalarCarrier]
        Raises:
            ScalarValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=ScalarValidationRequest,
            null_exception=ScalarValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(ScalarValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            Type[self.toolkit.metadata.types.carrier],
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that there is no blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
            
        # Handle the case that any scalar component in the blueprint is flagged.
        magnitude_test = self.toolkit.helper.number_validator.execute(blueprint.magnitude)
        if magnitude_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=magnitude_test.exception,
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        magnitude = cast(int, magnitude_test.payload)
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.is_carrying_model:
            return ValidationResult.success(
                ScalarCarrier(model=Scalar(magnitude))
            )
        # The blueprint case
        return ValidationResult.success(
            ScalarCarrier(blueprint=ScalarBlueprint(magnitude=magnitude))
        )