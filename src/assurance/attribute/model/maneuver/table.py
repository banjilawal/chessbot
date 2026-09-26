# src/assurance/attrribute/model/maneuver/table.py

"""
Module: assurance.attrribute.model.maneuver.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelValidationWrapperDict, NumberValidator, PrimingValidator
from client import PathValidationResponseWrapper, TokenValidationResponseWrapper
from domain import Maneuver
from microservice import IdentityService


class ManeuverValidationWrapperDict(ModelValidationWrapperDict[Maneuver]):
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
    _path_client: PathValidationResponseWrapper
    _token_client: TokenValidationResponseWrapper
    
    def __init__(
            self,
            path_client: Optional[PathValidationResponseWrapper] | None = None,
            token_client: Optional[TokenValidationResponseWrapper] | None = None,
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
        self._path_client = path_client or PathValidationResponseWrapper()
        self._token_client = token_client or TokenValidationResponseWrapper()
        
    @property
    def path_client(self) -> PathValidationResponseWrapper:
        return self._path_client
    
    @property
    def token_client(self) -> TokenValidationResponseWrapper:
        return self._token_client