# src/chess/system/travel/event.py

"""
Module: chess.system.id.validator
Author: Banji Lawal
Created: 2025-08-11
Updated: 2025-10-10

# SECTION 1 - Purpose:
1. This module provides a satisfaction of the `ChessBot` consistency requirement. The module supplies consistency
      by providing a features for rollback activities.
    enforcement of regulations for unique IDs in the system.

# SECTION 2 - Scope:
The module only covers the basic properties and behavior objects in the `Event` domain.

# SECTION 3 - Limitations:
  1. Do not use this module directly. A stateful entity is responsible for
        * Having `Builders` which create subclasses for each state the entity has in its lifecycle.
        * Having `Validators` that ensure a transition will be successful.
  1. This module does not have any logic for executing a `Transaction` that changes an entity's state. Module
      `chess.system.travel.notification` is responsible for the `Event` lifecycle.
  2. The module does not verify the correctness of data control or routing information it contains. Directly using the
      module can breach data integrity, propagate inconsistencies or negatively impact performance. Use a
        * `Builder` for the
      DO NOT USE THE MODULE DIRECTLY. is not responsible for verifying the uniqueness of an ID. the `AutoId` class in
      `chess.system.id.auto_id` module.
  1. The module is not responsible for supplying or publishing IDs that meet system requirements.
      For details about publishing IDs see the `AutoId` class in module `chess.system.id.auto_id`.

# SECTION 4 - Design Considerations and Themes:
Major themes influencing the design include:
1. Easy and fast debugging.
2. Single responsibility, single source of truth.

# SECTION 5 - Features Supporting Requirements:
1. No direct support for any user level features.
2. Direct support for reliability, verification, and integrity.

# SECTION G - Feature Delivery Mechanism:
1. An rollback_exception for each requirement providing granular, accurate and precise error reporting.
2. Minimizing the boilerplate error handling and logging code with the `LoggingLevelRouter` decorator.
3. `IdValidator` can be used as component in more complex verifications.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ExecutionContext`,

* From Python `typing` Library:
    `Generic`, `TypeVar`, `Optional`

# SECTION 8 - Contains:
1. `Event`
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
  1. Transport data representing an entity's current state.
  2. A store of current states of an entities whose states might change.
  3. A reference for verifying success of a rollback notification.

  # PROVIDES:
  Information to execute a `Transaction` that could change the entity's state.

  Attributes:
    * `_actor` (`A`): The entity requesting the travel.
    * `__resource` (`R`): Component `actor_candidate` needs to change system state.
    * `_parent` (`Event`): The parent travel of this travel.
    * `_execution_environment` (`X`): The domain `actor_candidate` and `square` are in where the state change will happen
  """
  _id: int
  _actor: A
  __resource: Optional[R]
  _parent: Optional['Event']
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