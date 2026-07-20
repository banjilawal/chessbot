# src/model/target/model.py

"""
Module: model.target.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Optional

from container import VectorSet
from model import Vector


class TargetVectorSet(ABC):
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
    _hunter: Vector
    _group: VectorSet
    
    def __init__(
            self,
            hunter: Vector,
            group: Optional[VectorSet] | None = None,
    ):
        """
        Args:
            hunter: Vector
            group: Optional[VectorSet]
        """
        self._hunter = hunter
        self._group = group or VectorSet()
        
    @property
    def hunter(self) -> Vector:
        return self._hunter
    
    @property
    def group(self) -> VectorSet:
        return self.group
    
    @property
    def hunter_targeting_itself(self) -> bool:
        return self._hunter in self._group
    
    @property
    def hunter_not_targeting_itself(self) -> bool:
        return not self.hunter_targeting_itself
    
    @property
    def target_count(self) -> int:
        return self._group.size
    
    @property
    def targets_are_null(self) -> bool:
        return self._group is None
    
    @property
    def has_targets(self) -> bool:
        return self._group.is_not_empty
    
    @property
    def has_no_targets(self) -> bool:
        return not self.has_targets
    
    def remove_hunter_from_targets(self) -> TargetVectorSet:
        if self.hunter_not_targeting_itself:
            return self
        temp = []
        for target in self._group.to_list:
            if target != self.hunter:
                temp.append(target)
        return TargetVectorSet(
            hunter=self._hunter,
            group=VectorSet(tuple(temp))
        )
        
