# src/transit/route/sensor/account/router.py

"""
Module: transit.route.sensor.account.outer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CollisionReport
from assurance import AccountContextValidator
from collection import AccountStack
from domain import Account, AccountContext
from err import AccountSensorRouterException
from sensor import AccountEmailSensor, AccountIdSensor, MachineAccountNameSensor
from transit import SensorRouter
from util import LoggingLevelRouter


class AccountSensorRouter(SensorRouter[Account]):
    """
    Role
        -   Task Routing

    Responsibilities:
        1.  Route jobs to an AccountSensor by Context.

    Attributes:
        id_sensor: AccountIdSensor
        email_sensor: AccountEmailSensor
        machine_name_sensor: MachineAccountNameSensor
        context_validator: AccountContextValidator

    Provides:
        -   def execute(context: AccountContext) -> CollisionReport

    Super Class:
        SensorRouter
    """
    
    _email_sensor: AccountEmailSensor
    _machine_name_sensor: MachineAccountNameSensor
    
    def __init__(
            self,
            id_sensor: Optional[AccountIdSensor] | None = None,
            email_sensor: Optional[AccountEmailSensor] | None = None,
            machine_name_sensor: Optional[MachineAccountNameSensor] | None = None,
            context_validator: Optional[AccountContextValidator] | None = None,
    ):
        """
        Args:
            id_sensor: AccountIdSensor
            email_sensor: Optional[AccountEmailSensor]
            machine_name_sensor: Optional[MachineAccountNameSensor]
            context_validator: Optional[AccountContextValidator]
        """
        super().__init__(
            id_sensor=id_sensor or AccountIdSensor(),
            context_validator=context_validator or AccountContextValidator()
        )
        self._email_sensor = email_sensor or AccountEmailSensor()
        self._machine_name_sensor = machine_name_sensor or MachineAccountNameSensor()
        
    @property
    def id_sensor(self) -> AccountIdSensor:
        return cast(AccountIdSensor, super()._id_sensor)
    
    @property
    def context_validator(self) -> AccountContextValidator:
        return cast(AccountContextValidator, super().context_validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, context: AccountContext, stream: AccountStack) -> CollisionReport:
        """
        Report if an Account is already using the context attribute-value.

        Action:
            1.  Send an exception chain in the report if a sensor discovers
                a context match
            2.  Otherwise, report no collisions occurred.
        Args:
            context: AccountContext
            stream: AccountStack
        Result:
            CollisionReport
        Raises:
            AccountSensorRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        id = context.id
        email = context.email
        machine_name = context.machine_name
        key: str = ""
        
        report = CollisionReport.no_collision_events()
        
        if id is not None:
            key = "id"
            report = self._id_sensor.execute(target=id, stream=stream)
        if email is not None:
            key = "email"
            report = self._email_sensor.execute(target=email, stream=stream)
        if machine_name is not None:
            key = "machine_name"
            report = self._machine_name_sensor.execute(target=machine_name, stream=stream)
        if report.collision_exists:
            match = report.match
            target = report.target
            particle = cast(Account, report.particle)
            identifier = report.identifier or key
            
            return CollisionReport.collision_event(
                match=match,
                target=target,
                particle=particle,
                identifier=identifier,
                exception=AccountSensorRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSensorRouterException.MSG,
                    err_code=AccountSensorRouterException.ERR_CODE,
                    ex=report.exception,
                )
            )
        return CollisionReport.no_collision_events()
        
        
        
        