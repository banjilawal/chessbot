# src/production/manager/sensor/account/manager.py

"""
Module: production.manager.sensor.account.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, AccountContext
from production import CollisionDetector
from transit import AccountSensorRouter
from util import LoggingLevelRouter


class AccountCollisionDetector(CollisionDetector[Account]):

    
    def __init__(self, router: Optional[AccountSensorRouter] | None = None):
        """
        Args:
            router: Optional[AccountSensorRouter]
        """
        super().__init__(router=router or AccountSensorRouter())
        
    @property
    def router(self) -> AccountSensorRouter:
        return cast(AccountSensorRouter, super().router)
    

    @LoggingLevelRouter.monitor
    def execute(self, context: AccountContext, stream: AccountStack) -> CollisionReport:
        """
        Detect if the name has been assigned to a MachineAccount.

        Action:
            1.  Send an exception chain in the report if an Account in the
                stream hits the target name.
            2.  Otherwise, report no collisions occurred.
        Args:
            context: AccountContext
            stream: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountCollisionDetectorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        attribute_name: str = ""
        table = context.to_dict()
        for key in table.keys():
            if table[key] is not None:
               attribute_name = key 
        
        report = self.router.execute(context=context, stream=stream)
        if report.collision_exists:
            if report.collision_exists:
                match = report.match
                target = report.target
                particle = cast(Account, report.particle)
                identifier = report.identifier or attribute_name
                
                return CollisionReport.collision_event(
                    match=match,
                    target=target,
                    particle=particle,
                    identifier=identifier,
                    exception=AccountCollisionDetectorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCollisionDetectorException.MSG,
                        err_code=AccountCollisionDetectorException.ERR_CODE,
                        ex=report.exception,
                    )
                )
        return CollisionReport.no_collision_events()