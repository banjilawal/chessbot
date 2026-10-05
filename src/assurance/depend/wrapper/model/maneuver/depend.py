# src/assurance/depend/wrapper/model/maneuver/depend.py

"""
Module: assurance.depend.wrapper.model.maneuver.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Maneuver
from exchange import PathValidationResponseWrapper, TokenValidationResponseWrapper


class ManeuverWrapperDependency(ModelWrapperDependency[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ManeuverValidator's ResponseWrapper dependencies.

    Attributes:
        path: PathValidationResponseWrapper
        token: TokenValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _path: PathValidationResponseWrapper
    _token: TokenValidationResponseWrapper
    
    def __init__(
            self,
            path: Optional[PathValidationResponseWrapper] | None = None,
            token: Optional[TokenValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            path: Optional[PathValidatorClient]
            token: Optional[TokenValidatorClient]
        """
        super().__init__()
        self._path = path or PathValidationResponseWrapper()
        self._token = token or TokenValidationResponseWrapper()
        
    @property
    def path(self) -> PathValidationResponseWrapper:
        return self._path
    
    @property
    def token(self) -> TokenValidationResponseWrapper:
        return self._token