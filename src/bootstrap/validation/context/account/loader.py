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
from assurance import AccountLayerToolkit
from bootstrap import ContextValidationLoader
from domain import AccountContext, AccountContextPrimeExtract, FlagState
from transit import AccountContextCarrier
from util import LoggingLevelRouter


class AccountContextValidationLoader(
    ContextValidationLoader[AccountContext]
):
    """
    Role
        -   Boostrap

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   AccountContextValidationRequest
            -   AccountContextCarrier
            -   AccountBlueprint

    Attributes:
        toolkit: AccountLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[AccountContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[AccountLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AccountLayerToolkit]
        """
        super().__init__(toolkit=toolkit or AccountLayerToolkit())
    
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[AccountContextPrimeExtract]:
        """
        Extract the AccountBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a AccountValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a AccountContextCarrier
                        -   An empty AccountContextCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in an
                AccountContextPrimeExtract for the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[AccountContextPrimeExtract]
        Raises:
            AccountContextValidationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=item,
            target_model=AccountContextValidationRequest,
            null_exception=AccountContextValidationRequestNullException(),
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
        request = cast(Type[AccountContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
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
        # --- Cast carrier_validation payload then extract blueprint. ---#
        carrier = cast(AccountContextCarrier, carrier_validation.payload)
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
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the too many flags are enabled.
        if blueprint.size > blueprint.capacity:
            return ValidationResult.failure(
                AccountContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationLoaderException.MSG,
                    err_code=AccountContextValidationLoaderException.ERR_CODE,
                    ex=AccountContextCapacityException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCapacityException.MSG,
                        err_code=AccountContextCapacityException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that no flags are enabled.
        if blueprint.is_empty:
            return ValidationResult.failure(
                AccountContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationLoaderException.MSG,
                    err_code=AccountContextValidationLoaderException.ERR_CODE,
                    ex=AccountContextEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextEmptyException.MSG,
                        err_code=AccountContextEmptyException.ERR_CODE,
                    ),
                )
            )
        blueprint.flag_state = FlagState.VALID_SIZE
        # --- Send the work product. ---#
        extract = AccountContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)