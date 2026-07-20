# src/builder/register/square/builder.py

"""
Module: builder.register.square.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import RegisterBuilder
from model import Square
from register import SquareRegister
from util import LoggingLevelRouter


class SquareRegisterBuilder(RegisterBuilder[SquareRegister]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        origin: Square
        destination: Square
        origin_is_destination: bool
        origin_is_not_destination: bool
            
    Provides:

    Super Class:
        Register
    """
    
    def __init__(
            self,
            origin: Square,
            destination: Square,
            endpoint_validator: Optional[SquareValidator] | None = SquareValidator()):
        """
        Args:
            origin: Square
            destination: Square
            endpoint_validator: Optional[SquareValidator]
        """
        super().__init__(
            a=origin,
            b=destination,
            endpoint_validator=endpoint_validator
        )

        
    @property
    def origin(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)
    
    @property
    def endpoint_validator(self) -> SquareValidator:
        return cast(SquareValidator, self.endpoint_validator)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[SquareRegister]:
        pass


    
