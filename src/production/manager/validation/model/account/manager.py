# src/production/manager/validation/model/account/manager.py

"""
Module: production.manager.validation.model.account.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from domain import Account
from err import AccountValidatorException
from production import AccountColliderProducer, ModelColliderManager
from transit import AccountCarrier, AccountCollider, AccountColliderRouter
from util import LoggingLevelRouter


class AccountColliderManager(ModelColliderManager[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountCarrier is safe to use.

    Attributes:
        router: Optional[AccountValidationRouter]
        producer: Optional[AccountColliderProducer]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[AccountCarrier]:

    Super Class:
        ModelColliderManager
    """
    
    def __init__(
            self,
            router: Optional[AccountColliderRouter] | None = None,
            producer: Optional[AccountColliderProducer] | None = None,
    ):
        """
        Args:
            router: Optional[AccountValidationRouter]
            producer: Optional[AccountColliderProducer]
        """
        super().__init__(
            router=router or AccountColliderRouter(),
            producer=producer or AccountColliderProducer(),
        )
    
    @property
    def router(self) -> AccountColliderRouter:
        return cast(AccountColliderRouter, super().router)
    
    @property
    def producer(self) -> AccountColliderProducer:
        return cast(AccountColliderProducer, super().producer)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[AccountCarrier]:
        """
        Assure a candidate is a safe AccountCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Router fails.
                    -   Team, Formation, Deployment, id, or HomeAccount are flagged.
                    -   The producer does not return a product
            2.  Otherwise, send an AccountCarrier in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[AccountCarrier]
        Raises:
            AccountValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self.producer.execute(item=item)
        if product.is_failure:
            return ValidationResult.failure(
                AccountValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidatorException.MSG,
                    err_code=AccountValidatorException.ERR_CODE,
                    ex=product.exception,
                )
            )
        collider = cast(AccountCollider, product.payload)
        
        validation = self.router.execute(collider=collider)
        if validation.is_failure:
            return ValidationResult.failure(
                AccountValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidatorException.MSG,
                    err_code=AccountValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        carrier = cast(AccountCarrier, validation.payload)
        return ValidationResult.success(carrier)
    