# src/bootstrap/validation/context/account/loader.py

"""
Module: bootstrap.validation.context.account.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, AccountValidatorToolkit
from domain import Account, Account
from err import (
    AccountCarrierEmptyException, AccountContextValidationLoaderException, AccountValidationRequestNullException
)
from exchange import AccountValidationRequest
from transit import AccountCarrier

from util import LoggingLevelRouter


class AccountContextValidationLoader(ContextValidationLoader[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   AccountValidationRequest
            -   AccountCarrier
            -   AccountBlueprint

    Attributes:
        toolkit: AccountValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[Account[T]

    Super Class:
        ContextLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[AccountValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AccountValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or AccountValidatorToolkit())
    
    @property
    def toolkit(self) -> AccountValidatorToolkit:
        return cast(AccountValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Account]:
        """
        Extract the AccountBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a AccountValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a AccountCarrier
                        -   An empty AccountCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a Account
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Account]
        Raises:
            AccountLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_context=AccountValidationRequest,
            null_exception=AccountValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationLoaderException.MSG,
                    err_code=AccountContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[AccountValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_context=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationLoaderException.MSG,
                    err_code=AccountContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(AccountCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationLoaderException.MSG,
                    err_code=AccountContextValidationLoaderException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = Account(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)