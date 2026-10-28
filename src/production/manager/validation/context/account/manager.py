# src/assurance/validator/context/account/validator.py

"""
Module: assurance.validator.context.account.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
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
    def execute(self, item: Any) -> ValidationResult[AccountContextCarrier]:
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
            item: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        bootstrap = self.loader.execute(item=item)
        if bootstrap.is_failure:
            return ValidationResult.failure(
                AccountContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidatorException.MSG,
                    err_code=AccountContextValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        extract = cast(AccountContextPrimeExtract, bootstrap.payload)
        item = extract.blueprint
        if item is None:
            return ValidationResult.failure(
                AccountContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidatorException.MSG,
                    err_code=AccountContextValidatorException.ERR_CODE,
                    ex=AccountContextNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextNullException.MSG,
                        err_code=AccountContextNullException.ERR_CODE,
                    ),
                )
            )
        if item.is_wrong_size:
            return ValidationResult.failure(
                AccountContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidatorException.MSG,
                    err_code=AccountContextValidatorException.ERR_CODE,
                    ex=CapacityException(),
                )
            )
        blueprint = AccountContextBlueprint()
        if item.email is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=item.email
            )
            if validation.is_failure:
                return ValidationResult.failure(
                    AccountContextValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextValidatorException.MSG,
                        err_code=AccountContextValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            email = cast(str, validation.payload)
            blueprint = AccountContextBlueprint(email=email)
        if item.firstname is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=item.firstname
            )
            if validation.is_failure:
                return ValidationResult.failure(
                    AccountContextValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextValidatorException.MSG,
                        err_code=AccountContextValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            firstname = cast(str, validation.payload)
            blueprint = AccountContextBlueprint(firstname=firstname)
        if item.lastname is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=item.lastname
            )
            if validation.is_failure:
                return ValidationResult.failure(
                    AccountContextValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextValidatorException.MSG,
                        err_code=AccountContextValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            lastname = cast(str, validation.payload)
            blueprint = AccountContextBlueprint(email=lastname)
        if item.machine_name is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=item.machine_name
            )
            if validation.is_failure:
                return ValidationResult.failure(
                    AccountContextValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextValidatorException.MSG,
                        err_code=AccountContextValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            item.machine_name = cast(str, validation.payload)
            blueprint = AccountContextBlueprint(firstname=item.machine_name)
        if item.machine_account is not None:
            blueprint = AccountContextBlueprint(machine_account=True)
        if item.human_account is not None:
            blueprint = AccountContextBlueprint(human_account=True)
        if blueprint.is_empty:
            return ValidationResult.failure(
                ValidationRouterException()
            )
        if extract.recipient_wants_blueprint:
            return ValidationResult.success(
                AccountContextCarrier(blueprint=blueprint)
            )
        return ValidationResult.success(
            AccountContextCarrier(model=)
        )



    