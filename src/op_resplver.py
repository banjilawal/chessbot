# src/op_resolver.py

"""
Module: op_resolver
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations
from enum import Enum
from typing import Any, Union


from logic.system import BuildResult, Result, SearchResult, logging


class OperationResolver(Enum):
  @staticmethod
  def resolve(outcome: Union[Result, BuildResult, SearchResult], logger: logging.Logger) -> Union[Any, Exception]:
    """
    Logs the outcome and returns the payload or err.
    """

    if outcome.is_success():
      logger.info("✅ Success: %s", getattr(outcome, 'payload', None))
      return getattr(outcome, 'payload', None)

    exception = outcome.exception or ValueError("Unknown failure")
    logger.error("❌ Failure: %s", str(exception), exc_info=exception)
    return exception
