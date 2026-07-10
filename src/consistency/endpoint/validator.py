# src/consistency/endpoint/consistency.py

"""
Module: consistency.endpoint.consistency
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import ManeuverEndpointConsistencyException
from model import Square, Token
from result import ValidationResult
from util import LoggingLevelRouter
from consistency import TokenDestinationCertifier, TokenOriginCertifier


class ManeuverEndpointConsistency:
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
        Consistency
    """
    OPERATION_NAME = "token_destination_relation_consistency"
    
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
            origin_certifier: TokenOriginRelationConsistency
            destination_certifier: TokenDestinationRelationConsistency
        Returns:
            ValidationResult[int]
        Raises:
            ManeuverEndpointConsistencyException
        """
        method = f"{self.__class__.__name__}.consistency"
        
        # --- Supply any missing dependencies. ---#
        if origin_certifier is None:
            origin_certifier = TokenOriginRootCertifier(),
        if destination_certifier is None:
            destination_certifier = TokenDestinationRootCertifier()
        
        # Handle the case that, the token is not at the origin
        token_origin_relation_analysis_result = origin_certifier.validate(
            token=token,
            origin=origin,
        )
        if token_origin_relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverEndpointConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverEndpointConsistencyException.MSG,
                    err_code=ManeuverEndpointConsistencyException.ERR_CODE,
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
                ManeuverEndpointConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverEndpointConsistencyException.MSG,
                    err_code=ManeuverEndpointConsistencyException.ERR_CODE,
                    ex=token_destination_relation_analysis_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(2)