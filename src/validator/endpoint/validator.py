# src/validator/endpoint/validator.py

"""
Module: validator.endpoint.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import ManeuverEndpointValidatorException
from model import Square, Token
from result import ValidationResult
from util import LoggingLevelRouter
from validator import TokenDestinationCertifier, TokenOriginCertifier


class ManeuverEndpointValidator:
    """
    Role
        -   Validation Worker
        -   Integrity Maintenance
        -   Consistency Assurance

    Responsibilities:
        1.  Consolidates both relationship tests for a Token and the endpoints at the
            start of a maneuver.

    Attributes:

    Provides:
        -   def execute(
                    token: Token,
                    destination: Square,
                    toolkit: TokenEndpointRelationToolkit,
            ) -> ValidationResult[Square]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "token_destination_relation_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            token: Token,
            origin: Square,
            destination: Square,
            origin_certifier: TokenOriginCertifier | None = None,
            destination_certifier: TokenDestinationCertifier | None = None,
    ) -> ValidationResult[int]:
        """
        Makes sure the token is only at the origin at the beginning of a maneuver.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The relation analysis is not completed.
                    -   The token is either fully or partially bound to the destination.
            2.  Otherwise, Send the number two in the success result indicating two checks were passed.
        Args:
            token: Token
            origin: Square
            destination: Square
            origin_certifier: TokenOriginRelationValidator
            destination_certifier: TokenDestinationRelationValidator
        Returns:
            ValidationResult[int]
        Raises:
            ManeuverEndpointValidatorException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if origin_certifier is None:
            origin_certifier = TokenOriginCertifier(),
        if destination_certifier is None:
            destination_certifier = TokenDestinationCertifier()
        
        # Handle the case that, the token is not at the origin
        token_origin_relation_analysis_result = origin_certifier.validate(
            token=token,
            origin=origin,
        )
        if token_origin_relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverEndpointValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverEndpointValidatorException.MSG,
                    err_code=ManeuverEndpointValidatorException.ERR_CODE,
                    ex=token_origin_relation_analysis_result.exception,
                )
            )
        # Handle the case that, the token is already at the destination.
        token_destination_relation_analysis_result = destination_certifier.validate(
            token=token,
            destination=destination,
        )
        if token_destination_relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverEndpointValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverEndpointValidatorException.MSG,
                    err_code=ManeuverEndpointValidatorException.ERR_CODE,
                    ex=token_destination_relation_analysis_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(2)