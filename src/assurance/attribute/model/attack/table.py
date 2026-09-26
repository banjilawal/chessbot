# src/assurance/attrribute/model/attack/table.py

"""
Module: assurance.attrribute.model.attack.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, NumberValidator, PrimingValidator
from client import ManeuverValidatorClient, TokenValidatorClient
from domain import Attack
from microservice import IdentityService


class AttackHelperTable(ModelHelperTable[Attack]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients an Attack needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        token_client: TokenValidatorClient
        maneuver_client: ManeuverValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _token_client: TokenValidatorClient
    _maneuver_client: ManeuverValidatorClient
    
    def __init__(
            self,
            token_client: Optional[TokenValidatorClient] | None = None,
            maneuver_client: Optional[ManeuverValidatorClient] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            token_client: Optional[TokenValidatorClient]
            maneuver_client: Optional[ManeuverValidatorClient]
            identity_service: Optional[IdentityService]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            number_validator=number_validator,
            priming_validator=priming_validator,
        )
        self._token_client = token_client or TokenValidatorClient()
        self._maneuver_client = maneuver_client or ManeuverValidatorClient()
        
    @property
    def token_client(self) -> TokenValidatorClient:
        return self._token_client
    
    @property
    def maneuver_client(self) -> ManeuverValidatorClient:
        return self._maneuver_client