# src/assurance/depend/wrapper/struct/register/depend.py

"""
Module: assurance.depend.wrapper.struct.register.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterDependency
from domain import CoordRegister
from exchange import CoordValidationResponseWrapper


class CoordRegisterDependency(RegisterDependency[CoordRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord: CoordValidationResponseWrapper

    Provides:

    Super Class:
        RegisterDependency
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