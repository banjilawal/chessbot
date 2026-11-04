# src/sensor/collision/account/email/sensor.py

"""
Module: sensor.collision.account.email.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import CollisionReport
from collection import AccountStack
from domain import HumanAccount
from sensor import AccountSensor
from util import LoggingLevelRouter


class AccountEmailSensor(AccountSensor[HumanAccount, str]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an email has already been used.

    Attributes:

    Provides:
        -   def execute(target: str, stream: AccountStack) -> CollisionReport

    Super Class:
        EmailSensor
    """

    @LoggingLevelRouter.monitor
    def execute(self, target: str, stream: AccountStack) -> CollisionReport:
        """
        Detect if the target attribute exists in the AccountStack

        Action:
            1.  Send an exception chain in the report if an Account in the
                stream hits the target email.
            2.  Otherwise report no collisions occurred..
        Args:
            target: str
            stream: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountEmailSensorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Run the stream ---#
        matches = [
            item for item in stream.human_accounts if (
                    item.email.upper() == target.upper()
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
            identifier="email",
            exception=AccountEmailSensorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=AccountEmailSensorException.MSG,
                err_code=AccountEmailSensorException.ERR_CODE,
                ex=DuplicteAccountEmailException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DuplicteAccountEmailException.MSG,
                    err_code=DuplicteAccountEmailException.ERR_CODE,
                )
            )
        )

    
    
