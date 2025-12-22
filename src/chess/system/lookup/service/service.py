# src/chess/system/lookup/service/service.py

"""
Module: chess.system.lookup.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from enum import Enum

from chess.system import Builder, Context, ContextService, ForwardLookup, Validator
from chess.system.lookup.reverse import ReverseLookup


class LookupService(ContextService[Context[Enum]]):
    """
     # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

     # RESPONSIBILITIES:
     1.  Public facing microservice API.
     2.  Encapsulate integrity assurance logic in one extendable module.
     3.  Is authoritative, single-source-of-truth for an entity's state by providing single entry and exit points to
         the entity's lifecycle.
     4.  Bundles  operations that produce different Result subclasses.

     # PARENT:
         *  ContextService

     # PROVIDES:
     None

     # LOCAL ATTRIBUTES:
        *   forward_lookup (ForwardLookup)
        *   reverse_lookup (ReverseLookup)

     # INHERITED ATTRIBUTES:
         *  See ContextService for inherited attributes.
     """
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API for querying datasets of T objects.
    2.  Encapsulates Search and search filter validation in one extendable module.
    3.  Manage Context integrity lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   finder (Finder[T])

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    _forward_lookup: ForwardLookup
    _reverse_lookup: ReverseLookup
    
    def service(
            self,
            id: int,
            name: str,
            builder: Builder[Context[Enum]],
            validator: Validator[Context[Enum]],
            forward_lookup: ForwardLookup,
            reverse_lookup: ReverseLookup
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._forward_lookup = forward_lookup
        self._reverse_lookup = reverse_lookup
        
    @property
    def forward_lookup(self) -> ForwardLookup:
        return self._forward_lookup
    
    @property
    def __reversed__(self) -> ReverseLookup:
        return self._reverse_lookup