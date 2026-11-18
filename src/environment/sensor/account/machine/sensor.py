# src/environment/environment/account/machine/sensor.py

"""
Module: environment.sensor.account.machine.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import CollisionReport
from collection import AccountStack
from domain import AccountContext, MachineAccount
from environment import AccountSensor
from err import DuplicateMachineNameException, MachineAccountNameSensorException
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
            MachineAccountNameSensorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Run the stream ---#
        context = AccountContext(machine_name=target)
        matches = [
            item for item in stream.machine_accounts if (
                    item.name.upper() == target.upper()
            )
        ]
        # Handle the case that no particle hits the target.
        if len(matches) == 0:
            return CollisionReport.empty()
        # Otherwise report a collision.
        return CollisionReport.collision(
            particle=matches[0],
            context=context,
            exception=MachineAccountNameSensorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=MachineAccountNameSensorException.MSG,
                err_code=MachineAccountNameSensorException.ERR_CODE,
                ex=DuplicateMachineNameException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DuplicateMachineNameException.MSG,
                    err_code=DuplicateMachineNameException.ERR_CODE,
                    var=f"collider_id: {matches[0].id}, "
                        f"duplicate_machine_name: {target}",
                )
            )
        )

    
    
