# src/production/endpoint/validation/context/flag.py

"""
Module: production.endpoint.validation.context.flag
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit
from domain import AccountContext, AccountContextBlueprint, AccountContextPrimeExtract
from err import ConsistencyException, ContextConsistencyException, NameNullException
from production import AccountContextFlagValidator, ContextFlagValidator
from transit import AccountContextCarrier
from util import LoggingLevelRouter

class AccountFirstnameContext(AccountContextFlagValidator[str]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  The context attribute is safe

    Attributes:
        toolkit: AccountLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any,
                    prime_extract: AccountContextPrimeExtract,
            ) -> ValidationResult[AccountContextCarrier]

    Super Class:
        AccountContextFlagValidator
    """
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            prime_extract: AccountContextPrimeExtract,
    ) -> ValidationResult[AccountContextCarrier]:
        """
        Assure a candidate is a firstname search context.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The prime_extract is faulty.
                    -   The blueprint.firstname attribute is null
                    -   The candidate is marked unsafe.
            2.  Otherwise, encapsulate the requested product in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountFirstnameContextFlagException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        fingerprint = prime_extract.reference.extract_blueprint()
        
        # Handle the case that a blueprint cannot be created.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountFirstnameContextFlagException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountFirstnameContextFlagException.MSG,
                    err_code=AccountFirstnameContextFlagException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the firstname attribute is not set.
        if fingerprint.firstname is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountFirstnameContextFlagException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountFirstnameContextFlagException.MSG,
                    err_code=AccountFirstnameContextFlagException.ERR_CODE,
                    ex=NameNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NameNullException.MSG,
                        err_code=NameNullException.ERR_CODE,
                    )
                )
            )
        # --- Process matching blueprint and candidate attributes. --#
        values: List[str] = []
        for item in [candidate, fingerprint.firstname]:
            # Handle the case that the candidate is not a valid name.
            validation = self.toolkit.identity_service.validate_name(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    AccountFirstnameContextFlagException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountFirstnameContextFlagException.MSG,
                        err_code=AccountFirstnameContextFlagException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            values.append = cast(str, validation.payload)
        # Handle the case that candidate does not match the blueprint attribute
        if values[0] == values[1]:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountFirstnameContextFlagException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountFirstnameContextFlagException.MSG,
                    err_code=AccountFirstnameContextFlagException.ERR_CODE,
                    ex=AccountContextConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextConsistencyExceptionn.MSG,
                        err_code=AccountContextConsistencyException.ERR_CODE,
                    )
                )
            )
        # --- Extract the validation payload. ---#
        firstname = values[0]
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe AccountContext.
        if prime_extract.recipient_wants_model:
            model = AccountContext(firstname=firstname)
            payload = AccountContextCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is an AccountContextBuilder that needs a Blueprint.
        blueprint = AccountContextBlueprint(firstname=firstname)
        blueprint.mark_as_validated()
        payload = AccountContextCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)
