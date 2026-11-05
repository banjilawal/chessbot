# src/sensor/collision/account/name/sensor.py

"""
Module: sensor.collision.account.name.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import CollisionReport
from collection import AccountStack
from domain import MachineAccount
from sensor import AccountSensor
from util import LoggingLevelRouter


class MachineAccountNameSensor(AccountSensor[MachineAccount, str]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if a name has already been used.

    Attributes:

    Provides:
        -   def execute(target: str, stream: AccountStack) -> CollisionReport

    Super Class:
        NameSensor
    """

    @LoggingLevelRouter.monitor
    def execute(self, target: str, stream: AccountStack) -> CollisionReport:
        """
        Detect if the name has been assigned to a MachineAccount.

        Action:
            1.  Send an exception chain in the report if an Account in the
                stream hits the target name.
            2.  Otherwise, report no collisions occurred.
        Args:
            target: str
            stream: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountNameSensorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Run the stream ---#
        matches = [
            item for item in stream.machine_accounts if (
                    item.name.upper() == target.upper()
            )
        ]
        # Handle the case that no particle hits the target.
        if len(matches) == 0:
            return CollisionReport.no_collision_events()
        # Otherwise report a collision.
        return CollisionReport.collision_event(
            match=matches[0].id,
            target=target,
            particle=matches[0],
            identifier="name",
            exception=AccountNameSensorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=AccountNameSensorException.MSG,
                err_code=AccountNameSensorException.ERR_CODE,
                ex=DuplicteAccountNameException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DuplicteAccountNameException.MSG,
                    err_code=DuplicteAccountNameException.ERR_CODE,
                )
            )
        )

    
    
