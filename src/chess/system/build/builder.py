# src/chess/system/build/factory.py

"""
Module: chess.system.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import BuildResult, LoggingLevelRouter

T = TypeVar("V")

class Builder(ABC, Generic[T]):
  """
  # ROLE: Builder, Data Integrity and Reliability Guarantor.

  # RESPONSIBILITIES:
  1.  Produce V instances whose integrity is always guaranteed.
  1.  Uses Validator instances to verify build resources do not break safety contracts.
  2.  Wraps ValidatorExceptions inside BuildResult before returning to caller.
  3.  Performs any additional checks not covered by Validators to assure safety and integrity of new objects.


  # PROVIDES:
  BuildResult[V] containing either:
      - On success: V in the payload.
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
    1. Run integrity checks on each parameter required for constructing V.
    2. If any check fails it raises an exception that is returned inside a BuildResult.
    3. When all checks pass, construct V then return it inside a BuildResult.

    # PARAMETERS:
        * args: Parameters for constructing V.

    # Returns:
    BuildResult[V] containing either:
        - On success: V in the payload.
        - On failure: Exception.

    # RAISES:
      * BuildFailedException
    """
    pass