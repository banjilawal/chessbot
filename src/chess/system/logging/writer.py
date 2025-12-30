# src/chess/system/logging/writer.py

"""
Module: chess.system.writer
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

import inspect
import logging
from typing import Callable, TypeVar, Any, Optional, Dict

T = TypeVar('V')

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
      ACTION:
        Derive `map` metadata for logging, including
          - file visitor_name
          - module visitor_name
          - class visitor_name
          - function visitor_name when its available

      PARAMETERS:
        * `map (`Any`)`:
        * `function` (`Callable`):

      RETURNS:
        Dict

      RAISES:
        None
      """
      method = "LogWriter.resolve_context_info"

      frame = inspect.currentframe()
      caller_frame = frame.f_back if frame and frame.f_back else None

      module = inspect.getmodule(caller_frame)
      module_name = module.__name__ if module is not None else "unknown"
      file_name = getattr(module, "__file__", "unknown")

      # Resolve the class visitor_name
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
    ACTION:
      Create and return a logger named for either the class, instance, module,
    PARAMETERS:
        * `map` `Any`: The item to get a logger for.
    RETURNS:
        `loging.Logger`
    RAISES:
      No errors
    """

    log_info = cls.resolve_context_info(context)
    return logging.getLogger(log_info["module"])

    #
    # # If it's class, use its visitor_name
    # if inspect.isclass(map):
    #   return logging.getLogger(map.__name__)
    #
    # # If it's an instance, use the instance's visitor_name
    # if hasattr(map, '__class__'):
    #   return logging.getLogger(map.__class__.__name__)
    #
    # # Otherwise get the module(file) visitor_name
    # frame = inspect.currentframe()
    # caller_frame = frame.f_back
    # module = inspect.getmodule(caller_frame)
    # module_name = module.__name__ if module else "unknown"
    #
    # return logging.getLogger(module_name)

  @classmethod
  def log_info(cls, context: Any, message: str) -> None:
    """
    ACTION:
      Log informational messages for the map
    PARAMETERS:
        * `map` `Any`: The item to write into the info log.
        * `message` `str`: Information about the map
    RETURNS:
        `void`
    RAISES:
      No errors
    """

    context_info = cls.resolve_context_info(context)
    logger = cls.get_logger_for_context(context)
    logger.info("[%s.%s:%s] %s", context_info["class"], context_info["function"], context_info["file"])


  @classmethod
  def log_error(cls, context: Any, exception: Exception,  function: Optional[Callable]=None) -> None:
    """
    ACTION:
    Write error to the logger for the class, instance or module.
    PARAMETERS:
      * `map` `Any`: The item to write into the error log.
      * `message` `str`: The message to log.
    RETURNS:
      `void`
    RAISES:
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