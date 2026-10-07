# src/assurance/depend/wrapper/struct/model/depend.py

"""
Module: assurance.depend.wrapper.struct.model.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Footstep
from exchange import CoordValidationResponseWrapper


class FootstepDependency(ModelDependency[Footstep]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Model needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord: CoordValidationResponseWrapper

    Provides:

    Super Class:
        ModelDependency
    """
    _coord: CoordValidationResponseWrapper
    
    def __init__(
            self,
            coord: Optional[CoordValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            coord: Optional[CoordValidationResponseWrapper]
        """
        super().__init__()
        self._coord = coord or CoordValidationResponseWrapper()
        
    @property
    def coord(self) -> CoordValidationResponseWrapper:
        return self._coord