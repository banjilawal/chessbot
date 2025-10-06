"""
Module: chess.event.base
Author: Banji Lawal
Created: 2025-10-01
Version: 1.0.0

# Purpose
Data-holding object representing an`actor`'s intent to perform a state-changing operation with a `resource`.

# Contents:
  - `Event:` Super class of all events.
"""

from typing import Generic, TypeVar, Optional

from chess.event import ExecutionContext

A = TypeVar('A') # Actor Type
R = TypeVar('R') # Resource Type

@auto_id
class Event(Generic[A, R]):
  """

  Attributes:
    _id (`int`): A unique identifier.
    _actor (`A`): The entity requesting the event.
    _resource (`R`): entity being manipulated by the `actor`.
    _parent (`Event`): The parent event of this event.
  """

  _actor: A
  _resource: Optional[R]
  _parent: Optional['Event']
  _context: ExecutionContext

  def __init__(
    self,
    event_id: int,
    actor: A,
    resource: Optional[R]=None,
    parent: Optional['Event']=None,
    context: Optional[ExecutionContext]=None
  ):
    self._actor = actor
    self._parent = parent
    self._resource = resource
    self.context = context

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