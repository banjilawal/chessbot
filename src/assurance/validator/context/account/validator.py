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
from transit import AccountContextCarrier
from util import LoggingLevelRouter


class AccountContextValidator(
    ContextValidator[AccountContext]
):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountContextCarrier and its payload are
            safe to use.

    Attributes:
        loader: AccountContextValidationLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[AccountContextCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            loader: Optional[AccountContextValidationLoader] | None = None,
    ):
        """
        Args:
           loader: Optional[AccountContextValidationLoader]
        """
        super().__init__(loader=loader or AccountContextValidationLoader())
    
    @property
    def loader(self) -> AccountContextValidationLoader:
        return cast(AccountContextValidationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[AccountContextCarrier]:
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
        
        bootstrap = self.loader.execute(bootstrap=candidate)
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
        candidate = extract.blueprint
        if candidate is None:
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
        if candidate.is_wrong_size:
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
        if candidate.email is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=candidate.email
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
        if candidate.firstname is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=candidate.firstname
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
        if candidate.lastname is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=candidate.lastname
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
        if candidate.machine_name is not None:
            validation = self.loader.toolkit.identity_service.validate_name(
                candidate=candidate.machine_name
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
            candidate.machine_name = cast(str, validation.payload)
            blueprint = AccountContextBlueprint(firstname=candidate.machine_name)
        if candidate.machine_account is not None:
            blueprint = AccountContextBlueprint(machine_account=True)
        if candidate.human_account is not None:
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



    