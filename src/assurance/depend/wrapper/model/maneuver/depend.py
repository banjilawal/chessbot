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
from exchange import PathValidationServer, TokenValidationServer


class ManeuverWrapperDependency(ModelWrapperDependency[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ManeuverValidator's ResponseWrapper dependencies.

    Attributes:
        path: PathValidationServer
        token: TokenValidationServer

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _path: PathValidationServer
    _token: TokenValidationServer
    
    def __init__(
            self,
            path: Optional[PathValidationServer] | None = None,
            token: Optional[TokenValidationServer] | None = None,
    ):
        """
        Args:
            path: Optional[PathValidatorClient]
            token: Optional[TokenValidatorClient]
        """
        super().__init__()
        self._path = path or PathValidationServer()
        self._token = token or TokenValidationServer()
        
    @property
    def path(self) -> PathValidationServer:
        return self._path
    
    @property
    def token(self) -> TokenValidationServer:
        return self._token