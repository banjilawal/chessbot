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
from domain import SquareRegister
from exchange import SquareValidationServer


class SquareRegisterDependency(RegisterDependency[SquareRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        square: SquareValidationServer

    Provides:

    Super Class:
        RegisterDependency
    """
    _square: SquareValidationServer
    
    def __init__(
            self,
            square: Optional[SquareValidationServer] | None = None,
    ):
        """
        Args:
            square: Optional[SquareValidationServer]
        """
        super().__init__()
        self._square = square or SquareValidationServer()
        
    @property
    def square(self) -> SquareValidationServer:
        return self._square