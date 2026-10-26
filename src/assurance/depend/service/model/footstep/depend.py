# src/assurance/depend/service/struct/model/depend.py

"""
Module: assurance.depend.service.struct.model.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Footstep
from exchange import CoordValidationService


class FootstepDependency(ModelDependency[Footstep]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Model needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord: CoordValidationService

    Provides:

    Super Class:
        ModelDependency
    """
    _coord: CoordValidationService
    
    def __init__(
            self,
            coord: Optional[CoordValidationService] | None = None,
    ):
        """
        Args:
            coord: Optional[CoordValidationService]
        """
        super().__init__()
        self._coord = coord or CoordValidationService()
        
    @property
    def coord(self) -> CoordValidationService:
        return self._coord