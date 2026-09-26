# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterHelperTable, VectorValidatorClient
from domain import VectorRegister


class VectorRegisterHelperTable(RegisterHelperTable[VectorRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        vector: VectorValidatorClient

    Provides:

    Super Class:
        RegisterHelperTable
    """
    _vector: VectorValidatorClient
    
    def __init__(
            self,
            vector_client: Optional[VectorValidatorClient] | None = None,
    ):
        """
        Args:
            vector_client: Optional[VectorValidatorClient]
        """
        super().__init__()
        self._vector_client = vector_client or VectorValidatorClient()
        
    @property
    def vector_client(self) -> VectorValidatorClient:
        return self.vector_client