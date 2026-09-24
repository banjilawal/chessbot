# src/assurance/validator/structure/register/square/validator.py

"""
Module: assurance.validator.structure.register.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from artifcat import ValidationResult
from assurance import RegisterValidator, SquareRegisterValidatorToolkit
from domain import (
    Square, SquareRegister, SquareRegisterBlueprint, SquareRegisterValidationRequest,
    SquareValidationRequest
)
from err import (
    DuplicateSquareException, EmptySquareCarrierException, EmptySquareRegisterCarrierException,
    SquareRegisterValidationRequestNullException, SquareRegisterValidatorException
)
from transit import SquareCarrier, SquareRegisterCarrier
from util import IdFactory, LoggingLevelRouter


class SquareRegisterValidator(RegisterValidator[SquareRegister]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structures and blueprints inside an EntityCarrier's payload.

    Attributes:
        toolkit: SquareRegisterValidatorToolkit

    Provides:
        - def execute(candidate: Any) -> ValidationResult[SquareRegisterCarrier]:

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[SquareRegisterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareRegisterValidatorToolkit]
        """
        super().__init__(
            toolkit=toolkit or SquareRegisterValidatorToolkit()
        )
    
    @property
    def toolkit(self) -> SquareRegisterValidatorToolkit:
        return cast(SquareRegisterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareRegisterCarrier]:
        """
        Certify a SquareRegisterCarrier's payload is either a SquareRegister or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a SquareRegisterValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a SquareRegisterCarrier
                            an empty SquareRegisterCarrier.
                    *   Either the square, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareRegisterCarrier]
        Raises:
            SquareRegisterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            target_model=SquareRegisterValidationRequest,
            null_exception=SquareRegisterValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidatorException.MSG,
                    err_code=SquareRegisterValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        request = cast(SquareRegisterValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidatorException.MSG,
                    err_code=SquareRegisterValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            SquareRegisterCarrier,
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidatorException.MSG,
                    err_code=SquareRegisterValidatorException.ERR_CODE,
                    ex=EmptySquareRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareRegisterCarrierException.MSG,
                        err_code=EmptySquareRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Run the square validation checks. ---#
        endpoints: List[Square] = []
        for square in [blueprint.origin, blueprint.destination]:
            square_validation = self.toolkit.helper.square_validator.execute(
            candidate=SquareValidationRequest(
                    id=IdFactory.next_id(class_name="SquareValidationRequest"),
                    item=SquareCarrier(model=square),
                )
            )
            # Handle the case that the square is flagged.
            if square_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterValidatorException.MSG,
                        err_code=SquareRegisterValidatorException.ERR_CODE,
                        ex=square_validation.exception,
                    )
                )
            # Otherwise, extract the square from the carrier
            square_carrier = cast(SquareCarrier, square_validation.payload)
            # Handle the case that the carrier does not have a validated Square for the register.
            if not square_carrier.is_carrying_model:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterValidatorException.MSG,
                        err_code=SquareRegisterValidatorException.ERR_CODE,
                        ex=EmptySquareCarrierException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=EmptySquareCarrierException.MSG,
                            err_code=EmptySquareCarrierException.ERR_CODE,
                        ),
                    )
                )
            # Put the register's good Square in the endpoints array.
            endpoint = cast(Square, square_carrier.entity)
            # Handle the case that the origin and destination are the same.
            if endpoint in endpoints:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterValidatorException.MSG,
                        err_code=SquareRegisterValidatorException.ERR_CODE,
                        ex=DuplicateSquareException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=DuplicateSquareException.MSG,
                            err_code=DuplicateSquareException.ERR_CODE,
                        ),
                    )
                )
            endpoints.append(endpoint)
        # --- Forward the appropriate work product to the caller. ---#  
        # The model case
        if carrier.is_carrying_model:
            model = SquareRegister(origin=endpoints[0], destination=endpoints[1])
            return ValidationResult.success(
                SquareRegisterCarrier(model=model)
            )
        # The blueprint case
        blueprint = SquareRegisterBlueprint(origin=endpoints[0], destination=endpoints[1])
        return ValidationResult.success(
            SquareRegisterCarrier(blueprint=blueprint)
        )
    
    
