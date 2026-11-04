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
from sensor import IdCollisionSensor
from util import LoggingLevelRouter


class AccountIdCollisionSensor(IdCollisionSensor[Account, int]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an AccountId has already been used.

    Attributes:

    Provides:
        -   def execute(attractor: int, collection: AccountStack) -> CollisionReport

    Super Class:
        IdCollisionSensor
    """

    @LoggingLevelRouter.monitor
    def execute(self, attractor: Account, collection: AccountStack) -> CollisionReport:
        """
        Check that the attractor will be unique in the collection.

        Action:
            1.  Send an exception chain in the report if the attractor
                finds a match.
            2.  Otherwise, report the attractor is unique.
        Args:
            attractor: int
            collection: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountIdCollisionSensorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Run the sensor. ---#
        target_id = attractor.id
        matches = [item for item in collection.items if item.id == target_id]
        
        # Handle the case that target_id is unique.
        if len(matches) == 0:
            return CollisionReport.no_collision_events()
        # Otherwise report there are duplicate ids.
        return CollisionReport.collision_event(
            attractor=attractor,
            collider=matches[0],
            attribute=self.ATTRIBUTE,
            value=target_id,
            exception=AccountIdCollisionSensorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=AccountIdCollisionSensorException.MSG,
                err_code=AccountIdCollisionSensorException.ERR_CODE,
                ex=DuplicteAccounIdException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DuplicteAccounIdException.MSG,
                    err_code=DuplicteAccounIdException.ERR_CODE,
                )
            )
        )

    
    
