# src/assurance/depend/wrapper/struct/node/depend.py

"""
Module: assurance.depend.wrapper.struct.node.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import NodeDependency
from domain import EncounterWarningNode
from exchange import EncounterValidationService


class EncounterWarningNodeDependency(NodeDependency[EncounterWarningNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Node needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        encounter: EncounterValidationServer

    Provides:

    Super Class:
        NodeDependency
    """
    _encounter: EncounterValidationService
    
    def __init__(
            self,
            encounter: Optional[EncounterValidationService] | None = None,
    ):
        """
        Args:
            encounter: Optional[EncounterValidationServer]
        """
        super().__init__()
        self._encounter = encounter or EncounterValidationService()
        
    @property
    def encounter(self) -> EncounterValidationService:
        return self._encounter