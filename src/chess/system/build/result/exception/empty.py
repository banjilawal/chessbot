# src/chess/system/build/result/exception/empty.py

"""
Module: chess.system.build.result.exception.empty
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ResultException


class EmptyBuildResultException(BuildException, ResultException):
    """BuildResult must contain either a payload or an exception"""
    ERROR_CODE = "EMPTY_BUILD_RESULT_ERROR"
    DEFAULT_MESSAGE = "BuildResult must contain either a payload or an exception. It cannot be empty."