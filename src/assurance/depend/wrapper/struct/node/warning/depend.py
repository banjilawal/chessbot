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
from exchange import EncounterValidationResponseWrapper


class EncounterWarningNodeDependency(NodeDependency[EncounterWarningNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Node needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        warning: EncounterValidationResponseWrapper

    Provides:

    Super Class:
        NodeDependency
    """
    _warning: EncounterValidationResponseWrapper
    
    def __init__(
            self,
            warning: Optional[EncounterValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            warning: Optional[EncounterValidationResponseWrapper]
        """
        super().__init__()
        self._warning = warning or EncounterValidationResponseWrapper()
        
    @property
    def warning(self) -> EncounterValidationResponseWrapper:
        return self._warning