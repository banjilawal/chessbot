# src/chess/system/context/service.py

"""
Module: chess.system.context.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import TypeVar

from chess.system import Builder, Context, EntityService, Finder, Validator

D = TypeVar("D")
C = TypeVar("C", bound=Context[D])

class ContextService(EntityService[D]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Search lists of an Entity.

    # PARENT
        *   EntityService

    # PROVIDES:
        *   ContextService

    # ATTRIBUTES:
    None
        *   finder (Finder[T])
    """
    _finder: Finder[D]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[C],
            validator: Validator[C],
            finder: Finder[D],
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._finder = finder
    
    @property
    def entity_finder(self) -> Finder[D]:
        return self._finder
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EntityService):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)