# src/model/context/persona/model.py

"""
Module: model.context.persona.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from model.catalog import Persona
from model import Context


class PersonaContext(Context[Persona]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Persona attribute-value tuple which selects an execution path.

    Attributes:
        name: Optional[str]
        quota: Optional[int]
        ransom: Optional[int]
        designation: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _name: Optional[str]
    _quota: Optional[int]
    _ransom: Optional[int]
    _designation: Optional[str]
    
    def __init__(
            self,
            name: Optional[str] = None,
            quota: Optional[int] = None,
            ransom: Optional[int] = None,
            designation: Optional[str] = None,
    ):
        """
        Args:
            name: Optional[str]
            quota: Optional[int]
            ransom: Optional[int]
            designation: Optional[str]
        """
        super().__init__(id=None, name=name)
        self._quota = quota
        self._ransom = ransom
        self._designation = designation
    
    @property
    def quota(self) -> Optional[int]:
        return self._quota
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema": self.designation,
            "ransom": self._ransom,
            "quota": self._quota,
            "designation": self.designation,
        }