"""
Module: chess.event.base
Author: Banji Lawal
Created: 2025-10-01
Version: 1.0.0

# Purpose
Data-holding object representing an`actor`'s intent to perform a state-changing operation with a `resource`.

# Contents:
    - `Event:` Super class of all events.

# Notes:
    DO NOT USE THESE EXCEPTIONS DIRECTLY. Limited use in the finally statement of a try-except block.
"""

from typing import Generic, TypeVar, Optional


A = TypeVar('A') # Actor Type
R = TypeVar('R') # Resource Type

class Event(Generic[A, R]):
    """
    A data-holding object representing an`actor`'s intent to perform a state-changing operation with a
    `resource`. An `Event` is passed to a `Transaction` instance that fires and manages the event lifecycle.
    During the event lifecycle the `actor` manipulates the `resource`.

    Attributes:
        _id (`int`): A unique identifier.
        _actor (`A`): The entity requesting the event.
        _resource (`R`): entity being manipulated by the `actor`.
        _parent (`Event`): The parent event of this event.
    """

    _id: int
    _actor: A
    _resource: Optional[R]
    _parent: Optional['Event']

    def __init__(
        self,
        event_id: int,
        actor: A,
        resource: Optional[R]=None,
        parent: Optional['Event']=None
    ):
        self._id = event_id
        self._actor = actor
        self._parent = parent
        self._resource = resource


    @property
    def id(self) -> int:
        return self._id

    @property
    def actor(self) -> A:
        return self._actor

    @property
    def resource(self) -> Optional[R]:
        return self._resource

    @property
    def parent(self) -> Optional['Event']:
        return self._parent

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Event):
            return False
        return self._id == other.id == other.id