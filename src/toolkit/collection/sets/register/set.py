# src/toolkit/collection/sets/register/set.py

"""
Module: toolkit.collection.sets.register.set
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, Optional, Tuple, cast

from collection import SetCollection
from register import Register


class RegisterSet(SetCollection[Register]):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  A bag of registers whose order is not guaranteed.

    Attributes:
        items: Tuple[Register, ...]

    Provides:

    Super Class:
        Collection
    """
    
    def __init__(self, items: Optional[Tuple[Register, ...]] | None = None):
        """
        Args:
            items: Optional[Tuple[Register, ...]]
        """
        super().__init__(items=items)
        
    @property
    def items(self) -> Tuple[Register, ...]:
        return cast(Tuple[Register, ...], self.items)
    
    @property
    def iterator(self) -> Iterator[Register]:
        return iter(self.items)
        