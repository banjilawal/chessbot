# src/chess/system/scene/scene.py

"""
Module: chess.system.scene.scene
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
    """
    # ROLE:
    
    # RESPONSIBILITIES:
    
    # PROVIDES:
        `Scene`
      
    # ATTRIBUTES:
        `id`: `int`
        `actor`: `A` Entity performing rollback on `Stage`.
        `stage`: `S` Region containing `actor` and any `prop` they need.
        `prop`: `P` Resource `actor` may need for their operation
    """
    
    _id: int
    _actor: A
    _stage: S
    _prop: Optional[P]=None
    
    def __init__(self, id: int,  actor: A, stage: S, prop: Optional[P]=None):
        """
        # ACTION:
        Constructs a new `Scene`.

        # PARAMETERS:
            * `id` (`int`):
            * `actor` (`A`): Performs rollback on `Stage`.
            * `stage` (`S`): Environment whose `actor` interacts with entities.
            * `prop` (`P`): Resource `actor` may need for their rollback.

        # RETURNS:
            `None`

        # RAISES:
            `None`
        """
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
        
    