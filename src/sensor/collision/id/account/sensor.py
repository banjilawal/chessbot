# src/sensor/collision/id/account/sensor.py

"""
Module: sensor.collision.id.account.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account
from sensor import IdSensor
from util import LoggingLevelRouter


class AccountIdSensor(IdSensor[Account, int]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an AccountId has already been used.

    Attributes:

    Provides:
        -   def execute(target: int, stream: AccountStack) -> CollisionReport

    Super Class:
        IdSensor
    """

    @LoggingLevelRouter.monitor
    def execute(self, target: int, stream: AccountStack) -> CollisionReport:
        """
        Detect if the target_id exists in the AccountStack

        Action:
            1.  Send an exception chain in the report if an Account in the
                stream hits the target id.
            2.  Otherwise, report the attractor is unique.
        Args:
            target: int
            stream: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountIdSensorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Run the stream ---#
        matches = [item for item in stream.items if item.id == target]
        
        # Handle the case that no particle hits the target.
        if len(matches) == 0:
            return CollisionReport.no_collision_events()
        # Otherwise report a collision.
        return CollisionReport.collision_event(
            match=matches[0].id,
            target=target,
            particle=matches[0],
            identifier=self.ID_IDENTIFIER,
            exception=AccountIdSensorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=AccountIdSensorException.MSG,
                err_code=AccountIdSensorException.ERR_CODE,
                ex=DuplicteAccounIdException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DuplicteAccounIdException.MSG,
                    err_code=DuplicteAccounIdException.ERR_CODE,
                )
            )
        )

    
    
