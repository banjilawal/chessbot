# src/chess/event/roster.py

"""
Module: `chess.event.roster`
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0

Provides:
Implementation of `Context` interface

Contains:
 * `ExecutionContext`
"""

from abc import ABC
from chess.system import Context

class ExecutionContext(ABC, Context):
  """
  Super class of dependencies an `Event` passes to a `Transaction`.

  Attributes:
    No attributes. Subclasses declare their own.
  """