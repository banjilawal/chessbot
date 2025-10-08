# src/chess/system/err/handler
"""
Module: chess.system.err.handler
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
 * `OccupationTransaction`
"""

import inspect
import logging
from typing import Callable, TypeVar, Any, Optional, Dict

T = TypeVar('T')

class LogWriter:
  """
  ROLE:
  ----
  Reporting, logging

  RESPONSIBILITIES:
  ----------------
  1. Centralizing logger access for info and error reporting.
  PROVIDES:
  --------
  ATTRIBUTES:
  ----------
  None
  """

  @staticmethod
  def resolve_context_info(context: Any, function: Optional[Callable]=None) -> Dict[str, str]:
      """
      Action:
        Derive `context` metadata for logging, including
          - file name
          - module name
          - class name
          - function name when its available

      Parameters:
        * `context (`Any`)`:
        * `function` (`Callable`):

      Returns:
        Dict

      Raises:
        None
      """
      method = "LogWriter.resolve_context_info"

      frame = inspect.currentframe()
      caller_frame = frame.f_back if frame and frame.f_back else None

      module = inspect.getmodule(caller_frame)
      module_name = module.__name__ if module is not None else "unknown"
      file_name = getattr(module, "__file__", "unknown")

      # Resolve the class name
      if inspect.isclass(context):
        class_name = context.__name__
      elif hasattr(context, "__name__"):
        class_name = context.__class__.__name__
      else:
        class_name = "module"

      function_name = function.__name__ if hasattr(function, "__name__") else "unknown"

      return {
        "file": file_name,
        "module": module_name,
        "class": class_name,
        "function": function_name
      }


  @classmethod
  def get_logger_for_context(cls, context: Any) -> logging.Logger:
    """
    Action:
      Create and return a logger named for either the class, instance, module,
    Parameters:
        * `context` `Any`: The item to get a logger for.
    Returns:
        `loging.Logger`
    Raises:
      No errors
    """

    log_info = cls.resolve_context_info(context)
    return logging.getLogger(log_info["module"])

    #
    # # If it's class, use its name
    # if inspect.isclass(context):
    #   return logging.getLogger(context.__name__)
    #
    # # If it's an instance, use the instance's name
    # if hasattr(context, '__class__'):
    #   return logging.getLogger(context.__class__.__name__)
    #
    # # Otherwise get the module(file) name
    # frame = inspect.currentframe()
    # caller_frame = frame.f_back
    # module = inspect.getmodule(caller_frame)
    # module_name = module.__name__ if module else "unknown"
    #
    # return logging.getLogger(module_name)

  @classmethod
  def log_info(cls, context: Any, message: str) -> None:
    """
    Action:
      Log informational messages for the context
    Parameters:
        * `context` `Any`: The item to write into the info log.
        * `message` `str`: Information about the context
    Returns:
        `void`
    Raises:
      No errors
    """

    context_info = cls.resolve_context_info(context)
    logger = cls.get_logger_for_context(context)
    logger.info("[%s.%s:%s] %s", context_info["class"], context_info["function"], context_info["file"])


  @classmethod
  def log_error(cls, context: Any, exception: Exception,  function: Optional[Callable]=None) -> None:
    """
    Action:
    Write error to the logger for the class, instance or module.
    Parameters:
      * `context` `Any`: The item to write into the error log.
      * `message` `str`: The message to log.
    Returns:
      `void`
    Raises:
      No errors
    """

    context_info = cls.resolve_context_info(context)
    logger = cls.get_logger_for_context(context)
    logger.error(
        "[%s.%s:%s] %s: %s",
        context_info["class"],
        context_info["function"],
        context_info["file"],
        exception.__class__.__name__,
        str(exception),
        exc_info=exception
    )