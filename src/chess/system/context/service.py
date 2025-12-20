# src/chess/system/context/service.py

"""
Module: chess.system.context.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import TypeVar

from chess.system import Builder, Context, EntityService, Finder, Validator

T = TypeVar("T")

class ContextService(EntityService[Context[T]]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API for querying datasets of T objects.
    2.  Encapsulates Search and search filter validation in one extendable module.
    3.  Manage Context integrity lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   ContextService

    # LOCAL ATTRIBUTES:
        *   finder (Finder[T])
        
    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    _finder: Finder[T]
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[Context[T]],
            validator: Validator[Context[T]],
            finder: Finder[T],
    ):
        """
        # Action:
            1.  Constructor

        # Parameters:
            *   designation (str)
            *   id (int)
            *   finder (Finder[T])
            *   builder (Builder[Context[T]])
            *   number_bounds_validator (Validator[Context[T]])

        # Returns:
        None

        # Raises:
        None
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