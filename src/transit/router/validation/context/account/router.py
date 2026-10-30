# src/transit/route/validation/context/account/router.py

"""
Module: transit.route.validation.context.account.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit
from bootstrap import AccountContextValidationLoader
from domain import AccountContext, AccountContextPrimeExtract
from err import MissingValidationRouteException
from production import (
    AccountCategoryContextInspector, AccountEmailContextInspector, AccountFirstnameContextInspector,
    AccountIdContextInspector, AccountLastnameContextInspector, AccountMachineNameContextInspector
)
from transit import AccountContextCarrier, ContextValidationRouter
from util import LoggingLevelRouter

class AccountContextValidationRouter(
    ContextValidationRouter[AccountContext]
):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes a ContextPrimeExtract to the right attribute validator.

    Attributes:
        loader: AccountContextValidationLoader
        id_inspector: AccountIdContextInspector
        email_inspector: AccountEmailContextInspector
        lastname_inspector: AccountLastnameContextInspector
        firstname_inspector: AccountFirstnameContextInspector
        account_type_inspector: AccountCategoryContextInspector
        machine_name_inspector: AccountMachineNameContextInspector
        
    Provides:

    Super Class:
        ContextValidationRouter
    """
    _loader: AccountContextValidationLoader
    _id_inspector: AccountIdContextInspector
    _email_inspector: AccountEmailContextInspector
    _lastname_inspector: AccountLastnameContextInspector
    _firstname_inspector: AccountFirstnameContextInspector
    _account_type_inspector: AccountCategoryContextInspector
    _machine_name_inspector: AccountMachineNameContextInspector
    
    def __init__(
            self,
            toolkit: Optional[AccountLayerToolkit] | None = None,
            loader: Optional[AccountContextValidationLoader] | None = None,
            id_inspector: Optional[AccountIdContextInspector] |  None = None,
            email_inspector: Optional[AccountEmailContextInspector] | None = None,
            lastname_inspector: Optional[AccountLastnameContextInspector] | None = None,
            firstname_inspector: Optional[AccountFirstnameContextInspector] | None = None,
            account_type_inspector: Optional[AccountCategoryContextInspector] | None = None,
            machine_name_inspector: Optional[AccountMachineNameContextInspector] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AccountLayerToolkit]
            id_inspector: Optional[AccountIdContextInspector]
            email_inspector: Optional[AccountEmailContextInspector]
            lastname_inspector: Optional[AccountLastnameContextInspector]
            firstname_inspector: Optional[AccountFirstnameContextInspector]
            account_type_inspector: Optional[AccountCategoryContextInspector]
            machine_name_inspector: Optional[AccountMachineNameContextInspector]
        """
        super().__init__(toolkit=toolkit or AccountLayerToolkit())
        self._loader = loader or AccountContextValidationLoader()
        self._id_inspector = id_inspector or AccountIdContextInspector()
        self._email_inspector = email_inspector or AccountEmailContextInspector()
        self._lastname_inspector = lastname_inspector or AccountLastnameContextInspector()
        self._firstname_inspector = firstname_inspector or AccountFirstnameContextInspector()
        self._account_type_inspector = account_type_inspector or AccountCategoryContextInspector()
        self._machine_name_inspector = machine_name_inspector or AccountMachineNameContextInspector()
    
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
    
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
            AccountContextValidationRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        bootstrap = self._loader.execute(bootstrap=candidate)
        if bootstrap.is_failure:
            return ValidationResult.failure(
                AccountContextValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationRouterException.MSG,
                    err_code=AccountContextValidationRouterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        prime_extract = cast(AccountContextPrimeExtract, bootstrap.payload)
        fingerprint = prime_extract.reference.extract_blueprint()
        
        if fingerprint is None:
            return ValidationResult.failure(
                AccountContextValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationRouterException.MSG,
                    err_code=AccountContextValidationRouterException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        result = ValidationResult.failure(MissingValidationRouteException())
        if fingerprint.id is not None:
            result = self._id_inspector.execute(
                candidate=fingerprint.id,
                prime_extract=prime_extract,
            )
        if fingerprint.firstname is not None:
            result = self._firstname_inspector.execute(
                candidate=fingerprint.firstname,
                prime_extract=prime_extract,
            )
        if fingerprint.lastname is not None:
            result = self._lastname_inspector.execute(
                candidate=fingerprint.lastname,
                prime_extract=prime_extract,
            )
        if fingerprint.email is not None:
            result = self._email_inspector.execute(
                candidate=fingerprint.email,
                prime_extract=prime_extract,
            )
        if fingerprint.machine_name is not None:
            result = self._machine_name_inspector.execute(
                candidate=fingerprint.machine_name,
                prime_extract=prime_extract,
            )
        if fingerprint.account_type is not None:
            result = self._account_type_inspector.execute(
                candidate=fingerprint.account_type,
                prime_extract=prime_extract,
            )
        if result.is_failure:
            return ValidationResult.failure(
                AccountContextValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationRouterException.MSG,
                    err_code=AccountContextValidationRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(AccountContextCarrier, result.payload)
        return ValidationResult.success(carrier)
        
        
        
        