# src/sensor/collision/account/sensor.py

"""
Module: sensor.collision.account.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account, HumanAccount, MachineAccount
from sensor import CollisionSensor
from util import LoggingLevelRouter


class AccountCollisionSensor(CollisionSensor[Account]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an item violates the AttackStack uniqueness constraint.

    Attributes:

    Provides:
        -   def execute(
                    attractor: Account,
                    collection: AccountStack,
            ) -> CollisionReport

    Super Class:
        CollisionSensor
    """

    @LoggingLevelRouter.monitor
    def execute(self, attractor: Account, collection: AccountStack) -> CollisionReport:
        """
        Check that the attractor will be unique in the collection.

        Action:
            1.  Send an exception chain in the collision report if either duplicate;
                ids, emails, or machine_names are detected.
            2.  Otherwise, report the attractor is unique.
        Args:
            attractor: Account
            collection: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountCollisionSensorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Perform the check on the unique id attribute all Accounts have. ---#
        for item in collection.items:
            # Handle the case there are duplicate ids.
            if item.id == attractor.id:
                # Send an exception chain in the  report.
                return CollisionReport.collision_event(
                    attractor=attractor,
                    collider=item,
                    attribute="id",
                    value=item.id,
                    exception=AccountCollisionSensorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCollisionSensorException.MSG,
                        err_code=AccountCollisionSensorException.ERR_CODE,
                        ex=AccountIdCollisionException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=AccountIdCollisionException.MSG,
                            err_code=AccountIdCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- Run collision tests on unique sub class attributes. ---#
        
        # Human account uniqueness branch.
        if isinstance(attractor, HumanAccount):
            return self._human_account_collider(
                human_attractor=attractor,
                humans=collection.human_accounts,
                parent_method=method,
            )
        # Otherwise run the default sub-collider.
        return self._machine_account_collider(
                machine_attractor=attractor,
                machines=collection.machine_accounts,
                parent_method=method,
            )
            
    @LoggingLevelRouter.monitor
    def _human_account_collider(
            self,
            human_attractor: HumanAccount,
            humans: List[HumanAccount],
            parent_method: str
    ) -> CollisionReport:
        """duplicate_email_detector"""
        # Set up the target.
        attribute = "email"
        target = human_attractor.email.upper()
        
        # --- Run the collider. ---#
        for human in humans:
            # Handle the case that an email address is shared.
            if human.email.upper() == target:
                # Send an exception chain in the report.
                return CollisionReport.collision_event(
                    attractor=human_attractor,
                    collider=human,
                    attribute=attribute,
                    value=target,
                    exception=AccountCollisionSensorException(
                        cls_mthd=parent_method,
                        cls_name=self.__class__.__name__,
                        ex=AccountEmailCollisionException()
                    )
                )
        # Otherwise report the attractor is unique
        return CollisionReport.no_collision_events(attractor=human_attractor)
    
    @LoggingLevelRouter.monitor
    def _machine_account_collider(
            self,
            machine_attractor: MachineAccount,
            machines: List[MachineAccount],
            parent_method: str
    ):
        """duplicate_machine_name_detector"""
        # Set up the target.
        attribute = "machine_name"
        target = machine_attractor.name.upper()
        
        # --- Run the collider. ---#
        for machine in machines:
            # Handle the case that a machine_name is shared.
            if machine.name.upper() == target:
                # Send an exception chain in the report.
                return CollisionReport.collision_event(
                    attractor=machine_attractor,
                    collider=machine,
                    attribute=attribute,
                    value=target,
                    exception=AccountCollisionSensorException(
                        cls_mthd=parent_method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCollisionSensorException.MSG,
                        err_code=AccountCollisionSensorException.ERR_CODE,
                        ex=AccountMachineCollisionException()
                    )
                )
        # Otherwise report the attractor is unique.
        return CollisionReport.no_collision_events(attractor=machine_attractor)
    
    
