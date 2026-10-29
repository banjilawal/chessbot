# src/production/endpoint/validation/context/id/account/inspector.py

"""
Module: production.endpoint.validation.context.id.account.inspector
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, cast

from artifcat import ValidationResult
from domain import AccountContext, AccountContextBlueprint, AccountContextPrimeExtract
from err import IdentifierNullException
from production import IdContextInspector
from transit import AccountContextCarrier
from util import LoggingLevelRouter


class AccountIdContextInspector(IdContextInspector[AccountContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountContextCarrier with an id payload is safe to use.

    Attributes:
        identity_service: IdentityService

    Provides:
        -   def execute(
                    candidate: Any,
                    prime_extract: AccountContextPrimeExtract,
            ) -> ValidationResult[AccountContextCarrier]

    Super Class:
        IdContextInspector
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
        Assure a candidate is a safe Account-Id-Context to use or build.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the
                following occur
                    -   The prime_extract is faulty.
                    -   The blueprint.id attribute is null
                    -   Either candidate or blueprint.id is flagged.
                    -   THe candidate and blueprint.id do not match.
            2.  Otherwise, encapsulate the requested product in the success result.
        Args:
            candidate: Any
            prime_extract: AccountContextPrimeExtract
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountIdContextInspectorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Build a blueprint from the prime_extract ---#
        fingerprint = prime_extract.reference.extract_blueprint()
        
        # Handle the case that a blueprint cannot be created.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountIdContextInspectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountIdContextInspectorException.MSG,
                    err_code=AccountIdContextInspectorException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that a blueprint id field is not set.
        if fingerprint.id is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountIdContextInspectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountIdContextInspectorException.MSG,
                    err_code=AccountIdContextInspectorException.ERR_CODE,
                    ex=IdentifierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=IdentifierNullException.MSG,
                        err_code=IdentifierNullException.ERR_CODE,
                    )
                )
            )
        # --- Validate the corresponding blueprint and candidate attributes. ---#
        values: List[int] = []
        for item in [candidate, fingerprint.id]:
            # Handle the case that an item is not a number.
            validation = self.identity_service.validate_id(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    AccountIdContextInspectorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountIdContextInspectorException.MSG,
                        err_code=AccountIdContextInspectorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Append the success
            values.append(cast(int, validation.payload))
        # Handle the case that candidate does not match the fingerprint attribute.
        if values[0] == values[1]:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountIdContextInspectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountIdContextInspectorException.MSG,
                    err_code=AccountIdContextInspectorException.ERR_CODE,
                    ex=AccountContextConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextConsistencyExceptionn.MSG,
                        err_code=AccountContextConsistencyException.ERR_CODE,
                    )
                )
            )
        # --- Extract the validation payload. ---#
        id = values[0]
        # --- Forward the appropriate work product to the caller. ---#
        
        # The client wants a safe AccountContext.
        if prime_extract.recipient_wants_model:
            model = AccountContext(id=id)
            payload = AccountContextCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is an AccountContextBuilder that needs a Blueprint.
        blueprint = AccountContextBlueprint(id=id)
        blueprint.mark_as_validated()
        payload = AccountContextCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)

        
        