# src/logic/system/context/service/service.py

"""
Module: logic.system.context.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import TypeVar

from logic.system import BuildProcess, Context, IntegrityService, ValidationProcess

T = TypeVar("T")

class ContextService(IntegrityService[Context[T]]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API for querying datasets of T objects.
    2.  Encapsulates Search and search filter validation in one extendable module.
    3.  Manage Context integrity lifecycle.

    Super Class:
        *   IntegrityService

    Provides:

    # LOCAL ATTRIBUTES:
        *   finder (SearchProcess[T])
        
    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    _finder: Finder[T]
    def __init__(
            self,
            id: int,
            name: str,
            builder: BuildProcess[Context[T]],
            validator: ValidationProcess[Context[T]],
            finder: Finder[T],
    ):
        """
        # ACTION:
            1.  Constructor

        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   finder (SearchProcess[T])
            *   builder (BuildProcess[Context[T]])
            *   validator (ValidationProcess[Context[T]])

        # RETURNS:
        None

        Raises:
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        method="ContextService.__init__"
        self._finder = finder
    
    @property
    def entity_finder(self) -> Finder[T]:
        """Get entity finder."""
        return self._finder
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, ContextService):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)