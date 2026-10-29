# src/production/endpoint/validation/context/flag.py

"""
Module: production.endpoint.validation.context.flag
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from domain import AccountContext, AccountContextBlueprint, AccountContextPrimeExtract
from production import IdContextFlagValidator
from transit import AccountContextCarrier
from util import LoggingLevelRouter


class AccountIdContextFlag(IdContextFlagValidator[AccountContext]):
    
    def __init__(self):
        super().__init__()
        
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            prime_extract: AccountContextPrimeExtract,
    ) -> ValidationResult[AccountContextCarrier]:
        method = f"{self.__class__.__name__}.execute"
        
        fingerprint = prime_extract.reference.extract_blueprint()
        if fingerprint is None or fingerprint.id is None:
            return ValidationResult.failure(
                AccountIdContextFlagException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountIdContextFlagException.MSG,
                    err_code=AccountIdContextFlagException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        validation = self.identity_service.validate_id(candidate)
        if validation.is_failure:
            return ValidationResult.failure(
                AccountIdContextFlagException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountIdContextFlagException.MSG,
                    err_code=AccountIdContextFlagException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        id = cast(int, validation.payload)
        
        if prime_extract.recipient_wants_model:
            model = AccountContext(id=id)
            payload = AccountContextCarrier(model=model)
            return ValidationResult.success(payload)
        blueprint = AccountContextBlueprint(id=id)
        blueprint.mark_as_validated()
        payload = AccountContextCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)
        
        
        