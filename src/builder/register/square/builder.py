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
from builder.register.builder import T
from model import Square
from register import SquareRegister
from toolkit import RegisterBuildToolkit
from util import LoggingLevelRouter


class SquareRegisterBuilder(RegisterBuilder[SquareRegister]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        build_toolkit: Optional[SquareRegisterBuildToolkit]
            
    Provides:

    Super Class:
        RegisterBuilder
    """
    
    def __init__(
            self,
            build_toolkit: Optional[SquareRegisterBuildToolkit] |
                           None = SquareRegisterBuildToolkit()
    ):
        """
        Args:
            build_toolkit: Optional[SquareRegisterBuildToolkit]
        """
        super().__init__(builder_toolkit=build_toolkit)

        
    @property
    def build_toolkit(self) -> SquareRegisterBuildToolkit:
        return cast(SquareRegisterBuildToolkit, super().build_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SquareRegisterBlueprint) -> BuildResult[SquareRegister]:
        pass


    
