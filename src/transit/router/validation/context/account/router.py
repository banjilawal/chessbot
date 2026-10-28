# src/transit/route/validation/context/account/router.py

"""
Module: transit.route.validation.context.account.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit
from domain import AccountContext, AccountContextPrimeExtract
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
        toolkit: AccountLayerToolkit
        
    Provides:

    Super Class:
        ContextValidationRouter
    """
    
    def __init__(self, toolkit: Optional[AccountLayerToolkit] | None = None):
        """
        Args:
            toolkit: Optional[AccountLayerToolkit]
        """
        super().__init__(toolkit=toolkit or AccountLayerToolkit())
    
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            prime_extract: AccountContextPrimeExtract,
    ) -> ValidationResult[AccountContextCarrier]:
        pass