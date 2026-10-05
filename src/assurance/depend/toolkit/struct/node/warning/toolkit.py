# src/assurance/depend/toolkit/struct/node/warning/toolkit.py

"""
Module: assurance.depend.toolkit.struct.node.warning.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import NodeValidatorToolkit, EncounterWarningNodeDependency
from domain import (
    EncounterWarningNode, EncounterWarningNodeManifest, EncounterWarningNodeNullGroup,
    EncounterWarningNodeTypeUnion
)


class EncounterWarningNodeValidatorToolkit(NodeValidatorToolkit[EncounterWarningNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: EncounterWarningNodeDependency
            metadata: EncounterWarningNodeManifest

    Provides:

    Super Class:
       NodeValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[EncounterWarningNodeDependency] | None = None,
            metadata: Optional[EncounterWarningNodeManifest] | None = None,
    ):
        """
            wrapper: Optional[EncounterWarningNodeDependency]
            metadata: Optional[EncounterWarningNodeManifest]
        """
        super().__init__(
            wrapper=wrapper or EncounterWarningNodeDependency(),
            metadata=metadata or EncounterWarningNodeManifest(),
        )
    
    @property
    def wrapper(self) -> EncounterWarningNodeDependency:
        return cast(EncounterWarningNodeDependency, super().wrapper)
    
    @property
    def metadata(self) -> EncounterWarningNodeManifest:
        return cast(EncounterWarningNodeManifest, super().metadata)
    
    @property
    def nulls(self) -> EncounterWarningNodeNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> EncounterWarningNodeTypeUnion:
        return self.metadata.types