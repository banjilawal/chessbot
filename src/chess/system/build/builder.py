# src/chess/system/build/builder.py

"""
Module: chess.system.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import BuildResult, LoggingLevelRouter

T = TypeVar("T")

class Builder(ABC, Generic[T]):
  """
  # ROLE: Builder, Guarantee Data Integrity

  # RESPONSIBILITIES:
  Produce T instances whose integrity is always guaranteed. If any parameters do not pass their integrity checks,
  send an exception instead.

  # PROVIDES:
  BuildResult[T] containing either:
      - On success: T in the payload.
      - On failure: Exception.
      
  # ATTRIBUTES:
  None
  """

  @classmethod
  @abstractmethod
  @LoggingLevelRouter.monitor
  def build(cls, *args, **kwargs) -> BuildResult[T]:
    """
    # ACTION:
    1. Run integrity checks on each parameter required for constructing T.
    2. If any check fails it raises an exception that is returned inside a BuildResult.
    3. When all checks pass, construct T then return it inside a BuildResult.

    # PARAMETERS:
        * args: Parameters for constructing T.

    # Returns:
    BuildResult[T] containing either:
        - On success: T in the payload.
        - On failure: Exception.

    # RAISES:
      * BuildFailedException
    """
    pass