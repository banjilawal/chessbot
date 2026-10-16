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
from domain import VectorRegister
from exchange import VectorValidationServer


class VectorRegisterDependency(RegisterDependency[VectorRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        vector: VectorValidationServer

    Provides:

    Super Class:
        RegisterDependency
    """
    _vector: VectorValidationServer
    
    def __init__(
            self,
            vector: Optional[VectorValidationServer] | None = None,
    ):
        """
        Args:
            vector: Optional[VectorValidationServer]
        """
        super().__init__()
        self._vector = vector or VectorValidationServer()
        
    @property
    def vector(self) -> VectorValidationServer:
        return self._vector