# src/assurance/depend/service/model/maneuver/depend.py

"""
Module: assurance.depend.service.model.maneuver.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Maneuver
from exchange import PathValidationService, TokenValidationService


class ManeuverDependency(ModelDependency[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ManeuverValidator's ResponseService dependencies.

    Attributes:
        path: PathValidationService
        token: TokenValidationService

    Provides:

    Super Class:
        ModelDependency
    """
    _path: PathValidationService
    _token: TokenValidationService
    
    def __init__(
            self,
            path: Optional[PathValidationService] | None = None,
            token: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            path: Optional[PathValidatorClient]
            token: Optional[TokenValidatorClient]
        """
        super().__init__()
        self._path = path or PathValidationService()
        self._token = token or TokenValidationService()
        
    @property
    def path(self) -> PathValidationService:
        return self._path
    
    @property
    def token(self) -> TokenValidationService:
        return self._token