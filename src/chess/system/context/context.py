# src/chess/system/roster/roster.py

"""
Module: `chess.system.roster.roster`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Provides:
Interface to implement a `Context`

Contains:
 * `Context`
"""

from abc import ABC, abstractmethod


class Context(ABC):
  """
  Interface for defining optional dependencies an `Event` needs to execute a
  `Transaction`.

  Attributes:
    No attributes. Implementors declare their own.>
  """

  @abstractmethod
  def to_dict(self) -> dict:
    """
    Converts a roster's fields into a dictionary.
    Attributes:
      No attributes. Implementors declare their own.
    """
    pass
