# src/assurance/load/struct/register/square/loader.py

"""
Module: assurance.load.struct.register.square.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import RegisterLoader, SquareRegisterValidationToolkit
from client import SquareRegisterValidationRequest
from domain import SquareRegister, SquareRegisterBlueprint
from err import (
    EmptySquareRegisterCarrierException, SquareRegisterValidationRequestNullException,
    SquareRegisterExtractorException
)
from transit import SquareRegisterCarrier
from util import LoggingLevelRouter


class SquareRegisterExtractor(RegisterLoader[SquareRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a SquareRegisterBlueprint from the validation candidate.

    Attributes:
        toolkit: SquareRegisterValidationToolkit

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[SquareRegisterBlueprint]:

    Super Class:
        RegisterExtractor
    """
    
    def __init__(
            self, 
            toolkit: Optional[SquareRegisterValidationToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareRegisterValidationToolkit]
        """
        super().__init__(toolkit=toolkit or SquareRegisterValidationToolkit())
    
    @property
    def toolkit(self) -> SquareRegisterValidationToolkit:
        return cast(SquareRegisterValidationToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareRegisterBlueprint]:
        """
        Extract the SquareRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is null or not a SquareRegisterValidatorRequest.
                    -   The request payload is either:
                            -   Null
                            -   Not a SquareRegisterCarrier
                            -   An empty SquareRegisterCarrier.
                    -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, send the blueprint in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareRegisterBlueprint]
        Raises:
            SquareRegisterExtractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.wrapper.priming_validator.execute(
            candidate=candidate,
            target_register=SquareRegisterValidationRequest,
            null_exception=SquareRegisterValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterExtractorException.MSG,
                    err_code=SquareRegisterExtractorException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        request = cast(Type[SquareRegisterValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.wrapper.priming_validator.execute(
            candidate=request.item,
            target_register=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterExtractorException.MSG,
                    err_code=SquareRegisterExtractorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to into carrier to extract the blueprint. ---#
        carrier = cast(SquareRegisterCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterExtractorException.MSG,
                    err_code=SquareRegisterExtractorException.ERR_CODE,
                    ex=EmptySquareRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareRegisterCarrierException.MSG,
                        err_code=EmptySquareRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(blueprint)