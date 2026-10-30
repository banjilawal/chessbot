# src/assurance/validator/context/account/validator.py

"""
Module: assurance.validator.context.account.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import Result, ValidationResult
from assurance import ContextValidator
from bootstrap import AccountContextValidationLoader
from domain import AccountContext, AccountContextBlueprint, AccountContextPrimeExtract, ArenaContextNullWarningSet
from err import (
    AccountContextValidatorException, ArenaContextNullException, CapacityException,
    ValidationRouterException
)
from fabrication.contractor.account import machine
from transit import AccountContextCarrier, AccountContextValidationRouter
from util import LoggingLevelRouter


class AccountContextValidationManager(
    ContextValidationManager[AccountContext]
):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountContextCarrier and its payload are
            safe to use.

    Attributes:
        loader: AccountContextValidationLoader
        router: AccountContextValidationRouter

    Provides:
        -   def execute(item: Any) -> ValidationResult[AccountContextCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            loader: Optional[AccountContextValidationLoader] | None = None,
            router: Optional[AccountContextValidationRouter] | None = None,
    ):
        """
        Args:
           loader: Optional[AccountContextValidationLoader]
           router: Optional[AccountContextValidationRouter]
        """
        super().__init__(
            loader=loader or AccountContextValidationLoader(),
            router=router or AccountContextValidationRouter(),
        )
    
    @property
    def loader(self) -> AccountContextValidationLoader:
        return cast(AccountContextValidationLoader, super().loader)
    
    @property
    def router(self) -> AccountContextValidationRouter:
        return cast(AccountContextValidationRouter, super().router)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[AccountContextCarrier]:
        """
        Assure a candidate is a safe AccountContextCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The loader cannot bootstrap the process.
                    -   The chosen context is flagged.
                    -   There is no route to validate the choice.
            2.  Otherwise, send an AccountContextCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        result = self._router.execute(candidate)
        if result.is_failure:
            return ValidationResult.failure(
                AccountContextValidationManagerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationManagerException.MSG,
                    err_code=AccountValidationManagerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(AccountContextCarrier, result.authorization_applicant)
        return ValidationResult.success(carrier)




    