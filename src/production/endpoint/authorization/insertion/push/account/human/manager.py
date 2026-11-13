# src/production/endpoint/authorization/push/account/human/collider.py

"""
Module: production.endpoint.authorization.push.account.human.collider
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, AccountContext, HumanAccount
from environment import AccountCollisionDetector
from util import LoggingLevelRouter


class HumanAccountCollider(CollisionManager[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Detect if an insert breaks Account collection's uniqueness
            constraint.

    Attributes:
        detector: AccountCollisionDetector

    Provides:
        -   def execute(item: Account, collection: AccountStack) -> CollisionReport
        
    Super Class
        CollisionManager
    """
    
    def __init__(self, detector: Optional[AccountCollisionDetector] | None = None):
        """
        Args:
            detector: Optional[AccountCollisionDetector]
        """
        super().__init__(detector=detector or AccountCollisionDetector())

    @property
    def detector(self) -> AccountCollisionDetector:
        return cast(AccountCollisionDetector, super().detector)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: HumanAccount, stream: AccountStack) -> CollisionReport:
        """
        Assure the item will be unique in the Account collection.
        
        Action:
            1.  If the item shares an attribute-value supposed to be unique to the
                collection, send an exception chain in the report.
            2.  Otherwise, report that primary keys will be maintained.
        Args:
            item: Account
            stream: AccountStack
        Returns:
           CollisionReport
        Raises:
            AccountCollisionManagerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        report = self._id_attraction(account=item, stream=stream)
        if report.collision_exists:
            context = cast(AccountContext, report.context)
            particle = cast(Account, report.particle)
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountColliderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountColliderException.MSG,
                    err_code=HumanAccountColliderException.ERR_CODE,
                    ex=report.exception
                )
            )
        
        report = self._email_attraction(account=item, stream=stream)
        if report.collision_exists:
            context = cast(AccountContext, report.context)
            particle = cast(HumanAccount, report.particle)
            return CollisionReport.collision(
                context=context,
                particle=particle,
                exception=HumanAccountColliderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountColliderException.MSG,
                    err_code=HumanAccountColliderException.ERR_CODE,
                    ex=report.exception
                )
            )
        return CollisionReport.empty()
    
    @LoggingLevelRouter.monitor
    def _id_attraction(
            self,
            account: HumanAccount,
            stream: AccountStack,
    ) -> CollisionReport:
        particle = account
        context = AccountContext(id=account.id)
        report = self.detector.execute(context=context, stream=stream)
        if report.collision_exists:
            particle = cast(Account, report.particle)
        if not isinstance(particle, HumanAccount):
            return CollisionReport.collision(
                particle=particle, 
                context=context, 
                exception=HumanAccountColliderException(),
            )
        person = cast(HumanAccount, particle)
        if person.email.upper() != account.email.upper():
            return CollisionReport.collision(
                particle=person,
                context=context,
                exception=HumanAccountColliderException(),
            )
        return CollisionReport.empty()
        
    @LoggingLevelRouter.monitor
    def _email_attraction(
            self,
            account: HumanAccount,
            stream: AccountStack,
    ) -> CollisionReport:
        particle = account
        context = AccountContext(email=account.email)
        report = self.detector.execute(context=context, stream=stream)
        if report.collision_exists:
            particle = cast(HumanAccount, report.particle)
        if particle.id != account.id:
            return CollisionReport.collision(
                particle=particle,
                context=context,
                exception=HumanAccountColliderException(),
            )
        return CollisionReport.empty()

        
        