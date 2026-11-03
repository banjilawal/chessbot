# src/sensor/detector/collision/detector.py

"""
Module: sensor.detector.collision.detector
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, cast

from artifcat import CollisionReport
from domain import Account, HumanAccount, MachineAccount
from sensor import Collider
from util import LoggingLevelRouter


class AccountCollider(Collider[Account]):
    

    @LoggingLevelRouter.monitor
    def execute(self, attractor: Account, items: List[Account]) -> CollisionReport:
        method = f"{self.__class__.__name__}.execute"
        
        report = CollisionReport(attractor=attractor)
        # Handle the case that there is an id collision
        for item in items:
            if item.id == attractor.id:
                return CollisionReport(
                    attractor=attractor,
                    collider=item,
                    identifier="id",
                    value=item.id,
                    exception=AccountColliderException(
                        AcountIdCollisionException()
                    )
            )
        # Handle the case that there is an email collision
        if isinstance(attractor, HumanAccount):
            return self._email_collider(attractor, self._humans(items))
        return self._machine_name_collider(attractor, self._machines(items))
        
    @LoggingLevelRouter.monitor
    def _email_collider(
            self,
            human_attractor: HumanAccount,
            items: List[HumanAccount]
    ) -> CollisionReport:
        for item in items:
            if human_attractor.email.upper() == item.email.upper():
                return CollisionReport(
                    attractor=human_attractor,
                    collider=item,
                    identifier="email",
                    value=item.email,
                    exception=AccountColliderException(
                        AcountEmailCollisionException()
                    )
                )
        return CollisionReport.free(attractor=human_attractor)
    
    @LoggingLevelRouter.monitor
    def _machine_name_collider(
            self,
            machine_attractor: MachineAccount,
            items: List[MachineAccount]
    ):
        for item in items:
            if machine_attractor.email.upper() == item.email.upper():
                return CollisionReport(
                    attractor=machine_attractor,
                    collider=item,
                    identifier="machine_name",
                    value=item.machine_name,
                    exception=AccountColliderException(
                        AcountMachineNameCollisionException()
                    )
                )
        return CollisionReport.free(attractor=machine_attractor)
    
    def _humans(self, items: List[Account]) -> List[HumanAccount]:
        matches: List[HumanAccount] = []
        for item in items:
            if isinstance(item, HumanAccount):
                matches.append(item)
        return matches
    
    def _machines(self, items: List[Account]) -> List[MachineAccount]:
        matches: List[MachineAccount] = []
        for item in items:
            if isinstance(item, MachineAccount):
                matches.append(item)
        return matches
    
    
