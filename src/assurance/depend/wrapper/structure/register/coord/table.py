# src/assurance/depend/wrapper/struct/register/depend.py

"""
Module: assurance.depend.wrapper.struct.register.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterWrapperDependency, CoordValidatorClient
from domain import CoordRegister


class CoordRegisterHelperTable(RegisterWrapperDependency[CoordRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord: CoordValidatorClient

    Provides:

    Super Class:
        RegisterHelperTable
    """
    _coord: CoordValidatorClient
    
    def __init__(
            self,
            coord: Optional[CoordValidatorClient] | None = None,
    ):
        """
        Args:
            coord: Optional[CoordValidatorClient]
        """
        super().__init__()
        self._coord = coord or CoordValidatorClient()
        
    @property
    def coord(self) -> CoordValidatorClient:
        return self.coord