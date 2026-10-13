# src/domain/metadata/blueprint/struct/node/warning/blueprint.py

"""
Module: domain.metadata.blueprint.struct.node.warning.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import EncounterWarning, NodeBlueprint, EncounterWarningNode
from err import EncounterWarningNodeNullException


class EncounterWarningNodeBlueprint(NodeBlueprint[EncounterWarningNode]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a EncounterWarningNode.

     Attributes:
        payload: Optional[EncounterWarning]
        next: Optional[EncounterWarning]
        Optional[Type[EncounterWarningNode]]
        domain_null_exception: Optional[EncounterWarningNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _payload: Optional[EncounterWarning]
    _next: Optional[EncounterWarning]
    _previous: Optional[EncounterWarning]
    
    def __init__(
            self,
            payload: Optional[EncounterWarning] | None = None,
            next: Optional[EncounterWarning] | None = None,
            previous: Optional[EncounterWarning] | None = None,
            domain_class: Optional[Type[EncounterWarningNode]] | None = None,
            domain_null_exception: Optional[EncounterWarningNodeNullException] | None = None,
    ):
        """
        Args:
            payload: Optional[EncounterWarning]
            next: Optional[EncounterWarning]
            previous: Optional[EncounterWarning]
            Optional[Type[EncounterWarningNode]]
            domain_null_exception: Optional[EncounterWarningNodeNullException]
        """
        super().__init__(
            domain_class=domain_class or EncounterWarningNode,
            domain_null_exception=domain_null_exception or EncounterWarningNodeNullException(),
        )
        self._payload = payload
        self._next = next
        self._previous = previous
        
    @property
    def payload(self) -> Optional[EncounterWarning]:
        return self._payload
    
    @property
    def next(self) -> Optional[EncounterWarning]:
        return self._next
    
    @property
    def previous(self) -> Optional[EncounterWarning]:
        return self._previous
    
    @property
    def domain_class(self) -> Type[EncounterWarningNode]:
        return cast(Type[EncounterWarningNode], super().domain_class)
    
    @property
    def domain_null_exception(self) -> EncounterWarningNodeNullException:
        return cast(EncounterWarningNodeNullException, super().domain_null_exception)
    
    
