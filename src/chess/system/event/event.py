# src/chess/system/event/factory.py

"""
Module: chess.system.event.event
Author: Banji Lawal
Created: 2025-08-11
Updated: 2025-10-10
"""

from typing import Generic, TypeVar, Optional, cast
from chess.system import Event, LoggingLevelRouter

A = TypeVar('A') # Actor Type
R = TypeVar('R') # Resource Type
X = TypeVar('X') # ExecutionEnvironment Type


class Event(Generic[A, R, X]):
  """
  # ROLE: State Management, Data Transport, Abstract Data Type

  # RESPONSIBILITIES:
  1. Transport entity_service representing an entity's current state.
  2. A store of current states of an entities whose states might change.
  3. A reference for verifying success of a rollback notification.

  # PROVIDES:
  Information to execute a `Transaction` that could change the entity's state.

  Attributes:
    * `_actor` (`A`): The entity requesting the travel.
    * `__resource` (`R`): Component `actor_candidate` needs to change system state.
    * `_parent` (`Event`): The parent travel of this travel.
    * `_execution_environment` (`X`): The graph `actor_candidate` and `square` are in where the state change will happen
  """
  _id: int
  _actor: A
  __resource: Optional[R]
  _parent: Optional[Event]
  _execution_environment: X

  @LoggingLevelRouter.monitor
  def __init__(
    self,
    id: int,
    actor: A,
    execution_environment: X,
    resource: Optional[R]=None,
    parent: Optional['Event']=None
  ):
    self._id = id
    self._actor = actor
    self._parent = parent
    self._resource = resource
    self._execution_environment = execution_environment

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
  def parent(self) -> Optional[Event]:
    return self._parent


  @property
  def execution_environment(self) -> X:
    return self._execution_environment


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if isinstance(other, Event):
      event = cast(Event, other)
      return self._id == event.id
    return False

  def __hash__(self):
    return hash(self._id)