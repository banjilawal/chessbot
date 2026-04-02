# # src/logic/system/search/context/mode/root.py
#
# """
# Module: logic.system.search.context.model.root
# Author: Banji Lawal
# Created: 2025-11-18
# Version: 1.0.0
# """

from typing import Generic, Optional, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class Context(ABC, Generic[T]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply an attribute-value pair for selecting an execution path among different routes.
                
    Attributes:
        id: Optional[int]
        stack: Optional[str]
        
    Provides:
        -   to_dict() -> Dict[str, Any]
        
    Super Class:
    
    Notes:
        1.  Attribute is an entity's property.
        2.  Attribute is routing key.
        3.  Execution logic performed on attribute value.
        
        4.  Why Not Union:
                Used optional attributes with null default values instead of a union type because:
                    -   It's easier to extend
                    -   Implementations can decide if context can be mutually exclusive or not.
                    -   Unions are clunky if there are many attributes.
                    -   Unions don't lower validation and build integrity overhead.
    """
    _id: Optional[int]
    _name: Optional[str]
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
        """
        self._id = id
        self._name = name
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def designation(self) -> Optional[str]:
        return self._name
    
    @abstractmethod
    def to_dict(self) -> dict:
        """Implementations must override."""
        pass