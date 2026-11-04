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
    """
    Role:
        -   Report

    Responsibilities:
        1.  Capture details about a duplicate attribute collision.

    Attributes:
        state: CollisionState
        collider: Optional[T]
        attractor: Optional[T]
        value: Optional[str]
        attribute: Optional[Any]
        exception:Optional[Exception]
        
        collision_occurred: bool
        no_collision_occurred: bool
        

    Provides:
        -   def no_collision_events() -> CollisionReport
        
        -   def collision_event(
                    collider: T,
                    attractor: T,
                    value: Any,
                    attribute: str,
                    exception: Exception,
            ) -> CollisionReport

    Super Class:
        Report
    """
    _state: CollisionState
    _collider: Optional[T]
    _attractor: Optional[T]
    _value: Optional[Any]
    _attribute: Optional[str]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            state: CollisionState,
            collider: Optional[T] | None = None,
            attractor: Optional[T] | None = None,
            value: Optional[str] | None = None,
            attribute: Optional[Any] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: CollisionState
            collider: Optional[T]
            attractor: Optional[T]
            value: Optional[str]
            attribute: Optional[Any]
            exception:Optional[Exception]
        """
        self._attractor = attractor
        self._state = state
        self._collider = collider
        self._value = value
        self._attribute = attribute
        self._exception = exception
        
    @property
    def state(self) -> CollisionState:
        return self._state
        
    @property
    def attractor(self) -> Optional[T]:
        return self._attractor
        
    @property
    def collider(self) -> Optional[T]:
        return self._collider
        
    @property
    def value(self) -> Optional[Any]:
        return self._value
        
    @property
    def attribute(self) -> Optional[str]:
        return self._attribute
        
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
        
    @property
    def collision_occurred(self) -> bool:
        return (
                self.value is not None and
                self._attribute is not None and
                self._collider is not None and
                self._exception is not None and
                self._attractor is not None and
                self._state == CollisionState.COLLISION_DETECTED
        )
        
    @property
    def no_collision_occurred(self) -> bool:
        return not self.collision_occurred
    
    @classmethod
    def no_collision_events(cls) -> CollisionReport:
        return cls(state=CollisionState.NO_COLLISIONS)
        
    @classmethod
    def collision_event(
            cls,
            collider: T,
            attractor: T,
            value: Any,
            attribute: str,
            exception: Exception,
    ) -> CollisionReport:
        return cls(
            value=value,
            collider=collider,
            attractor=attractor,
            attribute=attribute,
            exception=exception,
            state=CollisionState.COLLISION_DETECTED,
        )