# src/space/target/linear/space.py

"""
Module: space.target.linear.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast


from model import Vector
from register import VectorRegister
from space import TargetVectorSet


class TargetSpanSet(TargetVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Stores vectors that can be journeyed to from the root.

    Attributes:
        root: Vector
        targets: VectorSet

    Provides:

    Super Class:
    """
    _root: Vector
    _targets: VectorSet
    
    def __init__(
            self,
            root: Vector,
            targets: Optional[VectorSet] | None = None,
    ):
        """
        Args:
            root: Vector
            targets: Optional[VectorSet]
        """
        self._root = root
        self._targets = targets or VectorSet()
    
    @property
    def root(self) -> Vector:
        return self._root
    
    @property
    def targets(self) -> VectorSet:
        return self.targets
    
    @property
    def root_is_a_target(self) -> bool:
        return self._root in self._targets
    
    @property
    def root_is_not_target(self) -> bool:
        return not self.root_is_a_target
    
    @property
    def target_count(self) -> int:
        return self._targets.size
    
    @property
    def targets_are_null(self) -> bool:
        return self._targets is None
    
    @property
    def has_targets(self) -> bool:
        return self._targets.is_not_empty
    
    @property
    def has_no_targets(self) -> bool:
        return not self.has_targets
    
    def remove_root_from_targets(self) -> TargetVectorSet:
        if self.root_is_not_target:
            return self
        temp = []
        for target in self._targets.to_list:
            if target != self.root:
                temp.append(target)
        return TargetVectorSet(
            root=self._root,
            targets=VectorSet(tuple(temp))
        )
        

        