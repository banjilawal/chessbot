# src/chess/system/event/validator.py

"""
Module: chess.system.id.validator
Author: Banji Lawal
Created: 2025-08-11
Updated: 2025-10-10

# SECTION 1 - Purpose:
1. This module provides a satisfaction of the `ChessBot` integrity requirement. The satisfaction covers
    enforcement of regulations for unique IDs in the system.
2. This module provides a satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module only covers the properties and behavior of an event during a stateful entity's lifecycle.

# SECTION 3 - Limitations:
  1. This module is not responsible for verifying the uniqueness of an ID. the `AutoId` class in
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
1. An exception for each requirement providing granular, accurate and precise error reporting.
2. Minimizing the boilerplate error handling and logging code with the `LoggingLevelRouter` decorator.
3. `IdValidator` can be used as component in more complex verifications.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `Validator`, `NegativeIdException`, `IdNullException`, `InvalidIdException`

* From Python `typing` Library:
    `cast`

# SECTION 8 - Contains:
1. `IdValidator`
"""
from typing import Generic, TypeVar, Optional

from chess.event import ExecutionContext
from chess.system import auto_id

A = TypeVar('A') # Actor Type
R = TypeVar('R') # Resource Type


class Event(Generic[A, R]):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Team` instances.
  2. Create new `Team` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """
  """
  Super class of all events.

  Attributes:
    * `_actor` (`A`): The entity requesting the event.
    * `_resource` (`R`): entity being manipulated by the `actor`.
    * `_parent` (`Event`): The parent event of this event.
    * `_context` (`ExecutionContext`): Context of the `Event`.
  """

  _actor: A
  _resource: Optional[R]
  _parent: Optional['Event']
  _context: ExecutionContext

  def __init__(
    self,
    actor: A,
    context: ExecutionContext,
    resource: Optional[R]=None,
    parent: Optional['Event']=None,
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

  @property
  def context(self) -> ExecutionContext:
    return self._context


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, Event):
      return False
    return self._id == other.id == other.id