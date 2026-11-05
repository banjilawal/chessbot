# src/production/manager/collision/account/manager.py

"""
Module: production.manager.collision.account.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, AccountContext, HumanAccount, MachineAccount
from environment import AccountCollisionDetector
from err import ChessException
from production import CollisionManager
from util import LoggingLevelRouter


class AccountCollisionManager(CollisionManager[Account]):
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
    def execute(self, item: Account, collection: AccountStack) -> CollisionReport:
        """
        Assure the item will be unique in the collection.
        
        Action:
            1.  If the item shares an attribute-value supposed to be unique to the
                collection, send an exception chain in the report.
            2.  Otherwise, report that primary keys will be maintained.
        Args:
            item: Account
            collection: AccountStack
        Returns:
           CollisionReport
        Raises:
            AccountCollisionManagerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        identifier: str = "id"
        context: AccountContext = AccountContext(id=item.id)
        
        # --- Assure the global primary key constraint is not violated. ---#
        report = self.detector.execute(
            context=context,
            stream=collection,
        )
        # Handle the case that a duplicate is found.
        if report.collision_exists:
            # Send the exception in the report.
            particle = cast(Account, report.particle)
            return CollisionReport.collision_event(
                match=report.match,
                target=report.target,
                particle=particle,
                identifier=identifier,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # --- Configure for assuring secondary keys. ---#
        # Set up for a HumanAccount.
        if isinstance(item, HumanAccount):
            identifier = "email"
            context = AccountContext(email=cast(HumanAccount, item).email)
        # Set up for MachineAccount
        if isinstance(item, MachineAccount):
            identifier = "machine_name"
            context = AccountContext(machine_name=cast(MachineAccount, item).name)
            
        # --- Run the secondary detector. ---#
        report = self.detector.execute(context=context, stream=collection)
        # Handle the case that the secondary key is duplicated.
        if report.collision_exists:
            # Send the exception in the report.
            particle = cast(Account, report.particle)
            return CollisionReport.collision_event(
                match=report.match,
                target=report.target,
                particle=particle,
                identifier=identifier,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # --- Forward the work product. ---#
        return CollisionReport.no_collision_events()
    
