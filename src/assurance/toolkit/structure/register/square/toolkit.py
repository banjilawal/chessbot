# src/assurance/toolkit/structure/register/square/toolkit.py

"""
Module: assurance.toolkit.structure.register.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterValidatorToolkit, SquareRegisterHelperTable
from domain import SquareRegister, SquareRegisterManifest


class SquareRegisterValidatorToolkit(RegisterValidatorToolkit[SquareRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            helper: SquareRegisterHelperTable
            metadata: SquareRegisterManifest

    Provides:

    Super Class:
       RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            helper: Optional[SquareRegisterHelperTable] | None = None,
            metadata: Optional[SquareRegisterManifest] | None = None,
    ):
        """
            helper: Optional[SquareRegisterHelperTable]
            metadata: Optional[SquareRegisterManifest]
        """
        super().__init__(
            helper=helper or SquareRegisterHelperTable(),
            metadata=metadata or SquareRegisterManifest(),
        )
    
    @property
    def helper(self) -> SquareRegisterHelperTable:
        return cast(SquareRegisterHelperTable, super().helper)
    
    @property
    def metadata(self) -> SquareRegisterManifest:
        return cast(SquareRegisterManifest, super().metadata)