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
from domain import Context, Model
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class CollisionReport(Report, Generic[T]):
    """
    Role:
        -   Report

    Responsibilities:
        1.  Capture details about a duplicate attribute collision.

    Attributes:
        state: CollisionState
        match: Optional[A]
        attractor: Optional[A]
        particle: Optional[T]
        identifier: Optional[str]
        exception:Optional[Exception]
        
        collision_occurred: bool
        no_collision_occurred: bool
        

    Provides:
        -   def no_collision_events() -> CollisionReport
        
        -   def collision_event(
                    match: A,
                    attractor: T,
                    particle: T,
                    identifier: str,
                    exception: Exception,
            ) -> CollisionReport

    Super Class:
        Report
    """
    _state: CollisionState
    _attractor: Optional[ModelCarrier[T]]
    _particle: Optional[T]
    _context: Optional[Context[T]]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            state: CollisionState,
            attractor: Optional[T] | None = None,
            particle: Optional[T] | None = None,
            context: Optional[Context[T]] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: CollisionState
            attractor: Optional[T]
            particle: Optional[T]
            context: Optional[Context[T]]
            exception:Optional[Exception]
        """
        self._state = state
        self._attractor = attractor
        self._particle = particle
        self._context = context
        self._exception = exception
        
    @property
    def state(self) -> CollisionState:
        return self._state
        
    @property
    def attractor(self) -> Optional[T]:
        return self._attractor
    
    @property
    def particle(self) -> Optional[T]:
        return self._particle
        
    @property
    def context(self) -> Optional[Context[T]]:
        return self._context
        
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def detector_failure_exists(self) -> bool:
        return (
                self._attractor is None and
                self._particle is None and
                self._context is None and
                self._exception is not None and
                self._state == CollisionState.DETECTOR_CRASHED
        )
        
    @property
    def collision_exists(self) -> bool:
        return (
                self._particle is not None and
                self._context is not None and
                self._exception is not None and
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
    def collision(
            cls,
            particle: T,
            context: Context[T],
            exception: Exception,
    ) -> CollisionReport:
        return cls(
            particle=particle,
            context=context,
            exception=exception,
            state=CollisionState.DIFFERENT_ITEMS,
        )