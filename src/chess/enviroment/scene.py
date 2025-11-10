# src/chess/environment/scene.py

"""
Module: chess.environment.scene
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from abc import ABC
from typing import Generic, Optional, TypeVar

A = TypeVar("A")
S = TypeVar("S")
P = TypeVar("P")


class Scene(ABC, Generic[A, S, P]):
    _id: int
    _actor: A
    _stage: S
    _prop: Optional[P]=None
    
    def __init__(self, id: int,  actor: A, stage: S, prop: Optional[P]=None):
        self._id = id
        self._actor = actor
        self._stage = stage
        self._prop = prop
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def actor(self) -> A:
        return self._actor
    
    @property
    def stage(self) -> S:
        return self._stage
    
    @property
    def prop(self) -> Optional[P]:
        return self._prop
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Scene):
            return self._id == other._id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
        
    