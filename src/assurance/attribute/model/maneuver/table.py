# src/assurance/attrribute/model/maneuver/table.py

"""
Module: assurance.attrribute.model.maneuver.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, NumberValidator, PrimingValidator
from client import PathValidatorClient, TokenValidatorClient
from domain import Maneuver
from microservice import IdentityService


class ManeuverHelperTable(ModelHelperTable[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Maneuver needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        path_client: PathValidatorClient
        token_client: TokenValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _path_client: PathValidatorClient
    _token_client: TokenValidatorClient
    
    def __init__(
            self,
            path_client: Optional[PathValidatorClient] | None = None,
            token_client: Optional[TokenValidatorClient] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            path_client: Optional[PathValidatorClient]
            token_client: Optional[TokenValidatorClient]
            identity_service: Optional[IdentityService]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            number_validator=number_validator,
            priming_validator=priming_validator,
        )
        self._path_client = path_client or PathValidatorClient()
        self._token_client = token_client or TokenValidatorClient()
        
    @property
    def path_client(self) -> PathValidatorClient:
        return self._path_client
    
    @property
    def token_client(self) -> TokenValidatorClient:
        return self._token_client