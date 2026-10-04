# src/assurance/depend/wrapper/struct/register/depend.py

"""
Module: assurance.depend.wrapper.struct.register.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterWrapperDependency
from domain import VectorRegister


class VectorRegistryWrapperDependency(RegisterWrapperDependency[VectorRegister]):
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
            vector: Optional[VectorValidatorClient] | None = None,
    ):
        """
        Args:
            vector: Optional[VectorValidatorClient]
        """
        super().__init__()
        self._vector = vector or VectorValidatorClient()
        
    @property
    def vector(self) -> VectorValidatorClient:
        return self.vector