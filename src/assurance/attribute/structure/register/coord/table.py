# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterValidationWrapperDict, CoordValidatorClient
from domain import CoordRegister


class CoordRegisterHelperTable(RegisterValidationWrapperDict[CoordRegister]):
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
            coord_client: Optional[CoordValidatorClient] | None = None,
    ):
        """
        Args:
            coord_client: Optional[CoordValidatorClient]
        """
        super().__init__()
        self._coord_client = coord_client or CoordValidatorClient()
        
    @property
    def coord_client(self) -> CoordValidatorClient:
        return self.coord_client