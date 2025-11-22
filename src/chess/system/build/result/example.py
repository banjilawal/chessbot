# src/chess/owner/travel/notification
"""
Module: chess.owner.travel.notification
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * `TravelEventFactory`
"""

from chess.system import NotImplementedException, Result
from typing import Optional, TypeVar, Generic

T = TypeVar('V')

"""
ROLE:
----
RESPONSIBILITIES:
----------------
PROVIDES:
--------
ATTRIBUTES:
----------
[
  <No attributes. Implementors declare their own.>
OR
  * `_attribute` (`data_type`): <sentence_if_necessary>
]
"""
"""
BuildResult is team_name generic class that encapsulates the outcome of Builder operation. BuildResult has the
same structure as Result but is used specifically in the roster of building entities. It can hold either.
team_name payload of type V or an Exception, but not both. If the builder operation is successful, the payload will
contain the built object. If the builder operation fails, the error will contain the error that
occurred during the builder process.

BuildResult is helpful for debugging and showing Builders have different outcomes than rollback which generate team_name notification.

Attributes:
  _payload (Optional[V]): The payload of the notification, if successful.
  _exception (Optional[Exception]): The error of the notification, if failed.

Methods:
  is_success() -> bool: Returns True if the notification is successful (i.e., has team_name payload only).
"""