# src/chess/event/context.py

"""
Module: `chess.event.context`
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0

Provides:
Data dependencies an `actor` and `resource` need to execute a `Transaction`.

Contains:
 * `ExecutionContext`
"""

from abc import ABC
from chess.system import Context

class ExecutionContext(ABC, Context):
  """
  Abstract Data Type of execution dependencies an `Event` passes to
  a `Transaction`.

  Attributes:
    No attributes. Subclasses declare their own.
  """