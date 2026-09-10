# src/assurance/validator/model/vector/validator.py

"""
Module: assurance.validator.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelValidator, VectorValidationToolkit
from domain import Vector, VectorBlueprint, VectorValidationRequest
from err import VectorValidatorException
from err.null.domain.exchange.request import RequestNullException
from transit import VectorCarrier
from util import LoggingLevelRouter


class VectorValidator(ModelValidator[Vector]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorBlueprint instance is safe before use.

    Attributes:
        toolkit: VectorValidationToolkit

    Provides:
        - def execute(self, candidate: Any) ->ValidationResult[VectorCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorValidationToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[VectorValidationToolkit]
        """
        super().__init__(toolkit=toolkit or VectorValidationToolkit())
    
    @property
    def toolkit(self) -> VectorValidationToolkit:
        return cast(
            VectorValidationToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorValidationRequest
    ) -> ValidationResult[VectorCarrier]:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a VectorCarrier or its null.
                    - The candidate is an empty VectorCarrier.
                    - Any Vector attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[VectorCarrier]
        Raises:
            VectorValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=VectorValidationRequest,
            null_exception=RequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(VectorValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
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
        
        # Handle the case that any vector component in the blueprint is flagged.
        numbers = []
        for number in [blueprint.x, blueprint.y]:
            validation = self.toolkit.helper.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorValidatorException.MSG,
                        err_code=VectorValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            numbers.append(cast(int, validation.payload))
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case
        if carrier.is_carrying_model:
            return ValidationResult.success(
                VectorCarrier(
                    model=Vector(
                        x=numbers[0],
                        y=numbers[1],
                    )
                )
            )
        # The blueprint case
        return ValidationResult.success(
            VectorCarrier(
                blueprint=VectorBlueprint(
                    x=numbers[0],
                    y=numbers[1],
                )
            )
        )