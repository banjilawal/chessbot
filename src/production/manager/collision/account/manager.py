# src/production/manager/collision/account/manager.py

"""
Module: production.manager.collision.account.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, AccountContext, HumanAccount, MachineAccount
from environment import AccountCollisionDetector
from err import AccountCollisionManagerException

from production import CollisionManager, HumanAccountAttractor, MachineAccountAttractor
from util import LoggingLevelRouter


class AccountCollisionManager(CollisionManager[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Detect if an insert breaks Account collection's uniqueness
            constraint.

    Attributes:
        human_account_attractor: HumanAccountAttractor
        machine_account_attractor: MachineAccountAttractor

    Provides:
        -   def execute(item: Account, collection: AccountStack) -> CollisionReport
        
    Super Class
        CollisionManager
    """
    _human_account_attractor: HumanAccountAttractor
    _machine_account_attractor: MachineAccountAttractor
    
    def __init__(
            self,
            detector: Optional[AccountCollisionDetector] | None = None,
            human_account_attractor: Optional[HumanAccountAttractor] | None = None,
            machine_account_attractor: Optional[MachineAccountAttractor] | None = None,
    ):
        """
        Args:
            detector: Optional[AccountCollisionDetector]
            human_account_attractor: Optional[HumanAccountAttractor]
            machine_account_attractor: Optional[MachineAccountAttractor]
        """
        super().__init__(detector=detector or AccountCollisionDetector())
        self._human_account_attractor = human_account_attractor or HumanAccountAttractor()
        self._machine_account_attractor = machine_account_attractor or MachineAccountAttractor()
        

    @property
    def detector(self) -> AccountCollisionDetector:
        return cast(AccountCollisionDetector, super().detector)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Account, particle_stream: AccountStack) -> CollisionReport:
        """
        Assure the item will be unique in the Account collection.
        
        Action:
            1.  If the item shares an attribute-value supposed to be unique to the
                collection, send an exception chain in the report.
            2.  Otherwise, report that primary keys will be maintained.
        Args:
            item: Account
            particle_stream: AccountStack
        Returns:
           CollisionReport
        Raises:
            AccountCollisionManagerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        report = CollisionReport.detector_failure(AccountCollisionManagerException())
        if isinstance(item, HumanAccount):
            report = self._human_account_attractor.execute(
                target=cast(HumanAccount, item),
                particle_stream=particle_stream,
            )
        if isinstance(item, MachineAccount):
            report = self._machine_account_attractor.execute(
                target=cast(MachineAccount, item),
                particle_stream=particle_stream,
            )
        # Handle the case that a detector component breaks.
        if report.detector_failure_exists:
            # Send an exception chain in the validation result.
            return CollisionReport.detector_failure(
                AccountCollisionManagerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountCollisionManagerException.MSG,
                    err_code=AccountCollisionManagerException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # Handle the case that a collision occurred.
        if report.collision_exists:
            context=cast(AccountContext, report.context)
            particle=cast(Account, report.particle)
            # Send an exception chain in the report.
            return CollisionReport.collision(
                particle=particle,
                context=context,
                exception=AccountCollisionManagerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountCollisionManagerException.MSG,
                    err_code=AccountCollisionManagerException.ERR_CODE,
                    ex=report.exception,
                )
            )
        return CollisionReport.empty()

        
        