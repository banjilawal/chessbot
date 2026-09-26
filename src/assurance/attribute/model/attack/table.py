# src/assurance/attrribute/model/attack/table.py

"""
Module: assurance.attrribute.model.attack.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelValidationWrapperDict, NumberValidator, PrimingValidator
from client import ManeuverValidationResponseWrapper, TokenValidationResponseWrapper
from domain import Attack
from microservice import IdentityService


class AttackValidationWrapperDict(ModelValidationWrapperDict[Attack]):
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
    _token_client: TokenValidationResponseWrapper
    _maneuver_client: ManeuverValidationResponseWrapper
    
    def __init__(
            self,
            token_client: Optional[TokenValidationResponseWrapper] | None = None,
            maneuver_client: Optional[ManeuverValidationResponseWrapper] | None = None,
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
        self._token_client = token_client or TokenValidationResponseWrapper()
        self._maneuver_client = maneuver_client or ManeuverValidationResponseWrapper()
        
    @property
    def token_client(self) -> TokenValidationResponseWrapper:
        return self._token_client
    
    @property
    def maneuver_client(self) -> ManeuverValidationResponseWrapper:
        return self._maneuver_client