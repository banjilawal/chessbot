# src/report/collision/collision.py

"""
Module: report.collision.collision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Generic, Optional, TypeVar

from artifcat import CollisionState, Report
from domain import Model

T = TypeVar("T", bound="Model")

class CollisionReport(Report, Generic[T]):
    _attractor: T
    _state: CollisionState
    _collider: Optional[T]
    _value: Optional[Any]
    _identifier: Optional[str]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            attractor: T,
            state: CollisionState,
            collider: Optional[T] | None = None,
            value: Optional[str] | None = None,
            identifier: Optional[Any] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            attractor: T
            state: CollisionState
            collider: Optional[T]
            value: Optional[str]
            identifier: Optional[Any]
            exception:Optional[Exception]
        """
        self._attractor = attractor
        self._state = state
        self._collider = collider
        self._value = value
        self._identifier = identifier
        self._exception = exception
        
    @property
    def state(self) -> CollisionState:
        return self._state
        
    @property
    def attractor(self) -> T:
        return self._attractor
        
    @property
    def collider(self) -> Optional[T]:
        return self._collider
        
    @property
    def value(self) -> Optional[Any]:
        return self._value
        
    @property
    def identifier(self) -> Optional[str]:
        return self._identifier
        
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
        
    @property
    def collision_exists(self) -> bool:
        return (
            self.value is not None and
            self._identifier is not None and
            self._collider is not None and
            self._exception is not None and
            self._attractor is not None and
            self._state == CollisionState.COLLISION_DETECTED
        )
        
    @property
    def no_collision_exists(self) -> bool:
        return not self.collision_exists
    
    @classmethod
    def free(cls, attractor: T) -> CollisionReport:
        return cls(
            attractor=attractor,
            state=CollisionState.NO_COLLISIONS,
        )
        
    @classmethod
    def hit(
            cls,
            value: Any,
            identifier: str,
            collider: T,
            attractor: T,
            exception: Exception,
    ) -> CollisionReport:
        return cls(
            value=value,
            collider=collider,
            attractor=attractor,
            identifier=identifier,
            exception=exception,
            state=CollisionState.COLLISION_DETECTED,
        )