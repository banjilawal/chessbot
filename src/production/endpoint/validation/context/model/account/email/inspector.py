# src/production/endpoint/validation/context/model/account/email/inspector.py

"""
Module: production.endpoint.validation.context.model.account.email.inspector
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, cast

from artifcat import ValidationResult
from domain import AccountContext, AccountContextBlueprint, AccountContextPrimeExtract
from err import NameNullException
from production import AccountContextInspector
from transit import AccountContextCarrier
from util import LoggingLevelRouter

class AccountEmailContextInspector(AccountContextInspector[str]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountContextCarrier with a email payload is safe to use.
        
    Attributes:
        toolkit: AccountLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any,
                    prime_extract: AccountContextPrimeExtract,
            ) -> ValidationResult[AccountContextCarrier]

    Super Class:
        AccountContextInspector
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
        Assure a candidate is a safe Account-email-Context to use or build.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The prime_extract is faulty.
                    -   The blueprint.email attribute is null
                    -   Either candidate or blueprint.email is flagged.
                    -   THe candidate and blueprint.email do not match.
            2.  Otherwise, encapsulate the requested product in the success result.
        Args:
            candidate: Any
            prime_extract: AccountContextPrimeExtract
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountEmailContextInspectorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        fingerprint = prime_extract.reference.extract_blueprint()
        
        # Handle the case that a blueprint cannot be created.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountEmailContextInspectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEmailContextInspectorException.MSG,
                    err_code=AccountEmailContextInspectorException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the email attribute is not set.
        if fingerprint.email is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountEmailContextInspectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEmailContextInspectorException.MSG,
                    err_code=AccountEmailContextInspectorException.ERR_CODE,
                    ex=NameNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NameNullException.MSG,
                        err_code=NameNullException.ERR_CODE,
                    )
                )
            )
        # --- Process corresponding blueprint and candidate attributes. --#
        safe_values: List[str] = []
        for item in [candidate, fingerprint.email]:
            # Handle the case that an item is not a string
            validation = self.toolkit.identity_service.validate_name(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    AccountEmailContextInspectorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountEmailContextInspectorException.MSG,
                        err_code=AccountEmailContextInspectorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            safe_values.append = cast(str, validation.payload)
        # Handle the case that candidate does not match the blueprint attribute
        if safe_values[0] == safe_values[1]:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountEmailContextInspectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEmailContextInspectorException.MSG,
                    err_code=AccountEmailContextInspectorException.ERR_CODE,
                    ex=AccountContextConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextConsistencyExceptionn.MSG,
                        err_code=AccountContextConsistencyException.ERR_CODE,
                    )
                )
            )
        # --- Extract the validation payload. ---#
        email = safe_values[0]
        
        # --- Forward the appropriate work product to the caller. ---#
        
        # The client wants a safe AccountContext.
        if prime_extract.recipient_wants_model:
            model = AccountContext(email=email)
            payload = AccountContextCarrier(model=model)
            return ValidationResult.success(payload)
        
        # Otherwise, the client is an AccountContextBuilder that needs a Blueprint.
        blueprint = AccountContextBlueprint(email=email)
        blueprint.mark_as_validated()
        payload = AccountContextCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)
