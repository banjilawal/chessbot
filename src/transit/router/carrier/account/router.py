# src/transit/route/carrier/account/router.py

"""
Module: transit.route.carrier.account.route
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from domain import Account, AccountBlueprint
from transit import CarrierRouter, HumanAccountCarrier, MachineAccountCarrier
from transit.router.carrier.router import T


class AccountCarrierRouter(CarrierRouter[Account]):
    _human_carrier: HumanAccountCarrier
    _machine_carrier: MachineAccountCarrier
    
    def __init__(
            self,
            model: Optional[Account],
            blueprint: Optional[AccountBlueprint],
            carrier: AccountCarrier,
            human_carrier: Optional[HumanAccountCarrier] | None = None,
            machine_carrier: Optional[MachineAccountCarrier] | None = None,
    ):
        """
        Args:
            model: Optional[Account]
            blueprint: Optional[AccountBlueprint]
            human_carrier: Optional[HumanAccountCarrier]
            machine_carrier: Optional[MachineAccountCarrier]
        """
        super().__init__(model=model, blueprint=blueprint)
        self._model = model
        self._blueprint = blueprint
        self._human_carrier = human_carrier or HumanAccountCarrier()
        self._machine_carrier = machine_carrier or MachineAccountCarrier()
        
    @property
    def model(self) -> Optional[Account]:
        return cast(Account, super().model)
    
    @property
    def blueprint(self) -> Optional[AccountBlueprint]:
        return cast(AccountBlueprint, super().blueprint)
    
    @property
    def entity(self, client: Any) -> [Account | AccountBlueprint]:
        if (
            client is None or
            not isinstance(client, HumanAccountCarrier)
        ):
            return None
            if is
            
    @property
    def human_carrier(self) -> HumanAccountCarrier:
        return self._human_carrier
    
    @property
    def machine_carrier(self) -> MachineAccountCarrier:
        return self._machine_carrier
    
    def extract_blueprint(self) -> Optional[AccountBlueprint]:
        if self.entity