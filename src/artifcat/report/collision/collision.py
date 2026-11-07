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
A = TypeVar("A")

class CollisionReport(Report, Generic[T, A]):
    """
    Role:
        -   Report

    Responsibilities:
        1.  Capture details about a duplicate attribute collision.

    Attributes:
        state: CollisionState
        match: Optional[A]
        target: Optional[A]
        particle: Optional[T]
        identifier: Optional[str]
        exception:Optional[Exception]
        
        collision_occurred: bool
        no_collision_occurred: bool
        

    Provides:
        -   def no_collision_events() -> CollisionReport
        
        -   def collision_event(
                    match: A,
                    target: T,
                    particle: T,
                    identifier: str,
                    exception: Exception,
            ) -> CollisionReport

    Super Class:
        Report
    """
    _state: CollisionState
    _target: Optional[T]
    _particle: Optional[T]
    _field_name: Optional[str]
    _field_value: Optional[A]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            state: CollisionState,
            target: Optional[T] | None = None,
            particle: Optional[T] | None = None,
            field_name: Optional[str] | None = None,
            field_value: Optional[A] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: CollisionState
            target: Optional[T]
            particle: Optional[T]
            field_name: Optional[str]
            field_value: Optional[A]
            exception:Optional[Exception]
        """
        self._state = state
        self._target = target
        self._particle = particle
        self._field_name = field_name
        self._field_value = field_value
        self._exception = exception
        
    @property
    def state(self) -> CollisionState:
        return self._state
        
    @property
    def target(self) -> Optional[T]:
        return self._target
        
    @property
    def field_value(self) -> Optional[A]:
        return self._field_value
    
    @property
    def particle(self) -> Optional[T]:
        return self._particle
        
    @property
    def field_name(self) -> Optional[str]:
        return self._field_name
        
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def detector_failure_exists(self) -> bool:
        return (
                self._target is None and
                self._particle is None and
                self._field_name is None and
                self._field_value is None and
                self._exception is not None and
                self._state == CollisionState.DETECTOR_CRASHED
        )
        
    @property
    def collision_exists(self) -> bool:
        return (
                self._target is not None and
                self._particle is not None and
                self._field_name is not None and
                self._exception is not None and
                self._field_value is not None and
                self._state == CollisionState.DIFFERENT_ITEMS
        )
        
    @property
    def no_collision_exists(self) -> bool:
        return not self.collision_exists
    
    @classmethod
    def empty(cls) -> CollisionReport:
        return cls(state=CollisionState.NO_COLLISIONS)
    
    @classmethod
    def detector_failure(cls, exception) -> CollisionReport:
        return cls(exception=exception, state=CollisionState.DETECTOR_CRASHED)
    
    @classmethod
    def same_entity(cls, target: T, particle: T):
        pass
        
    @classmethod
    def entity_conflict(
            cls,
            match: A,
            target: T,
            particle: T,
            identifier: str,
            exception: Exception,
    ) -> CollisionReport:
        return cls(
            field_value=match,
            target=target,
            particle=particle,
            field_name=identifier,
            exception=exception,
            state=CollisionState.DIFFERENT_ITEMS,
        )