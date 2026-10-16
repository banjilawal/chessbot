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
from exchange import CoordValidationServer


class CoordRegisterDependency(RegisterDependency[CoordRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord: CoordValidationServer

    Provides:

    Super Class:
        RegisterDependency
    """
    _coord: CoordValidationServer
    
    def __init__(
            self,
            coord: Optional[CoordValidationServer] | None = None,
    ):
        """
        Args:
            coord: Optional[CoordValidationServer]
        """
        super().__init__()
        self._coord = coord or CoordValidationServer()
        
    @property
    def coord(self) -> CoordValidationServer:
        return self._coord