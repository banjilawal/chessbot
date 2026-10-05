# src/domain/metadata/blueprint/struct/node/warning.blueprint.py

"""
Module: domain.metadata.blueprint.struct.node.warning.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Warning, NodeBlueprint, WarningNode
from err import WarningNodeNullException


class EncounterWarningNodeBlueprint(NodeBlueprint[WarningNode]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a WarningNode.

     Attributes:
        victim: Warning
        attacker: Warning
        Optional[Type[WarningNode]]
        domain_null_exception: Optional[WarningNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _victim: Warning
    _attacker: Warning
    
    def __init__(
            self,
            victim: Warning,
            attacker: Warning,
            domain_class: Optional[Type[WarningNode]] | None = None,
            domain_null_exception: Optional[WarningNodeNullException] | None = None,
    ):
        """
        Args:
            victim: Warning
            attacker: Warning
            Optional[Type[WarningNode]]
            domain_null_exception: Optional[WarningNodeNullException]
        """
        super().__init__(
            domain_class=domain_class or WarningNode,
            domain_null_exception=domain_null_exception or WarningNodeNullException(),
        )
        self._victim = victim
        self._attacker = attacker
        
    @property
    def victim(self) -> Warning:
        return self._victim
    
    @property
    def attacker(self) -> Warning:
        return self._attacker
    
    @property
    def domain_class(self) -> Type[WarningNode]:
        return cast(Type[WarningNode], super().domain_class)
    
    @property
    def domain_null_exception(self) -> WarningNodeNullException:
        return cast(WarningNodeNullException, super().domain_null_exception)
    
    
