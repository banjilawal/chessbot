# src/kit/toolkit/collection/tree/tree.py

"""
Module: kit.toolkit.collection.tree.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Collection, List

# src/kit/toolkit/collection/toolkit.py

"""
Module: kit.toolkit.collection.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import PrimingValidator
from microservice import IdentityService

T = TypeVar("T", bound="Tree")


class TreeToolkit(CollectionToolkit, ABC, Generic[T]):
    """
    Role:
        -   Dependency Management

    Responsibilities:
        1.  Bundles dependencies a Collection worker needs to complete its task.
        2.  Loose Coupling between Collection workers and their resources.
        3.  Simplify Entry points.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        Toolkit
    """
    
    def __init__(
            self,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(identity_service=identity_service, priming_validator=priming_validator)


T = TypeVar("T")

class Tree(Collection, ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Data protection
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        items: Tuple[T, ...]

    Provides:

    Super Class:
    """
    _root: T
    _branches: List[Collection[T]]
    
    def __init__(self, root: T, branches: [Collection[T]]):
        self._root = root
        self._branches = branches
        
    @property
    def root(self) -> T:
        return self._root
    
    @property
    def branches(self) -> List[Collection[T]]:
        return self._branches
    

    @property
    def number_of_branches(self) -> int:
        return len(self._branches)
    
    
    @property
    def has_no_branches(self) -> bool:
        return self.number_of_branches == 0