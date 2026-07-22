# src/register/state.py

"""
Module: register.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


class Register(Any):
    """
    Role:
        -   Addressing
        -   Data-Holder
  
    Responsibilities:
        1.  Contains a pair used in a binary operation whose operands must have
            the same type.
        
    Attributes:
        a: Any
        b: Any
        id: Optional[int]
        to_list: List[Any]
        to_dict: Dict[str, Any]
        
    Provides:
    
    Super Class:
        Model
    """
    _a: Any
    _b: Any
    _id: Optional[int]
    
    def __init__(
            self,
            a: Any,
            b: Any,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            a: Any
            b: Any
        """
        self._a = a
        self._b = b
        self._id = id
    
    @property
    def a(self) -> Any:
        return self._a
    
    @property
    def b(self) -> Any:
        return self._b
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def to_list(self) -> List[Any]:
        return [self._a, self._b]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"a": self._a, "v": self._b}
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_right_size(self) -> bool:
        return self.size == 2
    
    @property
    def is_wrong_size(self) -> bool:
        return not (
                self.is_empty and self.is_right_size
        )
    
    @property
    def size(self) -> int:
        return len(self._to_list)